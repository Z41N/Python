#Create list of friends
friends = ['anthony', 'Alex', '   Anh']

#Print list of friends
#Print each individual friend afterwards
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print('\n')

#Created a message using all 3 names in the list. 
#Used some methods to kind of play around with them. 
#Purposely messed up the formatting of the names in the list above 
#just so I can use methods lol
message = "One of my friends, " + friends[1] + ", always knows what to do. \nHowever, " + friends[0].title() + " is the exact opposite. \nDon't even get me started on " + friends[2].strip() + "."
print(message)

