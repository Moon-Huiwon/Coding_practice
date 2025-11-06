N = int(input())
books_dict = {}
for _ in range(N):
    book = input()
    books_dict[book] = books_dict.get(book, 0) - 1

sorted_books_dict = sorted(books_dict.items(), key=lambda x: (x[1], x[0]))

print(sorted_books_dict[0][0])