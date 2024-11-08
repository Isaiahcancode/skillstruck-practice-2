# Initial list
arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

# Get user input and add it to the list
num = int(input("Enter a number to add to the list: "))
arr.append(num)

# Insertion Sort
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    # Move elements of arr[0..i-1] that are greater than key to one position ahead
    # of their current position
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

# Print the sorted list
print(arr)
