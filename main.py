import pyautogui
import keyboard
import tkinter as tk
import threading
import mouse

root = tk.Tk()
root.geometry("500x500")

def find_perint():
    image_found = False
    image_list = ['per1.png', 'per16.png', 'per10.png']

    while not image_found:
        if pyautogui.locateCenterOnScreen(image="bluechecker.png", confidence=0.9, minSearchTime=0.5) is not None:
            pyautogui.keyDown('shift')
            res = pyautogui.locateCenterOnScreen(image=image_list[get_selected_index()], confidence=0.8, minSearchTime=0.5)
            if res is None:
                mouse.click('left')
            else:
                image_found = True
                print("Found it!")
        else:
            pyautogui.keyUp('shift')

def start_thread():
    thread = threading.Thread(target=find_perint)
    thread.start()

def get_selected_index():
    selected_index = listbox.curselection()
    if selected_index:
        return selected_index[0]
    else:
        return None

list_of_mods = ['Either per 16 and per 10 for wand', 'Per 16 for wand', 'Per 10 for wand']
listbox = tk.Listbox(root)
for item in list_of_mods:
    listbox.insert(tk.END, item)
listbox.pack()

# START BUTTON
B = tk.Button(root, text="START", command=start_thread, height=5, width=20)
B.place(x=10, y=10)

root.mainloop()



root.mainloop()






