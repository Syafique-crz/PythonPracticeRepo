# Python Data Structures

# 1️⃣ Lists (Mutable, Ordered)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adds orange
fruits.remove("banana")  # Removes banana
fruits[1] = "blueberry"  # Updates the second element (cherry)
print(len(fruits))  # Output: 3
print(fruits[1])  # Output: blueberry
print(fruits)  # Output: ['apple', 'blueberry', 'orange']

# Nested List
nested_list = [["apple", "banana"], ["cherry", "orange"]]
nested_list[0].append("grape")       # Adds grape to the first list
print(nested_list)          # Output: [['apple', 'banana', 'grape'], ['cherry', 'orange']]

# 2️⃣ Tuples (Immutable, Ordered)
coordinates = (10, 20, 30)
coordinates = coordinates + (40,)  # Adds 40
coordinates = coordinates[:2] + (15,) + coordinates[2:]  # Inserts 15 at index 2
print(coordinates[0])           # Output: 10
print(coordinates)           # Output: (10, 15, 20, 30, 40)

# Nested Tuple
nested_tuple = ((1, 2),         # 00 01
                (3, 4),         # 10 11
                (5, 6))         # 20 21
print(nested_tuple[2][0])           # Output: 5
print(nested_tuple[0][1])           # Output: 2

# 3️⃣ Sets (Unique, Unordered)
unique_numbers = {1, 2, 3, 7}
unique_numbers.add(4)
unique_numbers.remove(3)   # remove element 3
unique_numbers.update({2, 3, 5}) # Adds elements that are not in the set
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 7}

# Set Operations
another_set = {3, 4, 5, 8, 9}
union = unique_numbers | another_set       # Union of two sets
intersection = unique_numbers & another_set         # same elements in both sets
print(intersection)                 # Output: {3, 4}
print(union)                    # Output: {1, 2, 3, 4, 5, 7, 8, 9}

# 4️⃣ Dictionaries (Key-Value Pairs)
student = {"name": "Alice", "age": 20}
student["email"] = "alice@email.com"         # Add new key-value pair
student["height"] = 5.6
del student["height"]                   # Delete key-value pair
student["age"] = 21                 # Update value
student.pop("email")                  # Remove key-value pair
print(student)                  # Output: {'name': 'Alice', 'age': 21, 'email': 'alice@email.com'}
print(f"{student['name']} is {student['age']} years old")              # Output: Alice is 21 years old

# Nested Dictionary
students = {
    "Alice": {"age": 21, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}
students["Charlie"] = {"age": 23, "grade": "C"}     # Add new student
print(students["Bob"]["grade"])  # Output: B

# Dictionary Operations
for name, info in students.items():
    print(f"{name} is {info['age']} years old and got grade {info['grade']}")
# Output:
# Alice is 21 years old and got grade A
# Bob is 22 years old and got grade B
# Charlie is 23 years old and got grade C