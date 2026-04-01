def create_note():
    file = open("notes.txt", "a")  # append mode
    # Modified input handling for environments that might not support interactive input
    try:
        note = input("Enter your note: ")
    except EOFError:
        note = "[Empty Note due to EOF]"
        
    file.write(note + "\n")
    file.close()
    print("✅ Note saved successfully!\n")


def read_notes():
    try:
        file = open("notes.txt", "r")
        content = file.read()
        file.close()

        if content == "":
            print("⚠️ No notes found.\n")
        else:
            print("\n📒 Your Notes:")
            print(content)

    except FileNotFoundError:
        print("⚠️ No notes file found.\n")


while True:
    print("===== Notes Saver Menu =====")
    print("1. Create Note")
    print("2. Read Notes")
    print("3. Exit")

    try:
        choice = input("Enter your choice: ")
    except EOFError:
        # If EOF is encountered during menu selection, exit gracefully instead of crashing
        print("\n👋 Exiting program due to lack of input...")
        break

    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice! Try again.\n")
