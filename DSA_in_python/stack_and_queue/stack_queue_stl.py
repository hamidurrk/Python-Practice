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


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

#---------------------Stack Implementation--------------
stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print(stack.peek())  

print(stack.pop())  

print(stack.is_empty())  

print(stack.size()) 

#-------------------------------------------------------

#---------------------Queue Implementation--------------
queue = Queue()

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

print(queue.front())  

print(queue.dequeue())  

print(queue.is_empty())  

print(queue.size())  

#-------------------------------------------------------v