#3.1
# 1. Git vs. GitHub:
# Git is a version control system used to track changes in code.
# GitHub is a cloud platform that has Git repositories and lets people collaborate online.

# 2. Terminal vs. Command Line:
# The terminal is the program where you type commands.
# The command line is the actual interface where you type those commands.

# 3. Local vs. Remote Repository:
# A local repository is stored on your computer.
# A remote repository is stored on a server so others can access it.

# 4. Version Control:
# A system that tracks changes to files over time, allowing you to revert, compare, and collaborate safely.

# 5. Staging Area:
# A place where changes are gathered before they are permanently saved.

# 6. git add:
# Moves changes from your directory into the staging area.
# 7. git commit:
# Saves the changes to the repository’s history with a message attached.

# 8. git push:
# Uploads your local commits to GitHub.

# 9. git status:
# Shows the current state of your directory.

# 10. git pull:
# Fetches and merges changes from the remote repository into your local branch.

# 11. pwd:
# Shows the current folder path you’re in.

# 12. ls:
# Lists the files and folders in your current directory.

# 13. cd:
# Moves you into a different folder.

# 14. nano:
# Opens a simple text editor in the terminal to create or edit files.

# 15. touch:
# Creates a new empty file or updates an existing one.

# 16. mv:
# Moves or renames files and directories.

# 17. rm:
# Deletes files or directories. It’s permanent.

# 18. cat:
# Shows the contents of a file in the terminal.


#3.2 
#1 "pwd"

#2 "ls"

#3 "cd ../brianna_repo" and "git pull"

#4 "mv homework.py" and "../judy_decal/homework"

#5 "cd ../judy_decal/homework"

#6 "cat homework.py"

#7 "git add homework.py", "git commit -m "Finished homework"", and "git push"

#8 "git pull origin main" and "git push" (This error basically means that someone has pushed new commits to GitHub that the local copy doesn’t have.)

#9 "cd ~/Recent"

#4.1
def DataType(value):
    return type(value).__name__
print(DataType(3.14))
print(DataType(True))
print(DataType("hello"))
print(DataType([1, 2]))

#4.2
def evenOrOdd(n):
    return 'Even' if n % 2 == 0 else 'Odd'
print(evenOrOdd(7))
print(evenOrOdd(10))
print(evenOrOdd(-4))
print(evenOrOdd(0))

#5
def SumLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [1, 2, 3, 4, 5]
print(SumLoop(numbers))

#6.1
def duplicateList(lst):
    result = []
    for item in lst:
        result.extend([item, item])
    return result
print(duplicateList(['a', 'b', 'c']))

 #6.2
 #What was wrong: def square(num) needed a ":" placed after it
def square(num):
    return num * num
print(square(5))
print(square(-3))

#7.2
def duplicateList(lst):
    result = []
    for item in lst:
        result.extend([item, item])
    return result
list = ['a', 'b', 'c']
result = duplicateList(list)
print(duplicateList(list))