def read_last(lines, file):
  with open(file, 'r', encoding='utf-8') as f:
    return f.readlines()[-lines:]
  
print(read_last(5, 'poem.txt'))
