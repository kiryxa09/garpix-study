a = input("Введите первую сторону: ")
b = input("Введите вторую сторону: ")
с = input("Введите третью сторону: ")

if int(a) == int(b) == int(с):
  print("Равносторонний")
elif int(a) == int(b) or int(a) == int(с) or int(с) == int(b):
  print("Равнобедренный")
else:
  print("Разносторонний")
