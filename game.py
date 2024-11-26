def borrowed_books():
    
    num_records = int(input("Enter the number of books: "))
    
    books = []
    
    
    for _ in range(num_records):
        
        record = input("Enter the title and number of days like ('Title - nomber'): ")
        title, days = record.split('-')  
        books.append((title, int(days)))  
    
    most_days = max(books, key=lambda x: x[1])

    least_days = min(books, key=lambda x: x[1])

    total_days = sum(book[1] for book in books)  
    average_days = total_days / len(books) if books else 0 


    unique_titles = set(title for title, _ in books)

    sorted_books = sorted(books, key=lambda x: x[1], reverse=True)

    return {
        'most_days': most_days,
        'least_days': least_days,
        'average_days': average_days,
        'unique_titles': unique_titles,
        'sorted_books': sorted_books
    }

result = borrowed_books()

print("Most borrowed days of book:", result['most_days'])
print("Least borrowed days of book:", result['least_days'])
print("Average days :", result['average_days'])
print("Unique titles:", result['unique_titles'])
print("Books sorted by borrowed days:")
for book in result['sorted_books']:
    print(book)
