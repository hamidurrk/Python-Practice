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
    
    def show(self):
        for item in self.stack:
            print(item, ", ", end=' ')


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
    
    def show(self):
        for item in self.queue:
            print(item, ", ", end=' ')
        
    def remove(self, item):
        temp_queue = Queue()

        while not self.is_empty():
            element = self.dequeue()
            if element != item:
                temp_queue.enqueue(element)

        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())
            
    def remove_if_divisible(self, num):
        for item in list(self.queue):
            print(item)
            if (item % num == 0):
                self.remove(item)

if __name__ == '__main__':
    nlist = []
    stack = Stack()
    queue = Queue()
    
    while True:
        try:
            flag = True
            user_input = int(input("\nEnter an integer: "))
            print("\nYou entered:", user_input, "\n")       #\n means newline
            
            if(user_input % 2 == 0):                         #a
                stack.push(user_input)
                flag = None
                        
            if(user_input % 3 == 0):                         #c
                queue.enqueue(user_input)
                stack.push(queue.dequeue())            # moving an item from queue to stack
                flag = None
            
            if (stack.size() > 0): 
                if(stack.size() % 6 == 0):                  #b
                    for i in range(stack.size() // 2):
                        if (stack.peek() != 30):            # check if the stack element is 30 or not, for question e
                            queue.enqueue(stack.pop())        # move half of the stack to the queue
                    flag = None
                
            queue.remove_if_divisible(100)
                    
            if flag:
                nlist.append(user_input)
            
            print("\nThe list:")
            print(nlist)
            
            print("\nThe stack:")
            stack.show()
            
            print("\nThe queue:")
            queue.show()
            
        except ValueError:
            print("\nError: Please enter a valid integer.\n")