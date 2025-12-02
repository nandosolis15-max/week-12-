# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

Temp = int(input("What is the temperature today?: "))
if Temp <= -10: 
    print("Extreme temperature warning!")
elif Temp >= -9 and Temp <= 39:
    print("COLD")
elif Temp >= 40 and Temp <= 55:
    print("CHILLY ")
elif Temp >= 56 and Temp <= 65:
    print("WARM")
elif Temp >= 66 and Temp <= 109:
    print("HOT")
else:
    print("Extreme temperature warning!")
