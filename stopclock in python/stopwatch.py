import tkinter as tk
import time

class ClockTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock with Timer")

        self.timer_running = False
        self.timer_seconds = 0

        # Clock Label
        self.clock_label = tk.Label(root, text="00:00:00", font=("Helvetica", 30), width=10)
        self.clock_label.pack()

        # Timer Label
        self.timer_label = tk.Label(root, text="Timer: 0", font=("Helvetica", 15))
        self.timer_label.pack(pady=10)

        # Timer buttons
        self.start_button = tk.Button(root, text="Start Timer", font=("Helvetica", 15), command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(root, text="Stop Timer", font=("Helvetica", 15), command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(root, text="Reset Timer", font=("Helvetica", 15), command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Clock update function
        self.update_clock()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.increment_timer()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.timer_seconds = 0
        self.timer_label.config(text="Timer: 0")

    def increment_timer(self):
        if self.timer_running:
            self.timer_seconds += 1
            self.timer_label.config(text=f"Timer: {self.timer_seconds}")
            self.root.after(1000, self.increment_timer)

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)  # Update every second

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockTimerApp(root)
    root.mainloop()
