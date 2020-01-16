#Function for checking speed sportsman
import colorama
from colorama import Fore, Back, Style
colorama.init()

distance = float(input("Відстань в метрах яку пробіг спортсмен: "))
time = float(input("Скліьки часу в секундах витратив спортсмен на забіг: "))


def speed_test(distance, time):
    result = distance / time
    return result


result = speed_test(distance, time)
print(Fore.RED + "Швидкість з якою рухався спортсмен:",
      result, "m/s\n або", result*3600/1000,"км/год")
