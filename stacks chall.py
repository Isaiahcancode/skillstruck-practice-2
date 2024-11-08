answer = ["apples", "steak", "potatoes", "carrots"]
new = input("enter a food with the letters")
news = new.count("s")
if news > 0:
    awnser = answer.append(new)
    print(answer)
else:
    print("The input doesn't have the letter s")
