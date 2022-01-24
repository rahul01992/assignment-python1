#python assignment 2
#Name-Onkar Ram  SID-21103123

#question 1
string=str(input("Enter the string\n"))
print(string)

#part a
print("\nThe length of string is ",len(string))

#part b
print("\nThe reverce string is ",string[: :-1])

#part c
new_string=string[9:26]
print("\nnew string is: ",new_string)

#part d
replaced_string=string.replace("a case sensitive","object oriented")
print("\n The replaced string is ",replaced_string)

#part e
print("\nThe index of 'a' in given string is: ",string.index("a"))

#part f
print("The string after removing spaces is ",string.replace(" ",""))




