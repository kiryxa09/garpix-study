def sum(a, b):
  try:
    return a + b
  except:
   print('Ожидаемый тип данных — число')

print(sum(1, 2))
print(sum(1, [1, 2, 3]))