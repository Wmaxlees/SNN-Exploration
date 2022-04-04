# The Hodgkin Huxley Neuron model using the Euler Method

# Sources
# =======
# https://en.wikipedia.org/wiki/Numerical_methods_for_ordinary_differential_equations
# https://www.math.mcgill.ca/gantumur/docs/reps/RyanSicilianoHH.pdf

import math

class HHNeuron:
  Cm = 0.01

  Ek = -72.14
  ENa = 55.17
  El = -49.42

  G_bar_k = 0.36
  G_bar_Na = 1.2
  G_bar_l = 0.003

  def __init__(self):
    self._Vm = -60
    self._m = self.alpha_m(self._Vm) / (self.alpha_m(self._Vm) + self.beta_m(self._Vm))
    self._n = self.alpha_n(self._Vm) / (self.alpha_n(self._Vm) + self.beta_n(self._Vm))
    self._h = self.alpha_h(self._Vm) / (self.alpha_h(self._Vm) + self.beta_h(self._Vm))

  def __call__(self, I):
    self._n += ((self.alpha_n(self._Vm) * (1-self._n)) - (self.beta_n(self._Vm) * self._n)) * dt
    self._m += ((self.alpha_m(self._Vm) * (1-self._m)) - (self.beta_m(self._Vm) * self._m)) * dt
    self._h += ((self.alpha_h(self._Vm) * (1-self._h)) - (self.beta_h(self._Vm) * self._h)) * dt

    GNa = self.G_bar_Na*(self._m**3)*self._h
    Gk = self.G_bar_k*(self._n**4)
    Gl = self.G_bar_l

    INa = GNa * (self._Vm - self.ENa)
    Ik = Gk * (self._Vm - self.Ek)
    Il = Gl * (self._Vm - self.El)

    self._Vm += dt * ((1/self.Cm) * (I - (INa + Ik + Il)))

    return self._Vm

  def alpha_n(self, u):
    return (0.01*(u + 50))/(1 - math.exp(-(u+50)/10))

  def beta_n(self, u):
    return 0.125 * math.exp(-(u+60)/80)

  def alpha_m(self, u):
    return (0.1 * (u + 35))/(1 - math.exp(-(u+35)/10))

  def beta_m(self, u):
    return 4.0 * math.exp(-0.0556 * (u+60))

  def alpha_h(self, u):
    return 0.07 * math.exp(-0.05 * (u+60))

  def beta_h(self, u):
    return 1/(1 + math.exp(-0.1 * (u+30)))
