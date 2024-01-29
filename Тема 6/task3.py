class Nikola:
  def __init__(self, name, age):
    if name == "Николай":
      self.name = name
    else:
      self.name = (f"Я не {name}, а Николай")
    self.age = age

  def about_me(self):
    #new line after name
    print(f"Имя: {self.name} \nВозраст: {self.age} лет")


Nick = Nikola("Николай", 18)
Nick.about_me()
Max = Nikola("Максим", 19)
Max.about_me()