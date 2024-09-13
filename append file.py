file = open("letter.txt", "a")
file.write("Quote was said by Gandhi")
file.close()

file = open("letter.txt", "r")
print(file.read())