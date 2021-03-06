from fileinput import filename
import tkinter as tk
from tkinter import Frame, filedialog, Text
import os


root = tk.Tk()
apps = []



def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables","*.exe"),("all files", "*.*")))

apps.append(filename)
print(filename)



canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


for app in apps:
    label = tk.Label(frame, text=app, bg="gray")
    label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

        

openfile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openfile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')


