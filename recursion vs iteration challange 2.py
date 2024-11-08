# Recursive function to find the Fibonacci number at a specific position
def fibonacci_number(position):
    # Base cases: return 0 for the first position, and 1 for the second
    if position == 0:
        return 0
    elif position == 1:
        return 1
    # Recursive case: sum of the previous two positions
    else:
        return fibonacci_number(position - 1) + fibonacci_number(position - 2)

# Input the number of Fibonacci numbers to generate
num = int(input("Enter the number of Fibonacci numbers to generate: "))

# Create a list and fill it using the recursive function in a loop
fibonacci_sequence = [fibonacci_number(i) for i in range(num)]

# Print the completed Fibonacci sequence
print(fibonacci_sequence)
