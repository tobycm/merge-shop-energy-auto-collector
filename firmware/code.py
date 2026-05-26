import time

import usb_cdc
import usb_hid
from adafruit_hid.keyboard import Keyboard, Keycode
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

keyboard = Keyboard(usb_hid.devices)

def home():
    mouse.move(-9999, -9999)

# home()


while True:
    if usb_cdc.data.in_waiting == 0:
        continue

    command: str = usb_cdc.data.readline().decode("utf-8").rstrip()

    parts = command.split(" ")

    code = parts.pop(0)

    if code == "mm": # mouse move
        dx = int(parts.pop(0))
        dy = int(parts.pop(0))
        mouse.move(dx, dy)

    if code == "ml": # mouse left click
        mouse.press(1)
        time.sleep(0.03)
        mouse.release(1)

    if code == "hra": # hold right arrow
        delay = float(parts.pop(0))
        keyboard.press(Keycode.RIGHT_ARROW)
        time.sleep(delay)
        keyboard.release(Keycode.RIGHT_ARROW)

    if code == "hw": # hold w
        delay = float(parts.pop(0))
        keyboard.press(Keycode.W)
        time.sleep(delay)
        keyboard.release(Keycode.W)

    if code == "pe": # press e
        keyboard.press(Keycode.E)
        time.sleep(0.1)
        keyboard.release(Keycode.E)

    if code == "pesc": # press escape
        keyboard.press(Keycode.ESCAPE)
        time.sleep(0.1)
        keyboard.release(Keycode.ESCAPE)

    if code == "pl": # press l
        keyboard.press(Keycode.L)
        time.sleep(0.1)
        keyboard.release(Keycode.L)

    if code == "penter": # press enter
        keyboard.press(Keycode.ENTER)
        time.sleep(0.1)
        keyboard.release(Keycode.ENTER)

    

    print(command)