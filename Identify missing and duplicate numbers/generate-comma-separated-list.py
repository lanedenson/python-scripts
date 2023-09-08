# Read the numbers from the file
with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

# Format and print the numbers
formatted_numbers = ", ".join(map(str, numbers))
print(formatted_numbers)