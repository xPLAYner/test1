# --- functions definitions ---

def add_book(books, operation_argument):
    # add book
    #book = input("Enter book title: ")
    book = operation_argument
    if not book:
        print("Book title cannot be empty.")
        return
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

def mark_as_read(books, operation_argument):
    # mark book as read
    parts = operation_argument.split()
    if len(parts) != 1 or not operation_argument.isdigit():
        print("Invalid command. Use 'read <ID>'.")
    elif int(operation_argument) not in books:
        print(f"Book with ID {operation_argument} does not exist.")
    elif books[int(operation_argument)]["Read"]:
        print(f"Book {books[int(operation_argument)]['Title']} is already marked as read.")
    else:
        books[int(operation_argument)]["Read"] = True
        print(f"Marking book {books[int(operation_argument)]['Title']} as read.")

def quit_program():
    print("Exiting the program.")
    exit()

def help_command():
    print("Available commands: add <Title>, list, read <ID>, quit, help.")

def default_command():
    print("Unknown command. Available commands: add <Title>, list, read <ID>, quit.")

# --- main program ---
# Initialize the books dictionary and next_id
books = {}
help_command()

while True:
    # Get user command
    cmd = input(">> ").strip()
    parts = cmd.split(maxsplit=1)

    operation = parts[0]
    operation_argument = parts[1] if len(parts) > 1 else None

    # Check if the command is valid
    if operation not in ["add", "list", "read", "quit", "help"]:
        default_command()
        continue

    # Process the command
    match operation:
        case "add":
            # add book
            add_book(books, operation_argument)
        case "list":
            # list books
            list_books(books)
        case "read":
            mark_as_read(books, operation_argument)
        case "quit":
            quit_program()
        case "help":
            help_command()
        case _:
            default_command()
