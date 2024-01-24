lst1 = ['Иваново', 'Санкт-Петербург', 'Москва', 'Казань', 'Новосибирск', 'Воронеж']
lst2 = ['Воронеж', 'Санкт-Петербург', 'Иваново', 'Волгоград']

matchList = []
missList = []

for i in lst1:
  if i in lst2:
    matchList.append(i)
  elif i not in lst2:
    missList.append(i)

for j in lst2:
  if j not in lst1:
    missList.append(j)


print(matchList)
print(missList)