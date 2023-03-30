class Goomba:
  def __init__(self, gnum=1, ghealth = 20):
    """
  Initalize the Goomba Object
  args: gnum [int] the goomba's id number, ghealth [int] the goomba's hitpoints
    """
    self.goomba_number = gnum
    self.alive = True #Goombas start alive
    self.is_small = True #Goombas start small
    self.color = "brown" #Goombas start brown 
    self.hitpoints = ghealth

class Pipe:
  def __init__(self, pnum=1):
    """
      Initalize the pipe Object
      args: pnum [int] the pipe's id number
    """
    self.pipe_number = pnum
    self.open = True #Pipes start without Mario in them
    self.is_small = True #Pipes start small
   




