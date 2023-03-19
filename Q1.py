import random

with open('random_numbers.txt', 'w') as f:
    for i in range(1000000000):
        f.write(str(random.randint(0, 999)) + '\n')
