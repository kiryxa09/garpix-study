a = input("Введите первую сторону: ")
b = input("Введите вторую сторону: ")
c = input("Введите третью сторону: ")

if int(a) == int(b) == int(c):
  print("Равносторонний")
elif int(a) == int(b) or int(a) == int(c) or int(c) == int(b):
  print("Равнобедренный")
else:
  print("Разносторонний")
