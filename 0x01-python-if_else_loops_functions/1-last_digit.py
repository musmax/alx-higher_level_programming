#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if lastDigit > 5:
    print("Last digit of{} is{} and is greater than 5".format(number, lastDigit))
elif lastDigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastDigit))
else lastDigit < 6 and lastDigit != 0:
    print("Last digit of{} is{} and is less than 6 not 0".format(number, lastDigit))
