import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def view(self, index):
        current_node = self.head
        for i in range(index):
            if current_node.next is None:
                return None
            current_node = current_node.next
        return current_node.data

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def sort(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next
            current_node = current_node.next

if __name__ == '__main__':

    #Generate data and write to a file
    with open('data_for_q2.txt', 'w') as f:
        for i in range(100):
            f.write(str(random.randint(0, 999)) + '\n')

    # Read data from file
    with open('data_for_q2.txt', 'r') as f:
        data = [int(line.strip()) for line in f]

    # Create linked list from data
    llist = LinkedList()
    for num in data:
        llist.append(num)

    # View data at index 10
    print(llist.view(10))

    # Reverse linked list
    llist.reverse()

    # Sort linked list
    llist.sort()
