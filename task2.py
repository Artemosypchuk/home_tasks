#Function find Ukrainian Holidays
day = int(input("Enter any day: "))
month = int(input("Enter any month: "))
def date(month, day):
    if month == 1 and day == 1:
        print("\t1.01\t!!!Heppy New Year!!!")
    elif month == 1 and day == 7:
        print("\t7.01\t!!!Merry Christmas!!!")
    elif month == 5 and day == 9:
        print("\t9.05\t!!!Day of Victory!!!")
    elif month == 8 and day == 24:
        print("\t24.08\t!!!Independence Day!!!")
    elif month == 9 and day == 13:
        print("\t13.09\tMy birthday!,,!. q(-_-)p .!,,!")
    else:print("Sorry wrong date (o_0)")
date(month,day)