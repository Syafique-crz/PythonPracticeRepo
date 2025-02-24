# 4️⃣ Functions & Modules
import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793
print(math.exp(6))    # Output: 403.4287934927351
print(math.log(100))  # Output: 4.605170185988092 
print(math.sin(math.pi/2))  # Output: 1.0

def greet(name):
    return f"Hello, {name} in Wonderland!"

def factorial(n):   # Recursive function
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):   # Generate Fibonacci sequence
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:   # loop length is less than n
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) # Add last two numbers
    return fib_sequence

def is_prime(num):   # Check if a number is prime
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(greet("Alice"))
print(f"Factorial of 5: {factorial(5)}")
print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
print(f"Is 29 a prime number? {is_prime(29)}")