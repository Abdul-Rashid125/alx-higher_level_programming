#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)
last_digit = int(last[-1])
if last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
elif last_digit == 0:
    print('Last digit of {} is {} and is 0'.format(number,last_digit))
else:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
