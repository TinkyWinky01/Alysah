#2. Create a Script
# This function prints a goodbye message.
def say_goodbye(name):
    print("Goodbye,", name)
#3. Print Functions

#3.1 Say Goodbye
# Call the function

#3.2 Area of a Circle
# This function prints the area of a circle given its radius.
def print_circle_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    print("The area of the circle is:", area)

#4 Return Functions

#4.1 Subtract, Multiply, and Divide
# Returns the result of subtracting b from a.
def subtract(a, b):
    return a - b
# Returns the result of multiplying a and b.
def multiply(a, b):
    return a * b
# Returns the result of dividing a by b.
def divide(a, b):
    return a / b

#5 Conditionals

#5.1 What should I Wear?
#This function will return the lowest and highest temperatures from a list
def get_temperature_range(readings):
    min_temp = min(readings) # Finds lowest temperature
    max_temp = max(readings) # Finds highest temperature
    return(min_temp, max_temp) # Should return a tuple with both values
readings = [5,10,15,20,25,30,35]
temperature_range = get_temperature_range(readings)

#5.2 Check if its the Weekend
# Returns True if the day is Saturday (6) or Sunday (7), otherwise False.
def is_weekend(day_number):
    return day_number == 6 or day_number == 7

#5.3 Fuel Efficiency Calculator
# Calculates and returns fuel efficiency in miles per gallon.
def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used

#5.4 Secret Code
# Encrypts a number by moving its last digit to the front.
def encrypt_number(n):
    last_digit = n % 10
    remaining = n // 10
    encrypted = int(str(last_digit) + str(remaining))
    return encrypted

#6 Loops

#6.1 Oski Stole Your Power
# Computes x raised to the power of y using a for loop.
def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

#6.2 Min and Max with Loops!
# Returns the minimum value from a list using a loop.
def find_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

# Returns the maximum value from a list using a loop.
def find_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
readings = [15, 14, 17, 20, 23, 28, 20]

#6.2.1 For Loops
# Finds the minimum value using a for loop.
def find_min_for(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

# Finds the maximum value using a for loop.
def find_max_for(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

#6.2.2 While Loops
# Finds the minimum value using a while loop.
def find_min_while(numbers):
    index = 0
    min_value = numbers[0]
    while index < len(numbers):
        if numbers[index] < min_value:
            min_value = numbers[index]
        index += 1
    return min_value

# Finds the maximum value using a while loop.
def find_max_while(numbers):
    index = 0
    max_value = numbers[0]
    while index < len(numbers):
        if numbers[index] > max_value:
            max_value = numbers[index]
        index += 1
    return max_value

#6.3 Calculate the Sum
# Returns the sum of all digits in an integer.
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10      # Add the last digit
        n = n // 10          # Remove the last digit
    return total

#7 Running Your Script
#7.1 In Your VS Code Terminal
# Example usage of the power function
x = 5
y = 7
result = power(x, y)  # 5 raised to the power of 7
print(f"The result of Oski Stole Your Power (5.1) with x = {x} and y = {y} is {result}.")

#7.2 Importing Functions
import homework3 as h3
h3.say_goodbye("Alysah")
h3.print_circle_area(5)
print(h3.subtract(10, 4))
print(h3.multiply(3, 7))
print(h3.divide(20, 5))
print(h3.get_temperature_range([5,10,15,20,25,30,35]))
print(h3.is_weekend(6))
print(h3.fuel_efficiency(300, 10))
print(h3.encrypt_number(12345))
print(h3.power(2, 3))
print(h3.find_min_for([5, 2, 9]))
print(h3.find_max_for([5, 2, 9]))
print(h3.find_min_while([5, 2, 9]))
print(h3.find_max_while([5, 2, 9]))
print(h3.sum_of_digits(2468))