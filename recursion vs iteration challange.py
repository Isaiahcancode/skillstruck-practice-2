# Recursive function to sum the elements of a list
def sum_list(nums):
    # Base case: if the list has only one element, return that element
    if len(nums) == 1:
        return nums[0]
    # Recursive case: add the first element to the sum of the rest of the list
    else:
        return nums[0] + sum_list(nums[1:])

# Input the list of numbers
list_of_nums = [int(n) for n in input("Enter numbers separated by spaces: ").split()]

# Calculate and print the sum of all numbers
print(sum_list(list_of_nums))
