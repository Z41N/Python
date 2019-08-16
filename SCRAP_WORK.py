list = [value**3 for value in range(2,10)]
print(list[:])

list2 = list[:]
print(list2)

list[2] = 2000
print(list)
print(list2)
