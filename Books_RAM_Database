books = {}
next_id = 1

while True:
    cmd = input(">> ").strip()
    if cmd == "add":
        # add book
        book = input("Enter book title: ")
        books.update({next_id: {"ID": next_id, "Title": book, "Read": False}})
        print(f"Book '{book}' added with ID {next_id}.")
        next_id = next_id + 1
    elif cmd == "print":
         # print books
         print(books)
    elif cmd == "list":
        # show books
        if not books:
            print("No books available.")
        else:
            print(f"{'ID':<4}{'Title':<30}{'Read'}")
            for book_id, book_data in books.items():
                if book_data["Read"] is True:
                  mark = "✓"
                else:
                  mark = "✗"
                print(f"{book_data['ID']:<4}{book_data['Title']:<30}{mark}")
    elif cmd.startswith("read "):
        # mark book as read
        parts = cmd.split()
        if len(parts) != 2 or not parts[1].isdigit():
            print("Invalid command. Use 'read <ID>'.")
        elif int(parts[1]) not in books:
            print(f"Book with ID {parts[1]} does not exist.")
        elif books[int(parts[1])]["Read"]:
            print(f"Book {books[int(parts[1])]['Title']} is already marked as read.")
        else:
         books[int(parts[1])]["Read"] = True
         print(f"Marking book {books[int(parts[1])]['Title']} as read.")
    elif cmd == "quit":
        print("Exiting the program.")
        break
    elif cmd == "help":
        print("Available commands: add, print, list, read <ID>, quit, help.")
    else:
        print("Unknown command. Available commands: add, print, list, read <ID>, quit.")
