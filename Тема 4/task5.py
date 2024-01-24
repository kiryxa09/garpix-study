lst1 = ['Иваново', 'Санкт-Петербург', 'Москва', 'Казань', 'Новосибирск', 'Воронеж']
lst2 = ['Воронеж', 'Санкт-Петербург', 'Иваново', 'Волгоград']

match_list = []
miss_list = []

for i in lst1:
  if i in lst2:
    match_list.append(i)
  elif i not in lst2:
    miss_list.append(i)

for j in lst2:
  if j not in lst1:
    miss_list.append(j)


print(match_list)
print(miss_list)