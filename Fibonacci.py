num = int(input("Enter how many numbers you want in the sequence: "))

# Start with the first two numbers of the sequence
a = 0
b = 1

# Store the sequence in a list
sequence = [a, b]

# Generate the Fibonacci sequence up to num
for i in range(2, num):
    next_number = sequence[-1] + sequence[-2]  # Calculate the next Fibonacci number
    sequence.append(next_number)

# Print the Fibonacci sequence
print("The Fibonacci sequence up to", num, "numbers:", sequence)
