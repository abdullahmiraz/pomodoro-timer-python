import tkinter as tk
from tkinter import ttk
import pygame
import os
from playsound import playsound


class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        # Double the width of the window
        new_width = self.root.winfo_screenwidth() * 1 // 3  # Set to 2/3 of the screen width
        new_height = self.root.winfo_screenheight() * 1 // 2  # Keep the height unchanged

        self.root.geometry(f"{new_width}x{new_height}")

        self.minutes = 25  # Initial time
        self.seconds = 0
        self.timer = None  # Initialize timer attribute

        self.timer_label = ttk.Label(root, text="25:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=10)

        self.start_button = ttk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.pause_button = ttk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(pady=5)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(pady=5)

        self.reset_button = ttk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=5)

        # Add minute and second options to the time_list
        self.time_list_minutes = ttk.Combobox(
            root, values=[0, 5, 10, 15, 20, 25, 30, 45, 60], state="readonly"
        )
        self.time_list_minutes.set("25")
        self.time_list_minutes.pack(pady=5)

        self.time_list_seconds = ttk.Combobox(
            root, values=[0, 5, 10, 15, 20, 30], state="readonly"
        )
        self.time_list_seconds.set("0")
        self.time_list_seconds.pack(pady=5)

        self.paused = False
        self.timer_running = False

        # Create Stop Alarm button
        self.stop_alarm_button = ttk.Button(
            root, text="Stop Alarm", command=self.stop_alarm,  
        )
        self.stop_alarm_button.pack(pady=5)

        # Initialize pygame mixer for playing alarm sound
        pygame.mixer.init()

      

    def start_timer(self):
        if not self.timer_running:
            if not self.paused:
                self.minutes = int(self.time_list_minutes.get())
                self.seconds = int(self.time_list_seconds.get())
            self.update_timer()
            self.timer_running = True

    def pause_timer(self):
        if self.timer_running:
            self.root.after_cancel(self.timer)
            self.paused = True
            self.timer_running = False

    def stop_timer(self):
        if self.timer_running:
            self.root.after_cancel(self.timer)
            self.paused = False
            self.timer_label["text"] = f"{self.minutes:02d}:{self.seconds:02d}"
            self.timer_running = False

    def reset_timer(self):
        if self.timer_running:
            self.root.after_cancel(self.timer)
        self.minutes = int(self.time_list_minutes.get())
        self.seconds = int(self.time_list_seconds.get())
        self.timer_label["text"] = f"{self.minutes:02d}:{self.seconds:02d}"
        self.paused = False
        self.timer_running = False

    def update_timer(self):
        self.timer_label["text"] = f"{self.minutes:02d}:{self.seconds:02d}"

        if self.minutes == 0 and self.seconds == 0:
            self.stop_timer()
            self.play_alarm()  # Play alarm sound when the timer reaches 0:00
            return

        self.timer = self.root.after(1000, self.update_timer)

        if self.seconds == 0:
            self.minutes -= 1
            self.seconds = 59
        else:
            self.seconds -= 1

    def play_alarm(self):
        pygame.mixer.music.load("D:\\python-pomodoro\\alarm.mp3")
        pygame.mixer.music.play(-1)

    def stop_alarm(self):
        pygame.mixer.music.stop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
