x = int(input("What is the first number? "))
y = int(input("What is the second number? "))
z = int(input("What is the third number? "))


my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]

rows = 4
cols = 3


largest_number = my_list[0][0]


for i in range(rows):
    for j in range(cols):
        if my_list[i][j] > largest_number:
            largest_number = my_list[i][j]

print(largest_number)
