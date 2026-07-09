#1
#runtime error
x = 10
y = 0
if y != 0:
    print(10 / y)
else:
    print("Cannot divide by zero")


#2
#logical error
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])

#3
#syntax error
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))

#4
#runtime error
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))

#5
#runtime error
for i in range(5):
    print(i)

#6
#logical error
def greet(name):
    return "Hello, " + name
print(greet("Alice"))

#7
#logical error
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)

#8
#runtime error
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

#9
#logical error
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")

#10
#runtime error
def divide_numbers(x, y):
    result = x / y
    return result
num1 = 10
num2 = 0
if num2 != 0:
    print(divide_numbers(num1, num2))
else:
    print("Cannot divide by zero")
