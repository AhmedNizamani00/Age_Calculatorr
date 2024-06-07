from tkinter import *
from datetime import date

# Initialize the main window
root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Age Calculator")

# Load the icon image
icon = PhotoImage(file="image1.png")
root.iconphoto(True, icon)

# Configure the window background color
root.config(background="#3256a8")

# Load an image (optional, make sure the file path is correct)
photo = PhotoImage(file="image.png")
myimage = Label(root, image=photo)
myimage.pack(padx=15, pady=15)

def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    Label(root, text=f"{nameValue.get()} your age is {age}", font=30).place(x=300, y=500)

# Create labels
Label(root, text="Name", font=23).place(x=200, y=250)
Label(root, text="Year", font=23).place(x=200, y=300)
Label(root, text="Month", font=23).place(x=200, y=350)
Label(root, text="Day", font=23).place(x=200, y=400)

# Create entry fields
nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=30, bd=3, font=20)
nameEntry.place(x=300, y=250)

yearEntry = Entry(root, textvariable=yearValue, width=30, bd=3, font=20)
yearEntry.place(x=300, y=300)

monthEntry = Entry(root, textvariable=monthValue, width=30, bd=3, font=20)
monthEntry.place(x=300, y=350)

dayEntry = Entry(root, textvariable=dayValue, width=30, bd=3, font=20)
dayEntry.place(x=300, y=400)

# Create button
Button(root, text="Calculate Age", font=20, bg="black", fg="white", width=11, height=2, command=calculateAge).place(x=300, y=450)

# Start the main loop
root.mainloop()
