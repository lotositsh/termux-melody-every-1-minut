import time
import os
import signal
import random

filename = "melody1.mp3"
duration = 1800
interval = random.randint(30, 60)
filename2 = "melody2.mp3"

def assan(sig, frame):
    print("1 - shavasana; 0 - exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        os.system("play " + filename2)
    elif choice == '0':
        os.system("termux-wake-unlock")
        print("\nWakelock released. Returning to menu...\n")
        exit(0)
signal.signal(signal.SIGINT, assan)

# Start the countdown loop
os.system("termux-wake-lock")
remaining_time = duration
while remaining_time > 0:
    print(f"{remaining_time // 60} minutes remaining...")
    os.system("play " + filename)
    time.sleep(min(interval, remaining_time))
    remaining_time -= interval
os.system("termux-wake-unlock")
