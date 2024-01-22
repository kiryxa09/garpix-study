a = input("Введите первую сторону: ")
b = input("Введите вторую сторону: ")
c = input("Введите третью сторону: ")

if int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(c) + int(b) > int(a):
  print("Треугольник существует")
else:
  print("Треугольник не существует")
