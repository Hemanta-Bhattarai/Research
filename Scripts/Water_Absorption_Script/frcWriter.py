from sys import argv
openFile=open(argv[5],"w");
openFile.write("""


// This is the forcefield file for the Embedded Atom Method (EAM)
// parameterized in:
//
//      X. W. Zhou, R. A. Johnson, and H. N. G. Wadley,
//      Phys. Rev. B, 69, 144113 (2004).
//
// Note that as of OpenMD version 2.5, precomputed funcfl or setfl DYNAMO files
// are not required - the splines for the electron density,
// functional, and pair potentials are computed upon initialization.
begin Options
      Name                  EAMZhou2004
      // energies in metallic force fields are usually in eV. Convert to kcal/mol:
      MetallicEnergyUnitScaling     23.0605423
      // All of the other interactions (NonBonded, Fluctuating Charge)
      // will also follow this eV convention
      EnergyUnitScaling     23.0605423
      // measure charges in electrons:
      //ChargeUnitScaling     1.0
      // measure distances in angstroms:
      DistanceUnitScaling   1.0
      EAMMixingMethod   Johnson
end Options


begin BaseAtomTypes
Cu       63.550
Ag      107.87
Au      196.97
Ni       58.710
Pd      106.40
Pt      195.09
Al       26.981538
Pb      207.2
Fe       55.845
Mo       95.94
Ta      180.94788
W       183.84
Mg       24.3050
Co       58.933195
Ti       47.867
Zr       91.224
H		1.0079
O		15.9994
D		2.0141
EP		0.0
LP		0.0
DIP         	9.00764		
SSD		18.0153		
SSD1        	18.0153 
SSD_E       	18.0153
SSD_RF      	18.0153
TAP		18.0153
TRED        	18.0153
H_DIP3P		1.0079
end BaseAtomTypes




begin AtomTypes
//name baseatomtype
OW              O
HW              H
Pt_FQ  Pt
Cu_FQ   Cu
Ag_FQ   Ag
Au_FQ   Au
Pd_FQ   Pd
Pb_FQ   Pb
Al_FQ   Al
Fe_FQ   Fe
Mo_FQ   Mo
Ta_FQ   Ta
W_FQ    W
Mg_FQ   Mg
Co_FQ   Co
Ti_FQ   Ti
Zr_FQ   Zr
Ni_FQ Ni
O_TIP4P                 OW
H_TIP4P                 HW
EP_TIP4P                EP
end AtomTypes

begin ChargeAtomTypes
//name			charge
H_TIP4P			0.520
EP_TIP4P		-1.040
end ChargeAtomTypes



begin LennardJonesAtomTypes
//name		epsilon(eV)  sigma(Angstroms)
O_TIP4P         0.006721438          3.15365
end LennardJonesAtomTypes

begin EAMAtomTypes
// Equlibrium distances (re) are in angstroms, density parameters (fe,rhoe) are
// in eV/angstrom. Most others (alpha, beta, kappa, lambda, eta) are
// dimensionless. Spline parameters for the energy functional (Fn0, Fn1, Fn2,
// Fn3, F0, F1, F2, F3, Fe) are in eV.
//
// Type     lat re       fe       rhoe      rhos      alpha    beta     A        B        kappa    lambda    Fn0       Fn1      Fn1       Fn3      F0    F1 F2       F3        eta      Fe        rhol rhoh
Cu Zhou2004 FCC 2.556162 1.554485 21.175871 21.175395 8.12762  4.334731 0.39662  0.548085 0.308782 0.756515 -2.170269 -0.263788 1.088878 -0.817603 -2.19 0  0.56183  -2.100595 0.31049  -2.186568 0.85 1.15
Ag Zhou2004 FCC 2.891814 1.106232 14.6041   14.604144 9.13201  4.870405 0.277758 0.419611 0.33971  0.750758 -1.729364 -0.255882 0.91205  -0.561432 -1.75 0  0.744561 -1.15065  0.783924 -1.748423 0.85 1.15
Au Zhou2004 FCC 2.885034 1.529021 19.991632 19.991509 9.516052 5.075228 0.229762 0.356666 0.35657  0.748798 -2.937772 -0.500288 1.601954 -0.83553  -2.98 0  1.706587 -1.134778 1.021095 -2.978815 0.85 1.15
Ni Zhou2004 FCC 2.488746 2.007018 27.562015 27.562031 8.383453 4.471175 0.429046 0.633531 0.443599 0.820658 -2.693513 -0.076445 0.241442 -2.375626 -2.7  0  0.26539  -0.152856 0.44547  -2.7      0.85 1.15
Pd Zhou2004 FCC 2.750897 1.595417 21.335246 21.940073 8.697397 4.638612 0.406763 0.59888  0.397263 0.754799 -2.321006 -0.473983 1.615343 -0.231681 -2.36 0  1.481742 -1.675615 1.13     -2.352753 0.85 1.15
//
// Note that the Pt rhol value below is not mentioned in the original paper,
// but is required for continuity of the functional.
//
Pt Zhou2004 FCC 2.771916 2.336509 33.367564 35.205357 7.105782 3.78975  0.556398 0.696037 0.385255 0.77051  -1.455568 -2.149952 0.528491  1.222875 -4.17 0  3.010561 -2.420128 1.45     -4.145597 0.25 1.15
Al Zhou2004 FCC 2.863924 1.403115 20.418205 23.19574  6.613165 3.527021 0.314873 0.365551 0.379846 0.759692 -2.807602 -0.301435 1.258562 -1.247604 -2.83 0  0.622245 -2.488244 0.785902 -2.824528 0.85 1.15
Pb Zhou2004 FCC 3.499723 0.647872  8.450154  8.450063 9.121799 5.212457 0.161219 0.236884 0.250805 0.764955 -1.42237  -0.210107 0.682886 -0.529378 -1.44 0  0.702726 -0.538766 0.93538  -1.439436 0.85 1.15
Fe Zhou2004 BCC 2.481987 1.885957 20.041463 20.041463 9.81827  5.236411 0.392811 0.646243 0.170306 0.340613 -2.534992 -0.059605 0.193065 -2.282322 -2.54 0  0.200269 -0.14877  0.39175  -2.539945 0.85 1.15
Mo Zhou2004 BCC 2.7281   2.72371  29.354065 29.354065 8.393531 4.47655  0.708787 1.120373 0.13764  0.27528  -3.692913 -0.178812 0.38045  -3.13365  -3.71 0  0.875874  0.776222 0.790879 -3.712093 0.85 1.15
Ta Zhou2004 BCC 2.860082 3.086341 33.787168 33.787168 8.489528 4.527748 0.611679 1.032101 0.176977 0.353954 -5.103845 -0.405524 1.112997 -3.585325 -5.14 0  1.640098  0.221375 0.848843 -5.141526 0.85 1.15
W  Zhou2004 BCC 2.74084  3.48734  37.234847 37.234847 8.900114 4.746728 0.882435 1.394592 0.139209 0.278417 -4.946281 -0.148818 0.365057 -4.432406 -4.96 0  0.661935  0.348147 0.582714 -4.961306 0.85 1.15
Mg Zhou2004 HCP 3.196291 0.544323  7.1326    7.1326  10.228708 5.455311 0.137518 0.22593  0.5      1        -0.896473 -0.044291 0.162232 -0.68995  -0.9  0  0.122838 -0.22601  0.431425 -0.899702 0.85 1.15
Co Zhou2004 HCP 2.505979 1.975299 27.206789 27.206789 8.679625 4.629134 0.421378 0.640107 0.5      1        -2.541799 -0.219415 0.733381 -1.589003 -2.56 0  0.705845 -0.68714  0.694608 -2.559307 0.85 1.15
Ti Zhou2004 HCP 2.933872 1.8632   25.565138 25.565138 8.775431 4.68023  0.373601 0.570968 0.5      1        -3.203773 -0.198262 0.683779 -2.321732 -3.22 0  0.608587 -0.75071  0.558572 -3.219176 0.85 1.15
Zr Zhou2004 HCP 3.199978 2.230909 30.879991 30.879991 8.55919  4.564902 0.424667 0.640054 0.5      1        -4.485793 -0.293129 0.990148 -3.202516 -4.51 0  0.928602 -0.98187  0.597133 -4.509025 0.85 1.15
end EAMAtomTypes





begin FluctuatingChargeAtomTypes
// Fictitious ChargeMass has units of (fs / e)^2 kcal / mol  (note the ps->fs difference between
// this code and the Rick, Stuart, and Berne paper
//Name  chargeMass (fs^2 kcal/e^2 mol) EAM  nValence coupling  q0 u0 k0 q1 u1 k1 q2 u2 k2
//all the parameters are converted in to eV
//Au_FQ Oxidation state of +3 excluded during fitting
Au_FQ 	400.0 EAMPoly   0.800000 1 27.87 2 2.674734 3 -84.1291 4 118.37
//Mg_FQ Oxidation state of +4 excluded in fitting
Mg_FQ 	400.0 EAMPoly   0.800000 1 23.859799 2 4.371449 3 -81.7706 4 104.19099 
Al_FQ 	400.0 EAMPoly   1.200000 1 15.3523 2 3.408248 3 0 4 14.8625 

Cu_FQ 	400.0 EAMPoly   0.800000 1 14.260142 2 4.349221 3 -4.651202 4 95.495394 5 -90.361031 6 25.570825
Ag_FQ 	400.0 EAMPoly   0.800000 1 12.699033 2 3.400839 3 6.791664 4 96.277057 5 -105.004874 6 31.359066
Ni_FQ 	400.0 EAMPoly   1.600000 1 15.930754 2 3.556433 3 -17.527848 4 100.915884 5 -83.199450 6 21.705843
Pd_FQ 	400.0 EAMPoly   1.600000 1 17.787145 2 2.370955 3 -22.655146 4 131.855262 5 -118.781967 6 32.565176
Pt_FQ 	400.0 EAMPoly   1.600000 1 19.034889 2 3.260063 3 -15.845591 4 108.339628 5 -103.304095 6 29.734526
Pb_FQ 	400.0 EAMPoly   1.600000 1 18.029287 2 3.489750 3 -40.180968 4 113.695488 5 -73.575660 6 14.895124
Fe_FQ 	400.0 EAMPoly   0.800000 1 17.754550 2 4.641886 3 -32.541335 4 118.108559 5 -96.808861 6 26.448973
Mo_FQ 	400.0 EAMPoly   2.400000 1 13.481808 2 6.453444 3 -11.149433 4 80.260391 5 -74.148205 6 20.849336
Ta_FQ 	400.0 EAMPoly   2.000000 1 15.388726 2 4.297356 3 -17.244594 4 109.121784 5 -109.024206 6 32.480561
W_FQ 	400.0 EAMPoly   2.400000 1 16.419712 2 5.045689 3 -19.868216 4 101.900161 5 -93.375451 6 26.344636
Co_FQ 	400.0 EAMPoly   0.800000 1 19.879082 2 3.778710 3 -41.260762 4 117.642647 5 -77.327563 6 16.510498
Ti_FQ 	400.0 EAMPoly   1.600000 1 11.191491 2 4.697455 3 10.786415 4 89.564871 5 -167.130612 6 80.112680
Zr_FQ 	400.0 EAMPoly   1.600000 1 13.330919 2 8.298343 3 -19.819794 4 67.275228 5 -52.130895 6 13.214623
end FluctuatingChargeAtomTypes

begin NonBondedInteractions

//Pt_FQ	O_TIP4P	Mie	2.511	0.0135	11	6
Au	O_TIP4P	Mie	%f	%f	11	6
Au	H_TIP4P	RepulsivePower	%f	%f	3

end NonBondedInteractions
"""%(float(argv[1]),float(argv[2]),float(3),float(4)))
openFile.close();
