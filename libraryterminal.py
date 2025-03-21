book_list = []

menu = """
1) Add Book
2) Remove Book
3) View Books
4) Press E to Exit
"""

def add_book(booklist, book):
    booklist.append(book)
    print(f"Book '{book}' added successfully.")

def remove_book(booklist, book):
    if book in booklist:
        booklist.remove(book)
        print(f"Book '{book}' removed successfully.")
    else:
        print(f"Book '{book}' not found in the list.")

def display_list(booklist):
    if booklist:
        print("Added Books ->", ", ".join(booklist))
    else:
        print("No books added yet.")

def exit_program():
    print("Thank you for visiting the book library system.")
    exit()  # Proper exit function

while True:
    print(menu)
    choice = input("Enter your choice: ").strip().lower()

    if choice == '1':
        add_book(book_list, input("Enter the name of the book to add: "))
    elif choice == '2':
        remove_book(book_list, input("Enter the name of the book to remove: "))
    elif choice == '3':
        display_list(book_list)
    elif choice == 'e':
        exit_program()
    else:
        print("Invalid option. Please try again.")
        input("Press Enter to return to the main menu.")
