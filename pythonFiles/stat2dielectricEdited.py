
"""A script that computes the static dielectric constant

Accumulates the static dielectric constant from an OpenMD stat file
that has been run with the SYSTEM_DIPOLE added to the statFileFormat.

This assumes the fluctuation formula appropriate for conducting
boundaries:

                     <M^2> - <M>^2
        epsA = 1 + -----------------
                   3 kB <T> <V> eps0
   
        epsA: dielectric constant
        M:    total dipole moment of the box
        <V>:  average volume of the box
        <T>:  average temperature
        eps0: vacuum permittivity
        kB:   Boltzmann constant

See M. Neumann, O. Steinhauser, and G. S. Pawley, Mol. Phys. 52, 97 (1984).

Also, optionally applies a correction factor as follows:

                ((Q + 2) (epsA - 1) + 3)
          eps = ------------------------
                ((Q - 1) (epsA - 1) + 3)

Where Q depends on the method used to compute the electrostatic interaction.
See M. Neumann and O. Steinhauser, Chem. Phys. Lett. 95, 417 (1983))

Usage: stat2dielectric 

Options:
  -h, --help              show this help
  -f, --stat-file=...     use specified stat file
  -o, --output-file=...   use specified output (.dielectric) file
  -q, --Q-value=...       use the specified Q value to correct the dielectric

To use this, the OpenMD file for the run should specify:

statFileFormat = "TIME|TOTAL_ENERGY|POTENTIAL_ENERGY|KINETIC_ENERGY|TEMPERATURE|PRESSURE|VOLUME|CONSERVED_QUANTITY|SYSTEM_DIPOLE";

This line will get OpenMD to compute the total system dipole and place
it in the final three columns of the stat file.  The stat2dielectric
script looks for the temperature in column 5, the volume in column 7,
and the dipole vector in the last 3 columns of the stat file.

Example:
   stat2dielectric -f stockmayer.stat -o stockmayer.dielectric

"""

__author__ = "Dan Gezelter (gezelter@nd.edu)"
__version__ = "$Revision:  $"
__date__ = "$Date:  $"

__copyright__ = "Copyright (c) 2014 by the University of Notre Dame"
__license__ = "OpenMD"

import sys
import getopt
import string
import math

def usage():
    print __doc__

def readStatFile(statFileName):
    global time
    global temperature
    global volume
    global boxDipole
    time = []
    temperature = []
    volume = []
    boxDipole = []

    statFile = open(statFileName, 'r')
    line = statFile.readline()
    line=statFile.readline()
    print "reading File"
    line = statFile.readline()
    while 1:
        L = line.split()

        time.append(float(L[0]))
        temperature.append(float(L[4]))
        volume.append(float(L[6]))
        dipX = float(L[-3])
        dipY = float(L[-2])
        dipZ = float(L[-1])
        boxDipole.append([dipX, dipY, dipZ])
                       
        line = statFile.readline()
        if not line: break
        
    statFile.close()
    
def computeAverages(outFileName, Q):

    # permittivity in C^2 N^-1 m^-2
    eps0 = 8.854187817620E-12
    # Boltzmann constant in J / K
    kB = 1.380648E-23
    # Convert angstroms^3 to m^3
    a3tom3 = 1.0E-30

    M2 = 0.0
    M = 0.0
    Dx = 0.0
    Dy = 0.0
    Dz = 0.0
    Temp = 0.0
    Vol = 0.0
    
    print "computing Dielectrics"
    outFile = open(outFileName, 'w')

        
    outFile.write("#time\t x1\t d1\t d3\t corrected\n")
    for i in range(len(time)):

        dipX = boxDipole[i][0]
        dipY = boxDipole[i][1]
        dipZ = boxDipole[i][2]

        length2 = dipX*dipX + dipY*dipY + dipZ*dipZ
        M2 += length2
        M2avg = M2 / float(1+i)

        Dx += dipX
        Dy += dipY
        Dz += dipZ

        # the average of each of the three components of the box dipole
        Mx = Dx / float(1+i)
        My = Dy / float(1+i)
        Mz = Dz / float(1+i)
        Mavg = Mx*Mx + My*My + Mz*Mz

        # the average of the box dipole vector length
        M += math.sqrt(length2)
        Mavg2 = M / float(1+i)

        Temp += temperature[i]
        Tavg = Temp / float(1+i)
        
        Vol += volume[i] * a3tom3
        Vavg = Vol / float(1+i)

        x1 = (M2avg - Mavg) / (9.0*eps0*kB*Tavg*Vavg)
        #x2 = (M2avg - Mavg2*Mavg2) / (9.0*eps0*kB*Tavg*Vavg)       

        # Clausius-Mossotti
        d1 = (2.0 * x1 + 1.0) / (1.0 - x1)
        #d2 = (2.0 * x2 + 1.0) / (1.0 - x2)

        # Conducting boundary conditions
        d3 = 1.0 + 3.0*x1 
        #d4 = 1.0 + 3.0*x2 
        
        #d1 = 1.0 + (M2avg - Mavg) / (3.0*eps0*kB*Tavg*Vavg)
        #d2 = 1.0 + (M2avg - Mavg2*Mavg2) / (3.0*eps0*kB*Tavg*Vavg)

        corrected1 = ((Q+2.0)*(d3 - 1.0) + 3.0)/((Q-1.0) * (d3 - 1.0) + 3.0)
        #corrected2 = ((Q+2.0)*(d4 - 1.0) + 3.0)/((Q-1.0) * (d4 - 1.0) + 3.0)

        #corrected1 = (1.0 + 2.0*x1 + Q*x1)/(1.0 - x1 - Q*x1)
        #corrected2 = (1.0 + 2.0*x2 + Q*x2)/(1.0 - x2 - Q*x2)
        
        outFile.write("%lf\t%lf\t%lf\t%lf\t%lf\n" % (time[i], x1, d1, d3, corrected1))

    outFile.close()


def main(argv):
    global haveStatFileName
    global haveOutputFileName
    global haveQValue
    
    haveStatFileName = False
    haveOutputFileName = False
    haveQValue = False
 
    try:                                
        opts, args = getopt.getopt(argv, "hq:f:o:", ["help", "Q-value=", "stat-file=", "output-file="]) 
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)                     
    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            usage()                     
            sys.exit()
        elif opt in ("-q", "--Q-value="): 
            Q = float(arg)
            haveQValue = True
        elif opt in ("-f", "--stat-file"): 
            statFileName = arg
            haveStatFileName = True
        elif opt in ("-o", "--output-file"): 
            outputFileName = arg
            haveOutputFileName = True
    if (not haveStatFileName):
        usage() 
        print "No stat file was specified"
        sys.exit()
    if (not haveOutputFileName):
        usage()
        print "No output file was specified"
        sys.exit()
    
    
    readStatFile(statFileName)
    if (not haveQValue):
        computeAverages(outputFileName, 1.0)
    else:
        computeAverages(outputFileName, Q)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
        sys.exit()
    main(sys.argv[1:])
