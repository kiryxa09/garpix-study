h = 80

real_t = input("Введите температуру воздуха: ")
needed_t = input("Введите желаемую температуру: ")
real_h = input("Введите текущую влажность: ")

if int(real_t) > int(needed_t) and int(real_h) <= h:
  print("on")
else:
  print("off")