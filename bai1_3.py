import random

a = int(input("Enter value a: "))
b = int(input("Enter value b: "))

rand_num = random.randint(0, 100)

print("Random number generated:", rand_num)

if a < rand_num < b:
    print("The number is in the range (a, b)")
else:
    print("The number is NOT in the range (a, b)")
