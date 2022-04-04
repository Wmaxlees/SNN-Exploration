# Leaky Integrate-and-Fire neuron using euler method to calculate

# https://en.wikipedia.org/wiki/Biological_neuron_model#Leaky_integrate-and-fire

class LIFNeuron:
  Cm = 3

  Vrest = -60
  Vreset = -70
  Vth = -40
  Vspike = 20
  R = 6

  def __init__(self):
    self._Vm = -60

  def __call__(self, I, dt):
    if self._Vm >= self.Vspike:
      self._Vm = self.Vreset
    elif self._Vm >= self.Vth:
      self._Vm = self.Vspike
    else:
      self._Vm += (I - (self._Vm / self.R)) * dt / self.Cm

    return self._Vm
