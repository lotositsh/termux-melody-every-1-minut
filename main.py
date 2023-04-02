import assan as f1
import shavasana as f2

while True:
    print("Please select a yoga pose to perform:")
    print("1. Assan")
    print("2. Shavasana")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        f1.assan()
    elif choice == "2":
        f2.shavasana()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
