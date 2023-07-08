# Python-Practice (Assignments & Leetcodes)

This repository contains Python code for some assignments and LeetCode problems. The code is written for educational purposes and may not be optimal or efficient.

## Installation
To use this repository, you need to have Python installed on your system. You can run the code in any Python IDE or terminal. You can also modify the code or add new files as per your requirements.

## Contents

The repository is organized into folders, each containing a specific assignment or a set of LeetCode problems. The folders are:

### Assignment_01
This folder contains Python code for the first assignment, which involves generating random numbers, creating and manipulating linked lists, and implementing a general tree data structure.

* __Q1.py:__ This code simply uses a for loop to generate 1 billion random integers between 0 and 999 using the `random.randint()` function. It then writes each number to a file called `random_numbers.txt`.
Since this code can still take a long time to run and may use a lot of memory, we are generating the numbers and writing them to a file.

* __Q2.py:__ This code defines a `Node class` to represent a node in the linked list, and a `LinkedList class` to represent the linked list itself. The LinkedList class has methods to `append` new nodes to the end of the list, `view` data at a given index, `reverse` the list, and `sort` the list. To create the linked list from data read from a file, we first read the data from the file using the `open()` and `read()` functions, then loop through the data and append each element to the linked list using the `append()` method. We can view the data at a given index in the linked list using the `view()` method, which traverses the list until it reaches the desired index and returns the data at that index. To reverse the linked list, we traverse the list using three pointers: `prev_node`, `current_node`, and `next_node`. We set `current_node` to the __head__ of the list and `prev_node` to __None__. We then loop through the list, setting `next_node` to the node following `current_node`, then setting the __next__ attribute of `current_node` to `prev_node`, and finally setting `prev_node` to `current_node` and `current_node` to `next_node`.

### Assignment_02
This folder contains Python code for the second assignment, which involves generating random characters and finding the probability of getting a substring match within the generated data.

* __charGen.py:__ This code is a Python script that generates a file with 100,000 random lowercase letters. It uses the random module to select a character from the ASCII range 97 to 122, which corresponds to the lowercase letters ‘a’ to ‘z’. It writes each character to the file named ‘random_chars.txt’, and displays a progress bar on the standard output stream using the sys module. The code uses a with a statement to ensure that the file is closed properly after writing.
* __Q2.py:__ This Python code searches for a given string and its substrings in a file with random characters. It generates all possible substrings of the given string using a function called genSubString. It then reads the file and compares each substring with the file contents. It counts the number of matches and partial matches for each substring length and calculates the probability of occurrence. It prints the results on the standard output stream.

### DSA_in_python
This folder contains Python implementations of some common data structures and algorithms.

* __binary_tree:__ This folder contains a module that defines a binary tree class and some methods to manipulate it, such as traversing, inserting, deleting, searching, and finding the height of the tree.

* __dna_sequence_search:__ This folder contains a module that implements a DNA sequence search algorithm using a trie data structure. The algorithm can find all occurrences of a given pattern in a DNA sequence in linear time.

* __graph/basic_terminology:__ This folder contains a module that introduces some basic graph terminology and concepts, such as vertices, edges, adjacency lists, adjacency matrices, degrees, paths, cycles, connected components, etc.

* __stack_and_queue:__ This folder contains two modules that define stack and queue classes using Python lists. The modules also demonstrate some applications of stacks and queues, such as reversing a string, checking balanced parentheses, and implementing a breadth-first search algorithm.

### LeetCode 
This folder contains Python solutions to some LeetCode problems, categorized by difficulty level and topic. The folder also contains some test cases and explanations for each solution.
