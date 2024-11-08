# Recursive function to calculate the total flowers each bee needs to visit
def pollinate(flowers):
    # Base case: if there's only one tree in the list, calculate and print the total flowers visited
    if len(flowers) == 1:
        print(flowers[0] * 3)
        return
    
    # Recursively call the function on the first tree
    print(flowers[0] * 3)
    pollinate(flowers[1:])  # Call the function on the rest of the list

# Input the list of blossoms on each tree
flowers = [int(n) for n in input("How many blossoms are on each tree? ").split()]

# Start the pollination process
pollinate(flowers)
