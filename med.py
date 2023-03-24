import time
import os
import signal

filename = "melody1.mp3"
duration = 1800
interval = 60
os.system("termux-wake-lock")

# Define a signal handler function to release wakelock on SIGINT
def signal_handler(sig, frame):
    os.system("termux-wake-unlock")
    print("\nWakelock released. Exiting...")
    exit(0)

# Register the signal handler function for SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Start the countdown loop
for i in range(duration, 0, -interval):
    print(f"{i//60} minutes remaining...")
    os.system("play " + filename)
    time.sleep(interval)

# Release wakelock at the end of the loop
os.system("termux-wake-unlock")	  
