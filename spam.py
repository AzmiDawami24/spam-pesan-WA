import pyautogui as pt
import time


batas = input("Masukkan batas: ")
pesan = input("Masukkan pesan: ")
time.sleep(5)
i = 0

while i < int(batas):
    pt.typewrite(pesan)
    pt.press("enter")
    i += 1
