import time
import os
import signal
import random

filename = "melody1.mp3"
duration = 1800
interval = random.randint(30, 60)
filename2 = "melody2.mp3"

while True:
    print("Please select a yoga pose to perform:")
    print("1. Assan")
    print("2. Shavasana")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        def assan(sig, frame):
            os.system("termux-wake-unlock")
            print("\nWakelock released. Exiting...")
            exit(0)

        # Register the signal handler function for SIGINT
        signal.signal(signal.SIGINT, assan)

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
        def shavasana(sig, frame):
            os.system("termux-wake-unlock")
            print("\nWakelock released. Exiting...")
            exit(0)

        signal.signal(signal.SIGINT, shavasana)
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
