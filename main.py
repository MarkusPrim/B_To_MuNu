import numpy
from uncertainties import ufloat


class Unit(object):
    GeV = 1
    MeV = 1e-3 * GeV
    eV = 1e-9 * GeV
    s = 1. / 6.582119e-16 / eV


class BToMuNuCalculations(object):

    def __init__(self):
        """ Calculates the Standard Model prediction for the B -> l nu decay.

        K.A. Olive et al. (Particle Data Group), Chin. Phys. C, 38, 090001 (2014).
        - Fermi coupling constant
        - B-Meson mass
        - B-Meson lifetime
        - V_ub
        - Electron mass
        - Muon mass
        - Tau mass

        arXiv:1212.0586v1 [hep-lat].
        - Decay constant

        :return:
        """
        self.fermi_coupling_constant = ufloat(1.1663786e-5 * Unit.GeV**-2, 0 * Unit.GeV**-2, tag="G_F")
        self.b_meson_mass = ufloat(5279.26 * Unit.MeV, 0.17 * Unit.MeV, tag="M_B")
        self.b_meson_lifetime = ufloat(1.638e-12 * Unit.s, 0.004e-12 * Unit.s, tag="tau_B")
        self.decay_constant = ufloat(0.191 * Unit.GeV, 0.009 * Unit.GeV, tag="f_B")
        # self.v_ub = ufloat(4.13e-3, 0.49e-3, tag="V_ub")  # PDG
        self.v_ub = ufloat(3.95e-3, numpy.sqrt(0.39e-3**2 + 0.38e-3**2), tag="V_ub")
        self.electron_mass = ufloat(0.510998929 * Unit.MeV, 0.000000022 * Unit.MeV, tag="m_e")
        self.muon_mass = ufloat(105.6583715 * Unit.MeV, 0.0000035 * Unit.MeV, tag="m_mu")
        self.tau_mass = ufloat(1776.82 * Unit.MeV, 0.16 * Unit.MeV, tag="m_tau")

    def standard_model_branching_ratio(self, lepton_mass):
        """ Standard Model prediction for the given lepton mass.
        Equation taken from Physics at the B-factories p.396.

        :param lepton_mass:
        :return: branching ratio
        """
        return self.fermi_coupling_constant**2 * self.b_meson_mass * lepton_mass**2 / (8 * numpy.pi) \
            * (1 - (lepton_mass / self.b_meson_mass)**2)**2 \
            * self.decay_constant**2 * self.v_ub**2 * self.b_meson_lifetime

if __name__ == '__main__':
    calculator = BToMuNuCalculations()
    e = calculator.standard_model_branching_ratio(calculator.electron_mass)
    mu = calculator.standard_model_branching_ratio(calculator.muon_mass)
    tau = calculator.standard_model_branching_ratio(calculator.tau_mass)

    print("Standard Model branching ratio predictions:")
    print("BR(B->e nu):\t{:.2e}".format(e))
    print("BR(B->mu nu):\t{:.2e}".format(mu))
    print("BR(B->tau nu):\t{:.2e}".format(tau))
    print()
    print("Electron and Muon helicity suppression compared to Tau Channel:")
    print("BR(B->e nu) / BR(B->tau nu):\t{:.2e}".format(e/tau))
    print("BR(B->mu nu) / BR(B->tau nu):\t{:.2e}".format(mu/tau))
