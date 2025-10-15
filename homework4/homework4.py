#3.1
favorite_foods = ["pizza", "sushi", "tacos", "pasta", "cake"]
print("second food:", favorite_foods[1])
print("last food:", favorite_foods[-1])
favorite_foods.append("cherry")
print("after append:", favorite_foods)
favorite_foods.insert(0,"apple")  #I encountered this error: "favorite_foods.insert("apple")~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^ TypeError: insert expected 2 arguments, got 1" I originally wrote favorite_foods.insert("apple"). I forgot to also insert 0.
print("after inserting apple", favorite_foods)
del favorite_foods[3]
print("after removing 3rd item:", favorite_foods)
print("length of list:", len(favorite_foods))
print("favorite_foods in uppercase:")
for favorite_food in favorite_foods:
    print(favorite_food.upper()) #I encountered this error: "line 13, in <module> print(favorite_foods.upper())^^^^^^^^^^^^^^^^^^^^ AttributeError: 'list' object has no attribute 'upper'" I originally wrote favorite_foods.upper. I forgot that I redefined it as "favorite_food".
new_list = [favorite_foods[0], favorite_foods[-1]]
print("first and last favorite_foods:", new_list)
if "potato" in favorite_foods:
    print("A potato!")
else:
    print("No potato!") #I encountered this error: "line 18 else print("No potato!") ^^^^^ SyntaxError: expected ':'" I originally wrote else print("No potato!"). I forgot to put ":" after else.


#3.2
numbers = list(range(21))
def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print("numbers:", numbers)
print("step 1 (first 15):", step1)
print("step 2 (every 5th):", step2)
print("step3 (reversed every 3rd):", step3)

#3.3
numbers = [[1,2,3], [4,5,6], [7,8,9]]
print("third row:", numbers[2])

print("second item in the second row:", numbers[1][1])

numbers.append([10, 11, 12])
print("after appending new row:", numbers)

def sum_nested(lst):
    total = 0
    for row in lst:
        for num in row:
            total += num
    return total

print("total sum:", sum_nested(numbers))

#3.4
def create_5x5():
    grid = []
    count = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        grid.append(row)
    return grid

matrix = create_5x5()
print(matrix)

def replacement(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix

updated_matrix = replacement(matrix)
print(updated_matrix)

def sum_question(matrix):
    total = 0
    for row in matrix:
        for item in row:
            if item != "?":
                total += item
    return total

sum_result = sum_question(updated_matrix)
print("sum of all elements without the '?':", sum_result)

#4.1
ages = {"Katie": 30, "Mariam": 42, "Safia": 25, "Mira": 48}

print(ages["Katie"])

ages["Mira"] = 100

ages["Milana"] = 52

del ages["Mariam"]

print("new age list:")
for name, age in ages.items():
    print(name, "is", age, "years old.")

#5.2
def sum_question(matrix):
    total = 0
    for row in matrix:
        for item in row:
            if item != "?":
                total += item
    return total
sum_result = sum_question(updated_matrix)
print("sum of all elements without the '?':", sum_result)