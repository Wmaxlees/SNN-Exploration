class IzhNeuron:
  a = .004
  b = 2
  c = -70
  d = 4

  def __init__(self):
    self._Vm = -60
    self._u = -15

  def __call__(self, I, dt):
    self._Vm += (0.04*(self._Vm**2) + 5*self._Vm + 140 - self._u + I) * dt
    self._u += (self.a * (self.b * self._Vm - self._u)) * dt

    if self._Vm >= 30:
      self._Vm = self.c
      self._u = self._u + self.d

    return self._Vm
  
