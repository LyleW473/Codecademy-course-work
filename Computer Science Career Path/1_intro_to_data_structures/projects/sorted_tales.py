import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

for book in bookshelf:
  book["author_lower"] = book["author"].lower()
  book["title_lower"] = book["title"].lower()

print(bookshelf)
print(ord("a"), ord(" "), ord("A"))

def by_title_ascending(book_a, book_b):
  return book_a["title_lower"] > book_b["title_lower"]

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

for book in sort_1:
  print(book["title"])

  def by_author_ascending(book_a, book_b):
    return book_a["author_lower"] > book_b["author_lower"]

bookshelf_v1 = bookshelf.copy()
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
  print(book["title"])

bookshelf_v2 = bookshelf.copy()
for book in bookshelf_v2:
  print("Pre-quicksort", book["author"])
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
for book in bookshelf_v2:
  print("Post-quicksort", book["author"])

def by_total_length(book_a, book_b):
  return (len(book_a["title_lower"]) + len(book_a["author_lower"])) > (len(book_b["title_lower"]) + len(book_b["author_lower"]))

long_bookshelf = utils.load_books("books_large.csv")
for book in long_bookshelf:
  book["author_lower"] = book["author"].lower()
  book["title_lower"] = book["title"].lower()

sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)
print("Started QS")
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
print("Finished QS")
