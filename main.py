
A 400x200 window opens showing the time.

## How it works

`strftime` formats the current time into a string, and `label.after(1000, time)` schedules the same function to run again in one second. That reschedule is what keeps the clock live, rather than a loop.

import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

root.geometry("400x200")
root.resizable(False, False)
root.configure(bg='white')

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  

label = tk.Label(
    root,
    font=('Helvetica', 48, 'bold'),
    background='white',
    foreground='black'
)
label.pack(expand=True)

time()  
root.mainloop()  
