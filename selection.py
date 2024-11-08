# Initial list
arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

# Get user input and add it to the list
user_input = int(input("Enter a number to add to the list: "))
arr.append(user_input)


def selection_sort(sort_list):
    
    for i in range(len(sort_list)):
        
        min_index = i
        for j in range(i + 1, len(sort_list)):
            if sort_list[j] < sort_list[min_index]:
                min_index = j
        
        sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]

# Sort the list
selection_sort(arr)

# Print the sorted list
print(arr)
