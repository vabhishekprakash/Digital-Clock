import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

root.geometry("400x200")
root.resizable(False, False)
root.configure(bg='white')

def time():
    string = strftime('%H:%M:%S %p')
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
