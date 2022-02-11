def Next_Date():
    list1 = [1, 3, 5, 7, 8]

    list2 = [4, 6, 9, 11]

    list3 = [2]

    list4 = [12]

    while (True):  # while loop is used so that if any wrong value is entered  then values will be entered again

        day = int(input("ENTER THE DAY: "))

        if (1 <= day <= 31):

            break

        else:

            print("Please Enter a valid day")

    while (True):  # while loop is used so that if any wrong value is entered  then values will be entered again

        month = int(input("ENTER THE MONTH OF THE YEAR: "))

        if (1 <= month <= 12):

            break

        else:

            print("Please Enter a valid month")

    while (True):  # while loop is used so that if any wrong value is entered  then values will be entered again

        year = int(input("ENTER THE YEAR: "))

        if (1800 <= year <= 2025):

            break

        else:

            print("Please Enter year from 1800 to 2025 only")

    if month in list1:

        if (day == 31):

            day = 1

            month = month + 1

            print(day, "/", month, "/", year)

        elif (day < 31):

            day += 1

            print(day, "/", month, "/", year)

        else:

            print("INVALID DATE TRY AGAIN")

            Next_Date()



    elif month in list2:

        if (day == 30):

            day = 1

            month = month + 1

            print(day, "/", month, "/", year)

        elif (day < 30):

            day += 1

            print(day, "/", month, "/", year)

        else:

            print("INVALID DATE TRY AGAIN")

            Next_Date()

    elif month in list3:

        if (year % 4 == 0):

            if (day == 29):

                day = 1

                month = month + 1

                print(day, "/", month, "/", year)

            elif (day < 29):

                day += 1

                print(day, "/", month, "/", year)

            else:

                print("INVALID DATE TRY AGAIN")

                Next_Date()

        else:

            if (day == 28):

                day = 1

                month += 1

                print(day, "/", month, "/", year)

            elif (day < 28):

                day += 1

                print(day, "/", month, "/", year)

            else:

                print("INVALID DATE TRY AGAIN")

                Next_Date()

    elif month in list4:

        if (day == 31):

            day = 1

            month = 1

            year += 1

            print(day, "/", month, "/", year)

        elif (day < 31):

            day += 1;

            print(day, "/", month, "/", year)

        else:

            print("INVALID DATE TRY AGAIN")

            Next_Date()



    else:

        print("INVALID DATE TRY AGAIN")

        Next_Date()


Next_Date()

print("\n")
