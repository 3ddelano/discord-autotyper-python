"""discord-autotyper-python
Delano Lourenco (https://delano-lourenco.web.app)
Repo: https://github.com/3ddelano/discord-autotyper-python
"""


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
onetime_queue = []
timers = []

cmd_count = 0

started = False
exited = False
cooldown = False
onetime_cooldown = False

onetime_delay = int(settings["onetime"]["delay"])
randomTime = int(settings["randomTime"])
command_delay = float(settings["commandDelay"])
stop_after = float(settings["stopAfter"])
controller = Controller()


def stop_typer():
    global started
    if started:
        started = False
        print("Auto stopped.")


def start_stop_after():
    global stop_after
    if stop_after > 0:
        Timer(stop_after*60, stop_typer).start()


def send_command(text):
    global controller
    controller.type(text)
    controller.press(Key.enter)
    controller.release(Key.enter)


def add_command(text, waittime, isRandom):
    global started
    global queue
    global timers
    global cmd_count
    global randomTime

    if started:
        random_delay = 0
        if isRandom:
            random_delay = floor(randint(0, randomTime))
        if randint(0, 100) / 100 <= settings["randomSkip"]:
            print(
                f"skipped command: {text} | next in {waittime + random_delay}s | total commands: {cmd_count}")
        else:
            cmd_count += 1
            queue.append({"text": text, "waittime": waittime})
            print(
                f"sending cmd: {text} | next in {waittime + random_delay}s | total commands: {cmd_count}")
        t = Timer(waittime + random_delay, add_command, args=(
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


def remove_cooldown():
    global cooldown
    cooldown = False


def remove_onetime_cooldown():
    global onetime_cooldown
    onetime_cooldown = not onetime_cooldown


def press_backspace():
    global controller
    controller.press(Key.backspace)
    controller.release(Key.backspace)


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
        press_backspace()
        started = not started
        if started:
            print("Started.")
            init_typer()
            start_stop_after()
        else:
            print("Stopped.")
    if key == settings["exitkey"]:
        press_backspace()
        print("Exited.")
        started = False
        exited = True
        return False

    global onetime_cooldown
    global onetime_queue
    if key == settings["onetime"]["hotkey"]:
        press_backspace()
        print("Started onetime cmds.")
        cmds = settings["onetime"]["commands"]
        for i in cmds:
            onetime_queue.append(i)


print("Discord AutoTyper\nWaiting for hotkey to be pressed...")
listener = Listener(on_press=on_key_press)
listener.start()


while not exited:
    if started:
        if len(queue) > 0:
            if not cooldown:
                cooldown = True
                send_command(queue[0]["text"])
                queue.pop(0)
                Timer(command_delay, remove_cooldown).start()

    if len(onetime_queue) > 0:
        if not onetime_cooldown:
            onetime_cooldown = True
            send_command(onetime_queue[0])
            print(f"sending onetime cmd: {onetime_queue[0]}")
            onetime_queue.pop(0)

            if len(onetime_queue) == 0:
                print("finished sending onetime cmds.")

            Timer(onetime_delay, remove_onetime_cooldown).start()
