my_food = ['Pizza', 'Cheeseburger', 'Fries']
friends_food = my_food[:]

my_food.append('Garbage')
friends_food.append("Ice Cream")

print(my_food)
print(friends_food)

popped_food1 = my_food.pop()
print(my_food)
print("I took out " + popped_food1)
