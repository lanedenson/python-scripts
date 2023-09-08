'''
Identify missing and duplicate numbers
Provide a list of numbers in a plain text file, one
number per line, titled numbers.txt 

The script will identify any missing or duplicate
numbers.

Not particularly fault-tolerant or optimized.
'''

# Read the numbers from the file
with open("numbers.txt", "r") as file:
    numberslist = [int(line.strip()) for line in file.readlines()]

# Format and print the numbers
formatted_numbers = numberslist

def find_duplicates_and_missing_numbers(numbers):
    duplicates = []
    missing = []

    # Create a dictionary to keep track of counts
    count_dict = {}

    # Find duplicates and count occurrences
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
            duplicates.append(num)
        else:
            count_dict[num] = 1

    # Find missing numbers
    max_num = max(numbers)
    min_num = min(numbers)
    for num in range(min_num, max_num + 1):
        if num not in count_dict:
            missing.append(num)

    return duplicates, missing

# Example list of numbers
numbers = formatted_numbers

duplicates, missing = find_duplicates_and_missing_numbers(numbers)

print("Duplicates:", duplicates)
print("Missing:", missing)