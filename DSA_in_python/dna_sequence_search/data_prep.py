import re

def remove_numbers_and_whitespace(filename):
    with open(filename, 'r') as file:
        text = file.read()

    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s', '', text)

    with open(filename, 'w') as file:
        file.write(text)

filename = "dog.txt"
remove_numbers_and_whitespace(filename)
