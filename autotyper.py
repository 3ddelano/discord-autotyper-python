import json
from math import floor
from threading import Timer
from pynput.keyboard import Key, Controller, Listener
from random import randint


try:
    open("./settings.json")
except FileNotFoundError:
    print("Error: settings.json file not found in directory.")
    quit()


settings = json.load(open("./settings.json"))
queue = []
timers = []
cmd_count = 0
started = False
exited = False
cooldown = False
controller = Controller()


def send_command(text):
    controller.type(text)
    controller.press(Key.enter)


def add_command(text, waittime, isRandom):
    global started
    global queue
    global timers
    global cmd_count

    if started:
        randomtime = 0
        if isRandom:
            randomtime = floor(randint(0, 60))
        if randint(0, 100) / 100 <= settings["randomSkip"]:
            print(
                f"skipped command: {text} | next in {waittime + randomtime}s | total commands: {cmd_count}")
        else:
            cmd_count += 1
            queue.append({"text": text, "waittime": waittime})
            print(
                f"sending cmd: {text} | next in {waittime + randomtime}s | total commands: {cmd_count}")
        t = Timer(waittime + randomtime, add_command, args=(
            text, waittime, isRandom))
        t.start()
        timers.append(t)


def init_typer():
    global queue
    global timers
    commands = settings["commands"]
    queue = []
    for timer in timers:
        timer.cancel()
    timers = []
    for cmd in commands:
        add_command(cmd["text"], int(cmd["waittime"]),
                    cmd["randomtime"] or False)


def on_key_press(key):
    if hasattr(key, "char"):
        key = str(key.char)
    else:
        key = str(key)

    if settings["showKeyCode"]:
        print("Key pressed: ", key)

    global started
    global exited
    if key == settings["hotkey"]:
        started = not started
        if started:
            print("Started.")
            init_typer()
        else:
            print("Paused.")
    elif key == settings["exitkey"]:
        print("Exited.")
        exited = True
        return False


print("Discord AutoTyper\nWaiting for hotkey to be pressed...")
listener = Listener(on_press=on_key_press)
listener.start()


def removeCooldown():
    global cooldown
    cooldown = False


while not exited:
    if started:
        if len(queue) > 0:
            if not cooldown:
                cooldown = True
                send_command(queue[0]["text"])
                queue.pop(0)
                Timer(1.0, removeCooldown).start()
