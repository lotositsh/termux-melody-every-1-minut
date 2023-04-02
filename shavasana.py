import os
import signal

filename = "melody2.mp3"
os.system("termux-wake-lock")

def shavasana(sig, frame):
    os.system("termux-wake-unlock")
    print("\nWakelock released. Exiting...")
    exit(0)

signal.signal(signal.SIGINT, shavasana)

def play():
    os.system("play " + filename)

os.system("termux-wake-unlock")
