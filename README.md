# pomodoro-timer-python

## How to run

---

`pyinstaller --onefile --noconsole --icon=timer.ico --name=pomodoro pomodoro.py`

paste the code above to the bash

## Dependencies to install:

---

The dependencies/components used in this project include:

Python Standard Library Modules:

tkinter: GUI toolkit for the graphical user interface.  
os: Provides a way to interact with the operating system.  
Third-Party Libraries:

pygame: Library for multimedia applications, used here for playing the alarm sound.  
playsound: Library for playing sound files.  
External Files:

alarm.mp3: Sound file used for the alarm.  
timer.ico: Icon file for the application.

## Check the app size:

---

`ls -lh dist`

## Reset Build Folders:

---

`rm -rf build dist`
