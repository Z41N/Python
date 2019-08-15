guestlist = ['Sheraz', 'Tayyaba', 'Mehak', 'Anum']
print("The guest list currently contains the following people:\n" + str(guestlist))

cant_come = 'Sheraz'
guestlist.remove(cant_come)
print ("\n" + cant_come + " has been removed from the guestlist.\n") 

can_come = 'Ashley'
guestlist.insert(0, can_come)
print(can_come + " has been added to the guestlist\n")
print("The new guest list is now: \n\n" + str(guestlist))

print(guestlist[0] + ", please accept this invite")
print(guestlist[1] + ", please accept this invite")
print(guestlist[2] + ", please accept this invite")
print(guestlist[3] + ", please accept this invite\n")

print("More attendees have expressed interest; therefore a larger table has been secured. Here's the new list:")

guestlist.insert(0,'Jay')
guestlist.insert(2, 'Choi')
guestlist.append('Alex')
print(guestlist)


print("\n")
print('There was an issue... now I can only bring 2 people with me...')
guestlist.pop(0)
print(str(guestlist[0]) + " has been removed")
guestlist.pop(0)
print(str(guestlist[0]) + " has been removed")
guestlist.pop(0)
print(str(guestlist[0]) + " has been removed")
guestlist.pop(0)
print(str(guestlist[0]) + " has been removed")
guestlist.pop(0)
print(str(guestlist[0]) + " has been removed")
print("\n")
print("The following users remain:\n" + str(guestlist))

del guestlist[0]
del guestlist[0]
print(guestlist)


