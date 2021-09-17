# Import the required libraries
from tkinter import *
import random, string
import pyperclip

# Initialize the GUI window
window = Tk()
window.geometry("300x300")
window.resizable(0, 0)
window.title("RANDOM PASSWORD GENERATOR")
window.configure(bg="white")

heading = Label(window, text="Generate your Password", font='arial 15 bold').pack()

# Select the Password Length per your requirement
password_label = Label(window, text='PASSWORD LENGTH', font='Times 12 bold').pack()
password_length = IntVar()
length = Spinbox(window, from_=8, to_=32, textvariable=password_length, width=20).pack()
pass_str = StringVar()


# Function to generate the password
def generate():
    password = ""
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(password_length.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


# generate buttons
Button(window, text="GENERATE PASSWORD", command=generate).pack(pady=5)
Entry(window, textvariable=pass_str).pack()


# copy the password to clipboard
def copy_password():
    pyperclip.copy(pass_str.get())


Button(window, text="COPY TO CLIPBOARD", command=copy_password).pack(pady=5)

# loop to run the main program
window.mainloop()
