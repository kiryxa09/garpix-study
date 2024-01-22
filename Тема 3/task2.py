password = "supersecret"

while True:
  password_input = input("Введите пароль: ")

  if password_input == password or password_input == "q":
    print("ОК")
    break
  else:
    continue