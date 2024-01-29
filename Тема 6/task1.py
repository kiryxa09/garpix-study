class Parallelepiped:
  def __init__(self, a, b, h):
    self.a = a
    self.b = b
    self.h = h

  def get_volume(self):
    return self.a * self.b * self.h
  
  def get_base_area(self):
    return self.a * self.b
  
  def get_sides_area(self):
    return (self.a * 2 + self.b * 2) * self.h
  
  def info(self):
    print("Методы класса: self.get_volume(), self.get_base_area(), self.get_sides_area()")
  

abc = Parallelepiped(10, 20, 30)
print(abc.get_volume())
print(abc.get_base_area())
print(abc.get_sides_area())
abc.info()