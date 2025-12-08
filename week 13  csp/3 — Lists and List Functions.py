# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

#my_list = ['apple', 'banana', 'cherry']
#print(my_list[0])         # apple
#print(my_list[1:])        # ['banana', 'cherry']

#my_list.append('grape')
#print(my_list)

#my_list.pop(1)
#print(my_list)

#numbers = [3, 1, 4, 2]
#numbers.sort()
#print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.

#collections are used to store multiple items in a single variable
# list are ordered collections of items
# lists are mutiple, meaning you can chnage their content
# lists are created using square brackets
list_of_fruits = ["apple", "bannana", "cherry", "date"]
print(list_of_fruits) #['apple', 'banana', 'cherry','date']
print(type(list_of_fruits))
print(list_of_fruits[0])
print(list_of_fruits[1])
print(list_of_fruits[-1])
print(list_of_fruits[1:3])
list_of_fruits.reverse()
print(list_of_fruits)
print(list_of_fruits[::-1])
list_of_fruits.append("elderberry")
print(list_of_fruits)
list_of_fruits.extend(["margo", "dragonfruit", "butterfly"])
popped_item = list_of_fruits.pop()
print(popped_item)
print(list_of_fruits)
list_of_fruits.insert(1, "blueberry")
print(list_of_fruits)
list_of_fruits.removal("bannana")
print(list_of_fruits)
list_of_fruits.insert(3, "bannana")
list_of_fruits.sort()
print(list_of_fruits)
list_of_items = list(range(1, 101))
print(list_of_items)
list_of_items = list(range(1, 1001))
print(list_of_items)
list_of_items.extend(range(1001,2001))
print(list_of_items)

#why use a list
#this makes our job easier
#this makes manageing our code easier
#when we need to manage mutilple items
#performance task answer

#sets and tuples
#sets and tuples are also part of the collection
#family in python
#sets examples:
set1 = {1,2,3,4,5}
set2 = {"apple","bannana","cherry"}
print(set1)
print(set2)
print(type(set1))
set_with_duplicates = {1,1,2,2,3,3,4,4,5}
print(set_with_duplicates)
print(3 in set1)
print(6 in set1)
tuple1 = (1,2,3,4,5)
tuple2 = ("apple", "banana", "cherry")
print(tuple1)
print(tuple2)
print(type(tuple1))
socail_secruity_number = (12344, 444445, 5676789)
# # Create a list of 3 lists (matrix), and access the middle element.
