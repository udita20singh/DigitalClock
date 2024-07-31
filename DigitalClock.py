import time
from tkinter import CENTER, Button, Label, StringVar, Tk

# Initialize the main window
root = Tk()
root.title("Digital Clock")
root.geometry("600x300")  # Set window size

# Variable to toggle between 12-hour and 24-hour formats
time_format = StringVar(value="%I:%M:%S %p")  # Start with 12-hour format

# Function to update the time display
def present_time():
    # Get the current time and format it based on the selected format
    display_time = time.strftime(time_format.get())
    digi_clock.config(text=display_time)
    # Update the clock every 1000 milliseconds (1 second)
    digi_clock.after(1000, present_time)
    
    # Update the date display
    current_date = time.strftime("%A, %B %d, %Y")
    date_label.config(text=current_date)

# Function to toggle between 12-hour and 24-hour formats
def toggle_format():
    if time_format.get() == "%I:%M:%S %p":
        time_format.set("%H:%M:%S")  # Switch to 24-hour format
        format_button.config(text="Switch to 12-hour format")
    else:
        time_format.set("%I:%M:%S %p")  # Switch to 12-hour format
        format_button.config(text="Switch to 24-hour format")

# Create the digital clock label
digi_clock = Label(root, font=("Cambria", 100), bg="black", fg="white", padx=20, pady=20)
digi_clock.pack(expand=True)

# Create the date label
date_label = Label(root, font=("Cambria", 20), bg="black", fg="white")
date_label.pack()

# Create the toggle button
format_button = Button(root, text="Switch to 24-hour format", command=toggle_format, font=("Cambria", 15), bg="grey", fg="white", padx=10, pady=5)
format_button.pack(pady=10)

# Start the time updates
present_time()

# Run the Tkinter event loop
root.mainloop()
