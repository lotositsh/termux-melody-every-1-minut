import time
import os
import signal
import random

filename = "melody1.mp3"
duration = 1800
interval = random.randint(30, 60)
print(interval)
filename2 = "melody2.mp3"


def assan(sig, frame):
    print("\n1 - shavasana;\n0 - exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        os.system("play " + filename2)
		os.system("termux-wake-unlock")
		print("\nwake unlock\n")
        exit(0)
    elif choice == '0':
        os.system("termux-wake-unlock")
        print("\nwake unlock\n")
        exit(0)
signal.signal(signal.SIGINT, assan)

os.system("termux-wake-lock")
remaining_time = duration
for i in range(duration, 0, -interval):
    print(f"{i//60} minutes remaining...")
    os.system("play " + filename)
    time.sleep(interval)
os.system("termux-wake-unlock")
