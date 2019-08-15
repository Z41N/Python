#Okay so I know how to create a list now.
#What about modifying data in those lists... lets see
motorcycles = ['Kawasaki', 'Ducati', 'Honda']
print(motorcycles)

#Kawasaki is king btw
#Anyway, now we want to modify one of the elements. Literally replace:
motorcycles[1] = 'Harley'
print(motorcycles)

#Okay so that replaced it. 
#Ducati is d-d-d-dont btw LOL
#Getting too carried away with comments...okay lets get serious:


#ADDING ELEMENTS:
motorcycles.append('Indiana')
print(motorcycles)

#append does the trick, but adds as last index
#Adding more elements, since order does not matter righit now:
motorcycles.append('Yamaha')
print(motorcycles)

#Can create blank list as a placeholder, to add data to later
#Especially useful considering users will control when data is added
motorcycles = []
print (motorcycles)
motorcycles.append('Kawasaki')
motorcycles.append('Tabi')
motorcycles.append('Ninja')
print(motorcycles)

#Now, for this last list, we want to add new information
#We can do so, using insert (X,Y), X=position, Y=string
motorcycles.insert(1,'Deadman')
print(motorcycles)

#DELETING ELEMENTS:
del motorcycles[2]
print(motorcycles)

