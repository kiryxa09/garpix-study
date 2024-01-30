class NameContainsNumbersError(Exception):
  pass

def check_name(name):
  if any(char.isdigit() for char in name):
    raise NameContainsNumbersError('Имя не может содержать в себе цифры')
  else:
    print(name)

check_name('Николай7')