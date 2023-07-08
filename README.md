# Python-Practice (Assignments & Leetcodes)

## Q1.py (Question 1)
### Description:
This code simply uses a for loop to generate 1 billion random integers between 0 and 999 using the `random.randint()` function. It then writes each number to a file called `random_numbers.txt`.
Since, this code can still take a long time to run and may use a lot of memory, so we are generating the numbers and writing it to a file.

## Q2.py (Question 2)
### Description:
This code defines a `Node class` to represent a node in the linked list, and a `LinkedList class` to represent the linked list itself. The LinkedList class has methods to `append` new nodes to the end of the list, `view` data at a given index, `reverse` the list, and `sort` the list.

To create the linked list from data read from a file, we first read the data from the file using `open()` and `read()` functions, then loop through the data and append each element to the linked list using the `append()` method.

We can view the data at a given index in the linked list using the `view()` method, which traverses the list until it reaches the desired index and returns the data at that index.

To reverse the linked list, we traverse the list using three pointers: `prev_node`, `current_node`, and `next_node`. We set `current_node` to the __head__ of the list and `prev_node` to __None__. We then loop through the list, setting `next_node` to the node following `current_node`, then setting the __next__ attribute of `current_node` to `prev_node`, and finally setting `prev_node` to `current_node` and `current_node` to `next_node`.
