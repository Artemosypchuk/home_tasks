import colorama
from colorama import Fore, Back, Style
colorama.init()

# Обчислення споживання пального Вашого авто!


car = input("Введіть марку вашого авто: ")  # для стилізації результату
# перша змінна
distance = float(input("Введіть відстань до пункту призначення в км.: "))
# друга змінна
fuel = float(input("Кількість споживання палива /100км: "))


def result(distance, fuel):  # Функція обчислення
    res = distance / 50 * fuel
    print("Ваш автомобіль", Fore.LIGHTRED_EX + car.upper(), Fore.RESET + "витратить",
          Fore.YELLOW + str(res),Fore.RESET+ "л. пального в дві сторони!")


result(distance, fuel)
