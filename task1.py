# 1. Sum of two numbers

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
sum = num1 + num2

# Print the result
print("The sum of", num1, "and", num2, "is:", sum)

# *******************************************************************************
# 2. Odd or Even number

# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
# *******************************************************************************
3. Factorial of a number

# Take input from the user
num = int(input("Enter a number: "))

# Initialize factorial
factorial = 1

# Calculate factorial iteratively
for i in range(1, num + 1):
    factorial *= i

# Print the result
print("Factorial of", num, "is:", factorial)
# *******************************************************************************

4. Fibonacci series up to n terms
# Take input from the user
n = int(input("Enter how many Fibonacci numbers to generate: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
# *******************************************************************************

5. String reversal
# Take input from the user
user_string = input("Enter a string: ")

# Reverse the string
reversed_string = user_string[::-1]

# Print the result
print("Reversed string:", reversed_string)
# *******************************************************************************

6. Palindrome check
# Take input from the user
word = input("Enter a word: ")

# Convert to lowercase to ignore case
word_lower = word.lower()

# Check if the word is the same forwards and backwards
if word_lower == word_lower[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is NOT a palindrome")
# *******************************************************************************

7. Leap year check
# Take input from the user
year = int(input("Enter a year: "))

# Check for leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is NOT a leap year")
# *******************************************************************************

8. Armstrong number check
# Take input from the user
num = int(input("Enter a number: "))

# Store the original number
original_num = num

# Find the number of digits
num_digits = len(str(num))

# Initialize sum
sum = 0

# Calculate the sum of digits raised to the power of num_digits
while num > 0:
    digit = num % 10
    sum += digit ** num_digits
    num //= 10

# Check if the sum equals the original number
if sum == original_num:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is NOT an Armstrong number")



