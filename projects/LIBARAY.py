library = []

def menu():
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        book = input("Enter book name: ")
        library.append(book)
        print(book, "added successfully!")

    elif choice == '2':
        if len(library) == 0:
            print("Library is empty!")
        else:
            print("Available Books:")
            for b in library:
                print("-", b)

    elif choice == '3':
        book = input("Enter book to issue: ")
        if book in library:
            library.remove(book)
            print(book, "issued successfully!")
        else:
            print("Book not found!")

    elif choice == '4':
        book = input("Enter book to return: ")
        library.append(book)
        print(book, "returned successfully!")

    elif choice == '5':
        print("Program Ended")
        break

    else:
        print("Invalid choice!")


