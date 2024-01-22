n = input("Введите число: ")

counter = 0
for i in range(1, int(n) + 1):
  print(i)
  if int(i) % 2 == 0:
    counter += 1

print(f"Количество четных цифр: {counter}")