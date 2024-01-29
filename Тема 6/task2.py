class ListWorker:
  def __init__(self, *args):
    self.list = list(args)

  def get_strs(self):
    return list(filter(lambda x: type(x) == str, self.list))

  def get_ints(self):
    return list(filter(lambda x: type(x) == int, self.list))

  def get_other(self):
    return list(filter(lambda x: type(x) != str and type(x) != int, self.list))
  
new_list = ListWorker(1, 2, 3, "a", "b", "c", [1, 2, 3, 4, 5])
print(new_list.get_strs())
print(new_list.get_ints())
print(new_list.get_other())