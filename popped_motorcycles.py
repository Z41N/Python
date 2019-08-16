#popping
#Here's the regular list



#Printing motorcycles now has 3 removed because it was popped
print (motorcycles)

#This just shows the value of the actual popped value
print (popped_motorcycles)
print ("\n")

#Example: given a list of motorcycles from when you purchased.
#Write a statement telling us the first motorcycle you ever bought.
all_motorcycles = ['Kawasaki', 'None2', 'Kawasaki1']
latest_motorcycle = all_motorcycles.pop(-1)

message = "The latest motorcycle I ever purchased was a " + latest_motorcycle + "."
print(message)

print ("\n")

first_motorcycle = all_motorcycles.pop(0)
message = "The first motorcycle was a " + first_motorcycle + "."
print(message)

print ("\n")
#REMOVING ITEMS BY VALUE, NOT BY INDEX LIKE ABOVE
print ("REMOVING ITEMS BY VALUE, NOT BY INDEX LIKE ABOVE")
motorcycles = ['Kawasaki', 'Honda', "Suzuki", 'Honda']
print (motorcycles)

motorcycles.remove('Honda')
print (motorcycles)


#Again
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
print("The " + too_expensive.title() + " was removed due to its high cost")

