from tkinter import *
import tkinter as tk
import tkinter.messagebox as mb

root = tk.Tk()
root.title("じゃんけん")
root.geometry("500x200")

def Enhancer():
    mb.showinfo("result","チョキを出されました、あなたの負けです")

def say_janken2():
    mb.showinfo("result","グーを出されました、あなたの負けです")

def say_janken3():
    mb.showinfo("result","パーを出されました、あなたの負けです")

desc_label = tk.Label(text="じゃんけん")
desc_label.pack()



button = tk.Button(
    text='パー',
    width=10,
    command=Enhancer
)
button.place(x=350, y=120)

button1 = tk.Button(
    text='チョキ',
    width=10,
    command=say_janken2
)
button1.place(x=200, y=120)

button2 = tk.Button(
    text='グー',
    width=10,
    command=say_janken3
)
button2.place(x=50, y=120)

root.mainloop()
