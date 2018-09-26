class utask
  def __init__ (self, name, desc, state, progress, deadline)
    self._name = name
    self.desc = desc
    self.state = state
    self.progress = progress
    self.deadline = deadline

  """Operaciones"""
  def add(self, name, desc) 
    self.name = name
    self.desc = desc

  def remove(self, name)
    search(self._name == name).remove()

  def list
    for utask in utaskList
      print(utask)

  def go(self, name, state)
    search(self._name == name).add(utastk._state = state)
