#--- variable and data types ---
a = 10
print(a)
print(type(a)) #a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) #b is a floater, a number containing fractions and decimals

c = 3j
print(c)
print(type(c)) #c is a complex, consists of two values, the first one is the real part and the second one is the imaginary part

d = "hello"
print(d)
print(type(d)) #d is a string, a line of code that contains words or text

e = [1, 2, 3]
print(e)
print(type(e)) #e is a list, it's used to store multiple items in a single variable (their contents can be changed after creation)

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #f is a dictionary, it's used to store data values in key:value pairs

g = (1,2)
print(g)
print(type(g)) #g is a tuple, it's used to store multiple items in a single variable (their contents can't be changed after creation)

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #h is a list, it's used to store multiple items in a single variable (can be changed after creation)

i = True
print(i)
print(type(i)) #i is a boolean, it represents one of two possible truth values: "True" or "False"

j = None
print(j)
print(type(j)) #j is a NoneType, it represents no value and isn't the same thing as 0

k = [True, "blue", 12]
print(k)
print(type(k)) #k is a list, it's used to store multiple items into a single variable (can be changed after creation)

l = str(14)
print(l)
print(type(l)) #l is a string, it's a line of code that contains words or text

m = 1e4
print(m)
print(type(m)) #m is an floater, its a number containing fractions or decimals

#Questions
#1. 9 different data types
#2. Integer, floater, complex, string, list, dictionary, tuple, boolean, NoneType
#3. E, h, and k are all lists. M and b are floaters. L and d are strings.
#4. L's data type is a string. It's not an integer because str() values are used to convert an object into its string representation
#5. The answer to this question is directly below.
my_set = {1, 2, 3, 4, 4}
print(my_set)
print(type(my_set)) #my_set is a set, they're used for unordered collections of unique elements (elements can be added or removed after creation)

print(10>9) #True, 10 is greater than 9
print(10==9) #False, 10 is not equal to 9
print(10<=9) #False, 10 is not greater than or equal to 9
print(bool("abc")) #True, abc are in the correct order
print(bool(123)) #True, 123 are in the correct order
print(bool(["apple", "cherry", "banana"])) #True, any non-empty list is considered "true"
print(bool(True)) #True, the value is true
print(bool(False)) #False, the value is false
print(bool(0)) #False, because of pythons concepts of "true" and "false"
print(bool("")) #False, the string is empty
print(bool(" ")) #True, the string isn't empty
print(bool(())) #False, the tuple is empty
print(bool([])) #False, the list is empty
print(bool({})) #False, dictionary is empty
print(bool(True and False)) #False, one value is "true" and one is "false"
print(bool(True and True)) #True, both values are "true"
print(bool(False and False)) #False, both values are "false"
print(bool(True or False)) #True, based on the first value being "true"
print(bool(True or True)) #True, both values are "true"
print(bool(False or False)) #False, both values are "false"
print(bool(not(False))) #True, the value is not "false" so it is "true"
print(bool(not(True))) #False, the value is not "true" so it is "false"

#Questions
#1. Truth values: Any non-empty object (like strings, lists, dicts), any non-zero number, and the boolean True are True.
#1. False values: Empty objects ("", [], {}, ()), the number 0, None, and the boolean False are False.
#2. The True or False being "true" shocked me the most
#3. The answer below is true because the dictionary contains a non-zero number
print(bool({"Name": "Alysah"}))
#4. The answer below is False because of the empty value "0"
print(bool(0))

