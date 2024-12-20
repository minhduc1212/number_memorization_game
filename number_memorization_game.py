import random
from time import sleep

def random_number(a):
    for i in range (a):
        g_n =  random.randint(1, 9)
        list_of_numbers.append(g_n)
        print(f'number_{i} is:', g_n)
    return list_of_numbers

a = 3

print("Welcome to the Number Memorization Game!")
print("You will be shown a number and you have to memorize it.")
print("You will be asked to enter the number after a few seconds.")
sleep(1)
print("1")
sleep(1)
print("2")
sleep(1)
print("3")
print("Let's start!")



while True:
    list_of_numbers = []
    correct = True
    random_number(a)
    sleep(2)
    for i in range (a):
        print(f'Enter number {i} you saw:')
        f_input = int(input())
        if f_input != list_of_numbers[i]:
            correct = False
            break
    if correct:
        print("Congratulations! You got all the numbers right!")
        a += 1
    else:
        print("Sorry! You got some numbers wrong. Try again!")
        print("The correct numbers were:")
        print("Your points are: ", a - 3)
        break


    