from shutil import move
from turtle import left
import pyautogui

pyautogui.alert('O programa vai começar...')
pyautogui.PAUSE = 0.5
# Abrir o Google Driver no meu computador
pyautogui.press ('winleft')
pyautogui.write ('chrome')
pyautogui.press ('enter')
pyautogui.move(10, 10, duration=0.5)
pyautogui.click(10=move)