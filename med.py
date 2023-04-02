import time
import os
import signal
import random

filename1 = "melody1.mp3"
filename2 = "melody2.mp3"
duration = 1800
interval = random.randint(30, 60)

def assan(sig, frame):
    os.system("termux-wake-unlock")
    print("\nWakelock released. Exiting...")
    exit(0)

def shavasana(sig, frame):
    os.system("termux-wake-unlock")
    print("\nWakelock released. Exiting...")
    exit(0)

signal.signal(signal.SIGINT, assan)

while True:
    print("Please select a yoga pose to perform:")
    print("1. Assan")
    print("2. Shavasana")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        signal.signal(signal.SIGINT, assan)
        os.system("termux-wake-lock")

        for i in range(duration, 0, -interval):
            print(f"{i // 60} minutes remaining...")
            os.system("play " + filename1)
            time.sleep(interval)

        os.system("termux-wake-unlock")

    elif choice == "2":
        signal.signal(signal.SIGINT, shavasana)
        os.system("termux-wake-lock")

        for i in range(duration, 0, -interval):
            print(f"{i // 60} minutes remaining...")
            os.system("play " + filename2)
            time.sleep(interval)

        os.system("termux-wake-unlock")

    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
