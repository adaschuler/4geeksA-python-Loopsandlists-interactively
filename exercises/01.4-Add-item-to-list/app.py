#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
def generate_random():
    number = random.randint(0, 10)
    return number

print(generate_random())

for x in range(10):
    my_list.append(generate_random())

    

print(my_list)
