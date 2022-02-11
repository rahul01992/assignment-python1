a=str(input("ENTER ANY STRING: "))
list=a.split() #To split all the elements of string in a list
dict={} #initializing an empty dictionary
if list.__len__()==1:   #if statement will be implemented when a single word is entered
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
else:
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")
