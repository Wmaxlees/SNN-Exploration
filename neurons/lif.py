# Leaky Integrate-and-Fire neuron using euler method to calculate

# https://en.wikipedia.org/wiki/Biological_neuron_model#Leaky_integrate-and-fire

class LIFNeuron:
  Cm = .1
  R = 100

  Vrest = 0
  Vreset = -10
  Vth = 20
  Vspike = 80

  def __init__(self):
    self._Vm = 0

  def __call__(self, I, dt):
    if self._Vm >= self.Vspike:
      self._Vm = self.Vreset
    elif self._Vm >= self.Vth:
      self._Vm = self.Vspike
    else:
      self._Vm += (I - (self._Vm / self.R)) * dt / self.Cm

    return self._Vm
