import time
import os
import signal
import random

filename = "melody1.mp3"
duration = 1800
interval = random.randint(30, 60)
filename2 = "melody2.mp3"

def menu():
    while True:
        def assan(sig, frame):
            os.system("termux-wake-unlock")
            print("\nWakelock released. Returning to menu...\n")
            return

        signal.signal(signal.SIGINT, assan)

        print("Please select a yoga pose to perform:")
        print("1. Assan")
        print("2. Shavasana")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Start the countdown loop
            os.system("termux-wake-lock")
            try:
                for i in range(duration, 0, -interval):
                    print(f"{i // 60} minutes remaining...")
                    os.system("play " + filename)
                    time.sleep(interval)
            except KeyboardInterrupt:
                print("\nReturning to menu...\n")
            finally:
                # Release wakelock at the end of the loop
                os.system("termux-wake-unlock")

        elif choice == "2":
            os.system("termux-wake-lock")

            def play():
                os.system("play " + filename2)

            try:
                while True:
                    play()
            except KeyboardInterrupt:
                print("\nReturning to menu...\n")
            finally:
                os.system("termux-wake-unlock")

        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


while True:
    menu()
    answer = input("Do you want to perform another action? (y/n)")
    if answer.lower() == "n":
        print("Goodbye!")
        break
