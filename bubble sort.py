
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
     
        for j in range(0, n - i - 1):
          
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

user_input = int(input("Enter a number to add to the list: "))
arr.append(user_input)

bubble_sort(arr)

print(arr)
