from Tkinter import *
import tkSimpleDialog
import tkMessageBox

# Set up GUI
root = Tk()
w = Label(root, text="Something !")
w.pack()

# Welcome the user
tkMessageBox.showinfo("SOME INF TO WELCOME")

# Get user info
name = tkSimpleDialog.askstring("Name", "WHat is your fucking name?")
age = tkSimpleDialog.askfloat("Age", "ARE YOU LEAGEL?")

# Process information
output = "Hello, %s. I hope you're doing fine today." % (name)
output += "Our records indicate that you are %d years old" % (age)

# Produce the output message box
tkMessageBox.showinfo("Results", output)