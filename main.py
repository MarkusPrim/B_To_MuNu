import numpy


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
        self.fermi_coupling_constant = 1.1663786e-5 * Unit.GeV**-2
        self.b_meson_mass = 5279.26 * Unit.MeV
        self.b_meson_lifetime = 1.638e-12 * Unit.s
        self.decay_constant = 0.191 * Unit.GeV
        self.v_ub = 4.13e-3
        self.electron_mass = 0.510998929 * Unit.MeV
        self.muon_mass = 105.6583715 * Unit.MeV
        self.tau_mass = 1776.82 * Unit.MeV

    def standard_model_branching_ratio(self, lepton_mass):
        """ Standard Model prediction for the given lepton mass.
        Equation taken from Physics at the B-factories p.396.

        :param lepton_mass:
        :return:
        """
        x = self.fermi_coupling_constant**2 * self.b_meson_mass * lepton_mass**2 / (8 * numpy.pi)
        helicity_suppression = (1 - (lepton_mass / self.b_meson_mass)**2)**2
        y = self.decay_constant**2 * self.v_ub**2 * self.b_meson_lifetime
        return x * helicity_suppression * y


if __name__ == '__main__':
    calculator = BToMuNuCalculations()
    e = calculator.standard_model_branching_ratio(calculator.electron_mass)
    mu = calculator.standard_model_branching_ratio(calculator.muon_mass)
    tau = calculator.standard_model_branching_ratio(calculator.tau_mass)

    print("BR(B->e nu):\t{:.2e}".format(e))
    print("BR(B->mu nu):\t{:.2e}".format(mu))
    print("BR(B->tau nu):\t{:.2e}".format(tau))

    print("BR(B->e nu) / BR(B->tau nu):\t{:.2e}".format(e/tau))
    print("BR(B->mu nu) / BR(B->tau nu):\t{:.2e}".format(mu/tau))
