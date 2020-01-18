# Function find Ukrainian Holidays
import colorama
from colorama import Fore, Back, Style
colorama.init()

day = int(input("Enter any day: "))
month = int(input("Enter any month: "))


def date(month, day):
    if month == 1 and day == 1:
        print(Fore.YELLOW+"\t1.01\t!!!Heppy New Year!!!")
    elif month == 1 and day == 7:
        print(Fore.YELLOW+"\t7.01\t!!!Merry Christmas!!!")
    elif month == 5 and day == 9:
        print(Fore.YELLOW+"\t9.05\t!!!Day of Victory!!!")
    elif month == 8 and day == 24:
        print(Fore.YELLOW+"\t24.08\t!!!Independence Day!!!")
    elif month == 9 and day == 13:
        print(Fore.YELLOW+"\t13.09\tMy birthday\t!,,!. q(-_-)p .!,,!")
    else:
        print(Fore.RED+"Sorry wrong date (o_0)")


date(month, day)
