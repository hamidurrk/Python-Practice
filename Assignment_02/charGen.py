import random
import sys

total_chars = 100000

filename = 'random_chars.txt'

with open(filename, 'w') as f:
    for i in range(total_chars):

        char = chr(random.randint(97, 122))
        f.write(char)

        # calculate the progress percentage
        progress = (i / total_chars) * 100

        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %0.2f%%" % ('=' * int(progress), progress))
        sys.stdout.flush()

print('\nFile generation complete.')
