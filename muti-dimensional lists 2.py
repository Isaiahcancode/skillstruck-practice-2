rows = input("input a list of fruit").split()
cols = ['apple', 'grape', 'peach', 'cinnamon', 'vanilla']
list = []
for i in rows:
    col = []
    for j in cols:
        col.append(i + " " + j)
    list.append(col )
print(list)