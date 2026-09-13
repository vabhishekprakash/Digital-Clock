# Digital Clock

A desktop clock built with Python and Tkinter. It shows the current time and updates every second.

This was one of my first Python projects, written in my first year. It is kept here as a record of where I started.

## Running it

You need Python 3. Tkinter ships with the standard library on most installs, so there is nothing to install.

```
python main.py
```

A 400x200 window opens showing the time.

## How it works

`strftime` formats the current time into a string, and `label.after(1000, time)` schedules the same function to run again in one second. That reschedule is what keeps the clock live, rather than a loop.
