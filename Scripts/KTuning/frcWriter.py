from sys import argv
openFile=open(argv[3]+"metalsFQ.frc","w");

openFile.write("""

begin Options
      Name                  metalsFQ
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
O        15.9994
Pt      195.09
end BaseAtomTypes

begin EAMAtomTypes
// Equlibrium distances (re) are in angstroms, density parameters (fe,rhoe) are
// in eV/angstrom. Most others (alpha, beta, kappa, lambda, eta) are
// dimensionless. Spline parameters for the energy functional (Fn0, Fn1, Fn2,
// Fn3, F0, F1, F2, F3, Fe) are in eV.
//
// Type     lat re       fe       rhoe      rhos      alpha    beta     A        B        kappa    lambda    Fn0       Fn1      Fn1       Fn3      F0    F1 F2       F3        eta      Fe        rhol rhoh
Pt Zhou2004 FCC 2.771916 2.336509 33.367564 35.205357 7.105782 3.78975  0.556398 0.696037 0.385255 0.77051  -1.455568 -2.149952 0.528491  1.222875 -4.17 0  3.010561 -2.420128 1.45     -4.145597 0.25 1.15
// Oxygen is special - There are splines over a range of values:
// Equlibrium distances (re) are in angstroms, density parameters (fe,
// rhoe[*],rholimits[*]) are in eV/angstrom.  Most others (alpha, beta, kappa,
// lambda, gamma, nu) are dimensionless. Spline parameters for the energy
// functional (F[*]) are in eV
// Type            re (Å)  fe      α       β       A (eV)  B (eV)  κ       λ       γ       ν       ρlimits                                 ρe[0]    ρe[1]    ρe[2]    ρe[3]    ρe[4]     F[0]                              F[1]                     F[2]                     F[3]                     F[4]
O  Zhou2005Oxygen  3.64857 1.39478 5.44072 2.11725 0.34900 0.57438 0.08007 0.37457 2.11725 0.37457 0.0 54.62910 65.24078 66.56797 70.57748 54.62910 64.26953 66.21202 66.92391 74.23105 -1.56489 -1.39123 1.77199 1.59833 -1.58967 1.30636 9.81033 -1.54116 2.02821 6.56240 -1.51798 2.30979 7.69582 -1.19082 4.12936 10.32338
end EAMAtomTypes

begin NonBondedInteractions
//Types         re (Å)  α       β       A (eV)  B (eV)  κ       λ
// O  O  EAMZhou   3.64857 5.44072 3.59746 0.34900 0.57438 0.08007 0.39310
//Types   ShiftedMorse  r0  D0  β
O O ShiftedMorse  1.05  17.9 2.4
end NonBondedInteractions

begin AtomTypes
//name baseatomtype
Pt_FQ  Pt
O_FQ    O
end AtomTypes

begin FluctuatingChargeAtomTypes
// Fictitious ChargeMass has units of (fs / e)^2 kcal / mol  (note the ps->fs difference between
// this code and the Rick, Stuart, and Berne paper
//Name  chargeMass (fs^2 kcal/e^2 mol) EAM  nValence coupling  q0 u0 k0 q1 u1 k1 q2 u2 k2
%s_FQ 	40000.0 EAM   1.64 0.0   0.0 0.0 %f
O_FQ 	40000.0 EAM    6 0.15  0.0 0.0 18.6119 -0.4 -1.4611105 38.07881 -0.8 7.275718 57.544
//_FQ 	40000.0 EAMSlater   1.64 2.771916 3.789750 0.0   0.0 0.0 8
end FluctuatingChargeAtomTypes

"""%(argv[1],float(argv[2])))
openFile.close();
