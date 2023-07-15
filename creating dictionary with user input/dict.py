dictionary = {}

while True:
    print("\nMENU:")
    print("1. Create dictionary")
    print("2. Insert element")
    print("3. Delete element")
    print("4. Display dictionary")
    print("5. Exit")

    choice = input("Enter your choice 1 to 5: ")

    if choice == '1':
        dictionary = {}
        print("Dictionary created!")
    elif choice == '2':
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        dictionary[key] = value
        print("Element inserted successfully!")
    elif choice == '3':
        key = input("Enter the key to delete: ")
        if key in dictionary:
            del dictionary[key]
            print("Element deleted successfully!")
        else:
            print("Key not found!")
    elif choice == '4':
        if not dictionary:
            print("Dictionary is empty!")
        else:
            print("Dictionary contents:")
            for key, value in dictionary.items():
                print(f"{key}: {value}")
    elif choice == '5':
        break
    else:
        print("Invalid choice! Try again.")

