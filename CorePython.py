# Python Basics, Control Flow, and Functions

# 1️⃣ Variables & Data Types
x = 10        # Integer
y = 3.14      # Float
name = "John" # String
is_python = True  # Boolean
complex_num = 2 + 3j  # Complex number
list_example = [1, 2, 3, 4, 5]  # List
tuple_example = (1, 2, 3)  # Tuple
set_example = {1, 2, 3, 4, 5}  # Set
dict_example = {"name": "John", "age": 30}  # Dictionary

print(f"x: {x}, y: {y}, name: {name}, is_python: {is_python}\n")
print(f"complex_num: {complex_num}, list_example: {list_example}")
print(f"tuple_example: {tuple_example}, set_example: {set_example}")
print(f"dict_example: {dict_example}\n")

# 2️⃣ Operators
# Arithmetic Operators
sum_result = x + y     # 13.14
diff_result = x - y     # 6.86
prod_result = x * y     # 31.4
div_result = x / y      # 3.1847133757961785
floor_div_result = x // y     # 3.0
mod_result = x % y         # 3.14
exp_result = x ** 2        # 100

# Comparison Operators
is_equal = (x == 10)         # True
is_not_equal = (x != 10)     # False
is_greater = (x > y)           # True
is_less_or_equal = (x <= y)    # False

# Logical Operators
logical_and = (x > 5 and y < 4)    # False
logical_or = (x > 5 or y < 4)      # True
logical_not = not (x > 5)          # False

# Bitwise Operators
bitwise_and = x & 1             # 0
bitwise_or = x | 1              # 11
bitwise_xor = x ^ 1             # 11
bitwise_not = ~x                # -11
bitwise_left_shift = x << 2     # 40
bitwise_right_shift = x >> 2    # 2


# 3️⃣ Control Flow
# if elif else statements
age = 25
if age < 13:
    print("You're a child!")
elif 13 <= age < 18:
    print("You're a teenager!")   
elif 18 <= age < 65:  
    print("You're an adult!")  # output
else:
    print("You're a senior!")

# Nested if statements
num = 15
if num > 10:
    if num % 2 == 0:
        print(f"{num} is greater than 10 and even")
    else:
        print(f"{num} is greater than 10 and odd")
else:
    print(f"{num} is 10 or less")

# For loop with else
for i in range(1, 6):
    print(i)  # Prints 1 to 5
else:
    print("Loop completed")

# While loop with break and continue
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue  # Skip even numbers
    if x > 7:
        break  # Exit loop if x is greater than 7
    print(x)  # Prints odd numbers less than 8



