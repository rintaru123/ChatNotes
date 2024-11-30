import tkinter as tk
from tkinter import scrolledtext, messagebox, Listbox, Scrollbar, Frame, Button
from tkcalendar import Calendar
import sqlite3
from datetime import datetime
from tkinter import ttk
from configparser import ConfigParser

def on_enter1(event=None):
    date=datetime.now().strftime('%y.%m.%d %H:%M:%S')
    if text2.get("1.0",tk.END) and event.keysym == 'Return':
        text.insert(tk.END,"{0} \n {1}".format(date,text2.get("1.0",tk.END)))
        text2.delete("1.0",tk.END)
        text.see("end")
        text2.configure(state='disabled')
        text2.configure(state="normal")
        text2.focus_set()

root=tk.Tk()
root.geometry("900x500+200+10")
root.title("ChatNotes")
root.option_add('*Font', 'Calibri 12')
root.attributes("-toolwindow", True)
root.resizable("true","true")

frame=Frame(root,width=100)
frame.pack(anchor="w",side=tk.LEFT,fill=tk.Y,expand="false")
frame2=Frame(root)
frame2.pack(side=tk.LEFT,fill=tk.BOTH,expand="true")
text=scrolledtext.ScrolledText(frame2)
text.pack(fill=tk.BOTH,expand="true")


text2=tk.Text(frame2,height="50")
text2.pack(side=tk.BOTTOM,fill=tk.X,pady="20 10",expand="false")
text2.focus_set()
text2.bind("<KeyRelease>",on_enter1)


frame3=Frame(root,width="200")
frame3.pack(side=tk.RIGHT,fill=tk.Y,anchor="e")
root.mainloop()
