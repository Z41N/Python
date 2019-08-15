#Regular print
print ("python")
#This /t does nothing because its the wrong \
print ("/tpython")
#This is the correct \t
print ("\tpython")
#Correct \n
print ("\n\tpython")

print("Here's why this is useful")

message = "Here's the languages that I know: \n\tPython \n\tJava \n\tC++"
print("\n")
print(message)


favorite_language = 'Python '
favorite_language = favorite_language.rstrip()
print(favorite_language)



person_name = "Zain Sheraz"
print ("Hello " + person_name + ", would you like to learn Python?")
print(person_name.title())
print(person_name.lower())
print(person_name.upper())
print ("\n")
quote = "Willing is not enough, we must do."
quote2 = "Knowing is not enough, we must apply."
quote_person = "   Bruce Lee   "
message = ('"' + quote2 + '"' + '\n"' + quote + '"\n\t-' + quote_person.strip())
print(message)
