import time
import tkinter as tk
from tkinter import messagebox, simpledialog
 
class GoogleTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Google Timer")
        self.master.geometry("300x250")

        self.time_left = 0
        self.is_running = False

        self.label = tk.Label(master, text="00:00", font=("Arial", 48))
        self.label.pack(pady=20)

        self.set_time_button = tk.Button(master, text="Set Time", command=self.set_time)
        self.set_time_button.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer, state=tk.DISABLED)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

    def set_time(self):
        minutes = simpledialog.askinteger("Set Timer", "Enter the number of minutes:", minvalue=1, maxvalue=180)
        if minutes is not None:
            self.time_left = minutes * 60
            self.update_display()
            self.start_button.config(state=tk.NORMAL)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.set_time_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.update_timer()

    def stop_timer(self):
        self.is_running = False
        self.set_time_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            self.update_display()
            self.master.after(1000, self.update_timer)
        elif self.is_running and self.time_left == 0:
            messagebox.showinfo("Time's up!", f"Your set time has passed. Take a break!")
            self.stop_timer()

    def update_display(self):
        minutes, seconds = divmod(self.time_left, 60)
        time_string = f"{minutes:02d}:{seconds:02d}"
        self.label.config(text=time_string)

if __name__ == "__main__":
    root = tk.Tk()
    timer = GoogleTimer(root)
    root.mainloop()