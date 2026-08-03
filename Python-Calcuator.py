# 1. Simple Calculator

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Choose Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter Choice (1-4): ")

if choice == "1":
    print("Result =", num1 + num2)

elif choice == "2":
    print("Result =", num1 - num2)

elif choice == "3":
    print("Result =", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid Choice")


# 2. Number Guessing Game
import random

secret = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == secret:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong Guess!")
    print("Correct Number is:", secret)


# 3. Student Grade Calculator
name = input("Enter Student Name: ")

sub1 = float(input("Enter English Marks: "))
sub2 = float(input("Enter Math Marks: "))
sub3 = float(input("Enter Science Marks: "))

total = sub1 + sub2 + sub3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)


# 4. Expense Tracker
expenses = []

n = int(input("How many expenses do you want to enter? "))

for i in range(n):
    amount = float(input(f"Enter Expense {i+1}: "))
    expenses.append(amount)

print("\nExpenses:", expenses)
print("Total Expense =", sum(expenses))


# 5. Password Generator
import random
import string

length = int(input("Enter Password Length: "))

characters = string.ascii_letters + string.digits + "@#$%&"

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)