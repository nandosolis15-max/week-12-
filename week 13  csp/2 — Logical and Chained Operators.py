# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True


# Practice Problems:
#score ?grade checker
#if the score is between 90 and 100 print A
#if the score is between 80 and 90 print B
#if the score is between 70 and 80 print C
#if the score is between 60 and 70 print D
grade = int(input("enter your score:"))
if grade >= 100:
    print("A")
grade = int(input("enter your score:"))
if grade >= 88:
    print("B")
    grade = int(input("enter your score:"))
if grade >= 76:
    print("C")
    grade = int(input("enter your score:"))
if grade >= 67:
    print("D")
# Write an expression that checks if a number is between 50 and 100 (inclusive).

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.

# Use chained comparison to check if 3 < 4 < 5.

# Challenge: Create a password rule using logical operators:
