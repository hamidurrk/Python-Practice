import random
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

def generate_random_data(n):
    data = []
    opening_parentheses = "([{"
    closing_parentheses = ")]}"
    
    for _ in range(n):
        string = ""
        length = random.randint(1, 20)  
        
        for _ in range(length):
            if random.random() < 0.5:
                string += random.choice(opening_parentheses)
            else:
                string += random.choice(closing_parentheses)
        
        data.append(string)
    
    return data

def is_balanced_parentheses(string):
    stack = Stack()
    opening_parentheses = "([{"
    closing_parentheses = ")]}"
    for char in string:
        if char in opening_parentheses:
            stack.push(char)
        elif char in closing_parentheses:
            if stack.size() == 0:
                return False
            last_opening = stack.pop()
            if opening_parentheses.index(last_opening) != closing_parentheses.index(char):
                return False
    return stack.size() == 0

print("Generating random data...")
random_data = generate_random_data(10000000)
balanced_count = 0
not_balanced_count = 0
print("Random data generated. Checking for imbalance...")
for string in random_data:
    if is_balanced_parentheses(string):
        #print(f"{string}: Balanced")
        balanced_count += 1
    else:
        #print(f"{string}: Not balanced")
        not_balanced_count += 1
print(f"{balanced_count}: Balanced")
print(f"{not_balanced_count}: Not Balanced")