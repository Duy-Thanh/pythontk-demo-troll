from tkinter import *
from tkinter import messagebox
import random
import threading
import pyautogui

def no():
    open_custom_message_box()

def move_mouse_randomly():
    custom_box = custom_boxes[0]
    
    pyautogui.move(random.randint(0, root.winfo_screenwidth() - custom_box.winfo_width()), random.randint(0, root.winfo_screenheight() - custom_box.winfo_height()), _pause=False)
    pyautogui.click(random.randint(0, root.winfo_screenwidth() - custom_box.winfo_width()), random.randint(0, root.winfo_screenheight() - custom_box.winfo_height()))
    
def move_custom_boxes():
    for custom_box in custom_boxes:
        x = random.randint(0, root.winfo_screenwidth() - custom_box.winfo_width())
        y = random.randint(0, root.winfo_screenheight() - custom_box.winfo_height())
        custom_box.geometry(f'200x100+{x}+{y}')

    root.after(100, move_custom_boxes)  # Move every 100 milliseconds

def open_custom_message_box():
    root.withdraw()
    
    custom_box = Toplevel(root)
    custom_box.title('Custom Message Box')
    custom_box.resizable(width=False, height=False)

    message_label = Label(custom_box, text='You are gay', font='Arial 12 bold')
    message_label.pack(pady=10)

    btn_custom = Button(custom_box, text='Close', font='Arial 12 bold')
    btn_custom.pack()

    x = random.randint(0, root.winfo_screenwidth() - custom_box.winfo_width())
    y = random.randint(0, root.winfo_screenheight() - custom_box.winfo_height())
    custom_box.geometry(f'200x100+{x}+{y}')

    custom_boxes.append(custom_box)
    custom_box.after(10, lambda: set_topmost(custom_box))  # Auto focus after 3 seconds
    custom_box.protocol("WM_DELETE_WINDOW", lambda: None)
    custom_box.after(500, open_custom_message_box)
    custom_box.after(4, move_mouse_randomly)
    
def set_topmost(custom_box):
    custom_box.wm_attributes("-topmost", 1)
    custom_box.focus_force()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

def on_closing():
    pass  # Do nothing when attempting to close

def open_window():
    new_root = Tk()

    pyautogui.PAUSE = 0

    new_root.geometry('600x600')
    new_root.title('survey')
    new_root.resizable(width=False, height=False)
    new_root['bg'] = 'white'
    label = Label(new_root, text='Are you gay?', font='Arial 20 bold', bg='white').pack()
    btnYes = Button(new_root, text='No', font='Arial 20 bold')
    btnYes.place(x=170, y=100)
    btnYes.bind('<Enter>', motionMouse)
    btnNo = Button(new_root, text='Yes', font='Arial 20 bold', command=no).place(x=350, y=100)
    root.mainloop()

if __name__ == "__main__": 
    root = Tk()

    root.geometry('600x600')
    root.title('survey')
    root.resizable(width=False, height=False)
    root['bg'] = 'white'
    label = Label(root, text='Are you gay?', font='Arial 20 bold', bg='white').pack()
    btnYes = Button(root, text='No', font='Arial 20 bold')
    btnYes.place(x=170, y=100)
    btnYes.bind('<Enter>', motionMouse)
    btnNo = Button(root, text='Yes', font='Arial 20 bold', command=no).place(x=350, y=100)

    custom_boxes = []

    root.after(100, move_custom_boxes)  # Start moving the custom message boxes

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()
