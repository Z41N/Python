places = ['Japan', 'Korea', 'China', 'Egypt', 'Dubai']
print("Here's the top 5 places I'd like to go:\n" + str(places))

print("Here they are sorted:\n" + str(sorted(places)))
print("Here's the original list again, unsorted, since we used sorted() instead of sort()\n" + str(places))
places.reverse()
print("Here's the reverse order:\n" + str(places))
print(places)
places.reverse()
print(places)

print(len(places))
print(places)
