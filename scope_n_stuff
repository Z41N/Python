#SCOPE N STUFF

age = 27 #global scope! does not involve the functions below

print(age)

def increase_age():
	age = 30
	def add_4(age):
		age = age + 4
		print("Nested age: " + str(age))
	add_4(age)
	print(age)

increase_age()

print(age) #that's why this one is still 27
