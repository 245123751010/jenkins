# factorial_args.py
import sys

# Check if a number is provided
if len(sys.argv) != 2:
    print("Usage: python factorial_args.py <number>")
    sys.exit(1)

num = int(sys.argv[1])

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
