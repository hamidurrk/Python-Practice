from git import Repo
import shutil
import os
import random
from datetime import datetime, timedelta

repo_url = 'https://github.com/hamidurrk/Python-Practice.githttps://github.com/hamidurrk/Python-Practice.git'

repo_path = 'C:\\Users\\hamid\\Documents\\Python-Practice'
file_path = 'C:\\Users\\hamid\\Documents\\Python-Practice\\leetcode'
leet = 'C:\\Users\\hamid\\Documents\\leet_python'

commit_messages = [
    "Solve problem using a brute force approach",
    "Optimize solution for better time complexity",
    "Implement a recursive algorithm",
    "Add test cases to validate the solution",
    "Refactor code for improved readability",
    "Apply dynamic programming technique",
    "Fix edge case scenario",
    "Update solution based on feedback",
    "Add comments to explain the code",
    "Improve variable naming for clarity",
    "Apply binary search strategy",
    "Use memoization to optimize the solution",
    "Implement a backtracking algorithm",
    "Apply sliding window technique",
    "Handle null/empty inputs gracefully",
    "Update time/space complexity analysis",
    "Implement a breadth-first search (BFS)",
    "Implement a depth-first search (DFS)",
    "Apply two-pointer approach",
    "Consider using a hash map for efficient lookup",
    "Apply a greedy algorithm",
    "Consider space-optimized data structures",
    "Implement a heap/priority queue",
    "Handle integer overflow/underflow cases",
    "Consider using a stack for efficient operations",
    "Apply bit manipulation techniques",
    "Optimize space usage by reusing variables",
    "Implement a topological sort",
    "Consider using a trie for efficient string operations",
    "Handle negative input cases appropriately",
    "Implement a union-find data structure",
    "Consider using a prefix sum array",
    "Apply the Sieve of Eratosthenes algorithm",
    "Use a custom comparator for sorting",
    "Implement an interval-based approach",
    "Consider using an adjacency list for graph representation",
    "Apply a divide and conquer strategy",
    "Handle cases with multiple pointers",
    "Use a sentinel node for linked list operations",
    "Implement a tree traversal algorithm",
    "Consider using a stack/queue for tree traversal",
    "Apply an in-order, pre-order, or post-order traversal",
    "Handle cases with multiple connected components",
    "Implement a memoization table for caching results",
    "Consider using a priority queue for efficient operations",
    "Apply an in-place sorting algorithm",
    "Handle cases with cyclic dependencies",
    "Implement an algorithm using matrix operations",
    "Consider using a virtual or dummy node",
    "Apply a sliding window with two pointers"
]

file_names = os.listdir(leet)

with open('leetcode\\tracker.txt', 'r') as file:
    n = int(file.read())
    print(f"Starting from file index: {n}")

repo = Repo(repo_path)

start_date = datetime(2025, 5, 8)
end_date = datetime(2025, 5, 20)
current_date = start_date

while current_date <= end_date and n < len(file_names):
    commits_today = random.randint(1, 2)
    for _ in range(commits_today):
        if n >= len(file_names):
            break
        source_file = os.path.join(leet, file_names[n])
        destination_file = os.path.join(file_path, file_names[n])

        print(f"Copying {source_file} to {destination_file}")
        try:
            shutil.copy(source_file, destination_file)
            n += 1
            with open('C:\\Users\\hamid\\OneDrive\\Documents\\Python-Practice\\leetcode\\tracker.txt', 'w') as file:
                file.write(str(n))
        except Exception as e:
            print(f"Error copying file: {e}")
            continue

        print("Staging...")
        repo.index.add([destination_file])

        message = random.choice(commit_messages)
        print(f"Committing with message: {message}")

        hour = random.randint(10, 18)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        commit_time = current_date.replace(hour=hour, minute=minute, second=second)
        commit_time_str = commit_time.strftime('%Y-%m-%dT%H:%M:%S')

        repo.index.commit(
            message,
            author_date=commit_time_str,
            commit_date=commit_time_str
        )
        print(f"Committed on {commit_time_str}")

    current_date += timedelta(days=1)

origin = repo.remote('origin')
origin.push()
print("Pushed successfully.")