import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

def disable_ntp():
    try:
        subprocess.run(['sudo','timedatectl','set-ntp','false'],check=True)
    except subprocess.CalledProcessError as e:
        print(f"{e}")

def check_superuser():
    """Check if the script is run as superuser"""
    if not os.name == 'nt' and os.geteuid() != 0:
        messagebox.showerror("Error", "This application must be run as root.")
        sys.exit(1)

def set_system_time(new_time):
    """Set the system time using PowerShell on Windows"""
    try:
        # Use PowerShell command to set the date and time
        subprocess.run(['sudo', 'timedatectl', 'set-time',new_time], check=True)
        messagebox.showinfo("Success", f"System time updated to {new_time}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to set system time: {e}")

def on_submit():
    """Handler for the submit button"""
    new_time = entry.get()
    disable_ntp()
    set_system_time(new_time)

# Check for superuser privileges before starting the GUI
check_superuser()

# Create the GUI application
root = tk.Tk()
root.title("Set System Time")

# Create and place the label
label = tk.Label(root, text="Enter the new date and time (YYYY-MM-DD HH:MM:SS):")
label.pack(padx=20, pady=5)

# Create and place the entry widget
entry = tk.Entry(root, width=25)
entry.pack(padx=20, pady=5)

# Create and place the submit button
button = tk.Button(root, text="Set Time", command=on_submit)
button.pack(pady=10)

# Run the application
root.mainloop()
