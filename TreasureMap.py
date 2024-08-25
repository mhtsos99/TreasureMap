# Define the initial map layout with three lines, each containing three empty squares
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

# Print a message indicating the start of the treasure hiding process
print("Hiding your treasure! X marks the spot.")

# Prompt the user to input the position where they want to put the treasure
# The position is expected in the format of a letter followed by a number (e.g., "a1") 
position = input("Where do you want to put the treasure (e.g. a1)? ") 

# Extract the letter part of the position and convert it to lowercase
letter = position[0].lower()

# Define the list of letters corresponding to columns
abc = ["a", "b", "c"]

# Find the index of the letter in the abc list to determine the column
letter_index = abc.index(letter)

# Extract the number part of the position and convert it to an integer
# Subtract 1 to get the correct index (as list indices start from 0)
number_index = int(position[1]) - 1

# Place the treasure marker ("X") at the specified position on the map
map[number_index][letter_index] = "X"

# Print the updated map showing the position of the treasure
print(f"{line1}\n{line2}\n{line3}")