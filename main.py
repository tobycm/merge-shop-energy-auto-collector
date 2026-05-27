import time

import pyautogui
import serial

pico = serial.Serial("COM5")  # Replace "COM4" with your actual port

def click():
    pico.write("ml\n".encode("utf-8"))

def home():
    pico.write("mm -9999 -9999\n".encode("utf-8"))

def move_mouse(dx, dy):
    pico.write(f"mm {dx} {dy}\n".encode("utf-8"))

def hold_right_arrow(delay):
    pico.write(f"hra {delay}\n".encode("utf-8"))

def hold_w(delay):
    pico.write(f"hw {delay}\n".encode("utf-8"))

def press_e():
    pico.write("pe\n".encode("utf-8"))

def press_esc():
    pico.write("pesc\n".encode("utf-8"))

def press_l():
    pico.write("pl\n".encode("utf-8"))

def press_enter():
    pico.write("penter\n".encode("utf-8"))

# home()

current_dx: int = 0
current_dy: int = 0

def move_mouse_absolute(x, y):
    global current_dx, current_dy
    dx = x - current_dx
    dy = y - current_dy
    move_mouse(dx, dy)
    current_dx = x
    current_dy = y

def locate_center_then_move(image_path):
    point: pyautogui.Point = pyautogui.locateCenterOnScreen(image_path, confidence=0.94)
    move_mouse_absolute(point[0], point[1])
    time.sleep(0.8)

def main():
    print("Hello from Merge Shop bot!")

    # locate_center_then_move("roblox.png")

    # click()
    # time.sleep(0.8)

    # locate_center_then_move("merge.png")

    # click()
    # time.sleep(0.4)
    # click()
    # time.sleep(0.4)
    # click()

    # time.sleep(0.8)

    # locate_center_then_move("play-button.png")

    click()

    time.sleep(3)

    hold_right_arrow(0.725)

    time.sleep(0.3)

    hold_w(1.2)

    time.sleep(0.3)

    press_e()

    time.sleep(0.3)

    press_esc()

    time.sleep(0.3)

    press_l()

    time.sleep(0.3)

    press_enter()

    time.sleep(0.3)

if __name__ == "__main__":
    time.sleep(5)

    delay = 60 * 99

    while True:
        main()

        for i in range(delay):
            print(f"Delay: {i}s/{delay}s", end="\r")
            time.sleep(1)