print(10+5) #15, + performs addition
print(10-5) #5, - performs subtraction
print(2*4) #8, * performs multiplication
print(6/3) #2, / performs division
print(5%2) #1, % performs the remainder of the division (modulo operator)
print(3**2) #9, ** means to make a value an exponent
print(15//2) #7, // performs integer division
print(5 == 2) #False, 5 doesn't equal 2
print(10 != 10) #False, performs the inequality operator
print(2<5) #True, 2 is less than 5
print(12>5) #True, 12 is greater than 5
print(5 <= 6) #True, 5 is less than 6
print(1>=10) #False, 1 is less than 10

x = 5
x = x + 5
print(x)
x = x - 4
print(x)
x = x * 3
print(x)

#Logical Operations
#1. The and operator only returns true if both sides are true
print(5 > 3 and 10 > 7)
print(5 > 3 and 2 > 7)
#2. The or operator only returns true if one side is true and false if both sides are false
print(5 > 10 or 8 > 2)  
print(5 > 10 or 2 > 7)  
#3. not true = false, not false = true
print(not(5 < 2))  
print(not(10 > 3))  

#More Questions
#1. / performs regular division, while // performs integer division (the operator divides and then rounds down to the nearest whole number)
#2. % performs the modulo operator (returns the remainder of a division), while // performs integer division (the operator divides and then rounds down to the nearest whole number)
#3. The modulo operator, which is %
#4. Assignment operators are used to assign values to variables.

my_string = "hello"
print(my_string) #Prints: hello
print(my_string[0]) #Prints: h (the first character)
print(my_string[1]) #Prints: e (the second character)
print(my_string[2]) #Prints l (the third character)
print(my_string[3]) #Prints: l (the fourth character)
print(my_string[4]) #Prints: o (the fifth character)
print(my_string[-1]) #Prints: o (last character in the string)
print(my_string[1:3]) #Prints: el (characters from index 1 up to, but not including, 3)
print(my_string[0:5:2]) #Prints:hlo (characters from 0 to 4, stepping by 2)
print(len(my_string)) #Prints:5 (the string has 5 characters)
print(my_string + "goodbye") #Prints: hellogoodbye (concatenation)
print(my_string * 7) #Prints: hellohellohellohellohellohellohello (repeats 7 times)

#Questions
#1. Slicing is a way to extract parts (ex: string[start:end:step]) from a string using the syntax. Slicing was used in: my_string[1:3] → "el"and my_string[0:5:2] → "hlo"
#2. name = "Oski" print("Hello, my name is", name). The result is "Hello, my name is Oski". This basically means that The print function separates its arguments with a space by default, so it joins the string and the variable value with a space in between.\
#3. name = "Oski" print(f"Hello, my name is {name}") This result uses an f-string. The {name} inside the string is replaced with the value of the variable
#4. The first version (print("Hello, my name is", name)) automatically separates the text and variable with a space. The second version (print(f"Hello, my name is {name}")) uses an f-string, which lets you insert variables or even expressions directly inside the string.

#Terminal Commands
# 1. cd
# "Change Directory": lets you move into another folder.
# Example: cd Desktop
# 2. ls
# "List": shows the files and folders in the current directory.
# Example: ls
# 3. ls -a
# "List All": shows all files, including hidden ones.
# Example: ls -a
# 4. mkdir
# "Make Directory": creates a new folder.
# Example: mkdir new_folder
# 5. cat
# "Concatenate": shows the contents of a file in the terminal.
# Example: cat notes.txt
# 6. pwd
# "Print Working Directory": shows the full path of where you are.
# Example: pwd
# 7. cd ..
# Goes up one folder (all the way until the parent directory).
# Example: cd ..
# 8. cd .
# Stays in the current folder (it basically does nothing).
# Example: cd .
# 9. cd ~
# Moves to your home directory.
# Example: cd ~
# 10. cp
# "Copy": copies files or folders.
# Example: cp file.txt backup_file.txt
# 11. mv
# "Move": moves or renames files/folders.
# Example 1 (rename): mv old.txt new.txt
# Example 2 (move): mv file.txt ../
# 12. rm
# "Remove": permanently deletes files
# Example: rm file.txt
# To delete a folder/directory and everything inside it: rm -r folder_name
# 13. clear
# Clears the terminal screen.
# Example: clear
# 14. grep
# "Global Regular Expression Print": searches for text patterns inside files.
# Example: grep "hello" notes.txt

#Questions
#1. 
# man
# "Manual": shows the manual/help page for a command.
# Example: man ls
# touch
# Creates a new empty file.
# Example: touch notes.txt
# head
# Shows the first 10 lines of a file.
# Example: head notes.txt
#2. ls lists files and folders, hides hidden files. ls -a lists all files, including hidden files
#3. A hidden file is any file or folder whose name starts with a . they usually store config settings
#4
# ls -l
# "Long format": shows detailed info (permissions, size, owner, date).
# Example output: -rw-r--r-- 1 user group  120 Sep 21  notes.txt
# ls -h
# "Human-readable": when used with -l, it makes file sizes easier to read (KB, MB, GB).
# Example: ls -lh
# grep -i
# "Ignore case": makes searches case-insensitive.
# Example: grep -i "hello" notes.txt ("Hello", "HELLO", "hello" are now considered the same thing)