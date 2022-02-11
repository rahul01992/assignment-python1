inputlist = input('Enter elements of a list separated by space ')
user_list = inputlist.split()

print('list: ', inputlist)
# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
squarelist =[(user_list[i], user_list[i]**2) for i in range(len(user_list))]
print(squarelist)
