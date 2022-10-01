"""Задача на дом: написать программу, которая постоянно нажимает какую то клавишу на клавиатуре с помощью pyautogui и делает это каждые 30 секунд"""

import pyautogui as pag

while True:
    pag.press('left', interval=30)

