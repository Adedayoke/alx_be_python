# pattern_drawing.py
# Square Pattern Generator using Nested Loops
# This program draws a square pattern of asterisks using while and for loops

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 0
while row < size:
    # Use for loop to print asterisks side by side
    for col in range(size):
        print("*", end="")
    
    # Move to next row after completing current row
    print()
    
    # Increment row counter
    row += 1