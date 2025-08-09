# --- functions definitions ---

def add_book(books):
    # add book
    book = input("Enter book title: ")
    next_id = len(books) + 1
    books.update({next_id: {"ID": next_id, "Title": book, "Read": False}})
    print(f"Book '{book}' added with ID {next_id}.")

def list_books(books):
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

def mark_as_read(books, cmd):
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

def quit_program():
    print("Exiting the program.")
    exit()

def help_command():
    print("Available commands: add, list, read <ID>, quit, help.")

def default_command():
    print("Unknown command. Available commands: add, list, read <ID>, quit.")

# --- main program ---
# Initialize the books dictionary and next_id
books = {}
help_command()

while True:
    # Get user command
    cmd = input(">> ").strip()

    # Process the command
    match cmd:
        case "add":
            # add book
            add_book(books)
        case "list":
            # list books
            list_books(books)
        case s if cmd.startswith("read"):
            mark_as_read(books, cmd)
        case "quit":
            quit_program()
        case "help":
            help_command()
        case _:
            default_command()
