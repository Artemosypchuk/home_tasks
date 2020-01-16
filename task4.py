# def sey_Hello():
#     name = input("enter your name")
#     print("hello ", name)


# sey_Hello()

# day = 0
# counter = 0
# while True:
#     if day == 7:
#         break
#     temp = int(input("Enter 1st day temp: "))
#     day +=1
#     if temp > 10:
#         counter += 1
#     print (day)
# print("Temp more then 10", counter,"times")
# -------------------------------------------------------------------
# numb = int(input("Enter a number"))

# for a in range(1, 10):
#     print(a,"x",numb,"=",a * numb)
# -------------------------------------------------------------------

from random import randint

# count = 0
# while True:
#     rand = randint(1, 6)
#     if rand == 6:
#         break

#     count += 1
# print(rand,"you needed: ",count)

name = input("Enter your name: ")
pc = 0
user = 0
count = 0
while True:
    count += 1
    input("Your turn press Enter")
    rand1 = randint(1, 6)
    rand2 = randint(1, 6)
    if rand1 == rand2:
        user += 2
        print("	Cangradilations!!!")
    result = rand1 + rand2
    print("You throw", rand1, "and", rand2)
    
    pcrand1 = randint(1, 6)
    pcrand2 = randint(1, 6)
    if pcrand1 == pcrand2:
        pc += 2
        print("	Cangradilations!!!")
    result_pc = pcrand1 + pcrand2
    print("PC throw", pcrand1, "and", pcrand2)
    

    if result > result_pc:
        user += 1
    elif result < result_pc:
        pc += 1
    if pc == 10 or user == 10:
        break
    print(name, "score: ",user,"\tPC score: ", pc)
if pc < user:

    print("The winner is ", name, "with", user, "points!")

else:
    print("Winner is PC with ", pc, "points!")
