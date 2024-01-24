list1 = [5, 5, 5, 20, 25, 50]

for i in list1:
  if list1.count(i) > 1:
    list1.remove(i)

print(list1)