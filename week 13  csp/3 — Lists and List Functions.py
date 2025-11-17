# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Collections are used to store multiple items in a single variable
# lists are ordered collections of items
# lists are mutable, meaning you can change their content
# lists are created using square brackets []

lists_of_fruits =(["apples", "banana",  "cheery", "date"])
["apples", "banana",  "cheery", "date"]
print(lists_of_fruits) 
print(type(lists_of_fruits))

print(lists_of_fruits[0]) 
print(lists_of_fruits[1])
print(lists_of_fruits[-1])
print(lists_of_fruits[1:3])
lists_of_fruits.reverse()
print(lists_of_fruits)
print(lists_of_fruits[::-1])
lists_of_fruits.append("elderberry")
print(lists_of_fruits)

lists_of_fruits.extend(["mango", "pear", "strawberry"])
print(lists_of_fruits)

lists_of_fruits.remove("banana")
print(lists_of_fruits)
lists_of_fruits.insert(3, "banana")
lists_of_fruits.sort()
print(lists_of_fruits)
lists_of_items = list(range(1, 1001))
print(lists_of_items)
print(len(lists_of_items))
lists_of_items.extend(range(1001, 2001))
print(len(lists_of_items))
 
#why use a list
#instead of creating seperate variables 
# for each item, we can store them in a list
# this wakes our job easier
# this is

set1= {1,2, 3 , 4, 4, 5}

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.