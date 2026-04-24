
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time


global fn
fn = ""

root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Machine Learning Based Predicting Student Academic Success")

# 43
video_label =tk.Label(root)
video_label.pack()
# read video to display on label
#player = tkvideo("IMG", video_label,loop = 1, size = (w, h))
#player.play()




#####For background Image
image2 = Image.open('stud1.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Student Performance Prediction System",font=("Times New Roman", 35, 'bold'),
                    background="Maroon", fg="white", width=50, height=1)
label_l1.place(x=0, y=0)


def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=12, height=1,font=('times', 20, ' bold '), bg="Purple", fg="white")
button1.place(x=80, y=160)

button2 = tk.Button(root, text="Register",command=reg,width=12, height=1,font=('times', 20, ' bold '), bg="Purple", fg="white")
button2.place(x=80, y=260)

button3 = tk.Button(root, text="Exit",command=window,width=12, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=80, y=360)

root.mainloop()
