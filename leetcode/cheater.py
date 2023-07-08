from git import Repo

repo_url = 'https://github.com/hamidurrk/Python-Practice.githttps://github.com/hamidurrk/Python-Practice.git'
local_path = 'C:\\Users\\hamid\\OneDrive\\Documents\\Python-Practice'

file_path = 'C:\\Users\\hamid\\OneDrive\\Documents\\Python-Practice\\leetcode'

with open('hello.txt', 'w') as file:
    file.write('New content')

repo = Repo(local_path)

# Stage the modified file
repo.index.add([file_path])

# Commit the changes
repo.index.commit('Commit message')

origin = repo.remote('origin')

# Push the changes
origin.push()
