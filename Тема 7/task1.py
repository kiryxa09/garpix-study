def get_6_lines(path):
  with open(path, 'r', encoding='utf-8') as file:
    return file.readlines()[:6]
  
print(get_6_lines('./poem.txt'))