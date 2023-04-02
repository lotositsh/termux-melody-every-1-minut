import os
import signal

filename = "melody2.mp3"
os.system("termux-wake-lock")


def play():
    os.system("play " + filename)


def shavasana(sig, frame):
    os.system("termux-wake-unlock")
    print("\nWakelock released. Exiting...")
    exit(0)

# Register the signal handler function for SIGINT
signal.signal(signal.SIGINT, shavasana)

os.system("termux-wake-unlock")