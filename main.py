import pyautogui
import mouseinfo
import mouse
import time
import pyauto
import keyboard
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")


def get_selected_index():
    selected_index = listbox.curselection()
    if selected_index:
        return selected_index[0]
    else:
        return None


def find_perint():
    image_found = False
    checker = False
    list = ['per1.png', 'per16.png', 'per10.png']
    while not image_found:
        if pyautogui.locateCenterOnScreen(image="bluechecker.png", confidence=0.9, minSearchTime=0.5) is not None:
            checker = True
        while checker:
            pyautogui.hold('shift')
            res = pyautogui.locateCenterOnScreen(image=list[get_selected_index()], confidence=0.9, minSearchTime=0.5)
            if keyboard.is_pressed('Tab'):
                break
            if res is None:
                mouse.click('left')
                checker = False
            else:
                image_found = True
                print("Found it!")

#START BUTTON
B = Button(root, text="START", command=find_perint(),height = 5, width=20).place(x=10, y=10)

#LISTBOX
list_of_mods = ['Either per 16 and per 10 for wand', 'Per 16 for wand', 'Per 10 for wand']

listbox = tk.Listbox(root)
for item in list_of_mods:
    listbox.insert(tk.END, item)
listbox.pack()

root.mainloop()






