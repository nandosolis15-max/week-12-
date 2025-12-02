# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

list1 = [1, 2, 3]
print (list1[-1])
list2 = [4, 5, 6]
print(list2[0])
nested_list = [list1, list2]
print(nested_list[0])
print(nested_list[1])
print(nested_list [1][2])



fruits = ["apples", "oranges", "banana", "coconut"]
vegetables = ["celery", "carrot"," potatoes"]
meats = ["chicken", "fish", "turkey"]
groceries = [fruits, vegetables, meats]

print(groceries[1][1])
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# for i in range (1,101):
#     for j in range(1,101):
#         if i > 0 and j > 0:
#             for k in range(1,101):
#                 print("the number is ", i)

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num, end=" ") 
    print()  

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# # Examples:

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(matrix[0])    # 6
print(matrix[2][1])

sum_list = [row[-1] for row in matrix]
print(sum_list)


# # List comprehension
# first_col = [row[0] for row in matrix]
# print(first_col)       # [1, 4, 7]



# # Practice Problems:

# # Build a matrix variable containing 3 lists of 3 numbers each.

# # Print the first list.

# # Print the second item from the third list.

# # Use a list comprehension to extract the last item from each sub-list.

# # Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.


squares = [x**2 for x in range (1, 11)]
print(squares)