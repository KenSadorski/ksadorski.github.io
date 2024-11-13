# Playing with Lists
# 1. Declaring a list
# 2. Filling a list without a loop
# 3. Printing a list
# 4. Sorting a list

# Initialize a list with colors
markers = ["yellow", "blue", "red", "pink", "black", "green", "orange"]

# Optional: Uncomment below to allow the user to add new marker colors to the list
# print("Add new marker colors to the list:")
# for index in range(len(markers)):
#     markers[index] = input(f"Enter a marker color for position {index + 1}: ")

# Printing the original list
print("Here is our list of markers as originally entered:")
print("*************************************************")
for color in markers:
    print(color)
print()

input("Press Enter to continue...")

# Using reverse method to reverse the list
markers.reverse()
print("Here is our list of markers AFTER using REVERSE:")
print("************************************************")
for color in markers:
    print(color)
print()

input("Press Enter to continue...")

# Sorting in descending order
markers.sort(reverse=True)
print("Here is our list of markers AFTER using SORT(reverse=True):")
print("************************************************************")
for color in markers:
    print(color)
print()

input("Press Enter to continue...")

# Sorting in ascending order
markers.sort()
print("Here is our list of markers AFTER using SORT:")
print("********************************************")
for color in markers:
    print(color)
print()
