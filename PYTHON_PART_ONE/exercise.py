import random

def last_digit(number):
    l1 = number % 10
    return l1

def second_digit(number):
    l2 = (number  / 10) % 10
    return l2

def third_digit(number):
    l3 = (number / 100) % 10
    return l3

a = random.randint(100, 1000)
guess = input("Guess the number: ")

a1 = last_digit(a)
a2 = second_digit(a - a1)
a3 = third_digit(a - ((a2 * 10) + a1))

g1 = last_digit(guess)
g2 = second_digit(guess - g1)
g3 = third_digit(guess - ((g2 * 10) + g1))

# compare with last last_digit
if g1 == a1 or g1 == a2 or g1 == a3:
    if g2 == a1 or g2 == a2 or g2 == a3:
        if g3 == a1 or g3 == a2 or g3 == a3:
            print("Close")
        else:
            print("Match")
    else:
        print("Match")

elif g2 == a1 or g2 == a2 or g2 == a3:
    if g1 == a1 or g1 == a2 or g1 == a3:
        if g3 == a1 or g3 == a2 or g3 == a3:
            print("Close")
        else:
            print("Match")
    else:
        print("Match")

elif g3 == a1 or g3 == a2 or g3 == a3:
    if g1 == a1 or g1 == a2 or g1 == a3:
        if g2 == a1 or g2 == a2 or g2 == a3:
            print("Close")
        else:
            print("Match")
    else:
        print("Match")

else:
    print("No match")

if a1 == g1 and a2 == g2 and a3 == g3:
    print("Bingo!!!")
    break
