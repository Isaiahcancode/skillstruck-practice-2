
def calculate_total_pages(books):
   
    if len(books) == 2:
        print(books[0] + books[1])
        return
    
    # Find the midpoint of the list
    mid = len(books) // 2
    
   
    calculate_total_pages(books[:mid])
    calculate_total_pages(books[mid:])


books = [int(n) for n in input("Input a list of numbers: ").split()]


if len(books) % 2 == 0:
    calculate_total_pages(books)
else:
    print("Please enter an even number of page numbers.")
