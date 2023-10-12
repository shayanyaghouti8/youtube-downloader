from tkinter import *
from tkinter import font
from tkinter.filedialog import askdirectory
from pytube import YouTube

window =  Tk()
window.title("youtubedownloader")
window.minsize(450, 200)

def widget():

    linklabel = Label(window, text="video link")
    linklabel. grid(row=0, column=0, padx=20, pady=20)
    linklabel.config(font=("None", 15), fg="blue")

    link_input= Entry(window, width=30, textvariable=video_link)
    link_input.grid(row=0, column=1)

    placelabel = Label(window, text= "directory")
    placelabel.grid(row=1, column=0)
    placelabel.config(font=("None", 15), fg="blue")

    placeinput = Entry(window, width=30)
    placeinput.grid(row=1, column=1)

    placebtn = Button(window, text= "open folder", width = 10, bg="blue", fg= "white", command=browse)
    placebtn.grid(row=1, column=2)

    downloadbtn = Button(text= "download", command=download)
    downloadbtn.grid(row=2, column=1)
    downloadbtn.config(height=3, width=20, bg="green", fg="White")

def browse():
   directory = askdirectory(initialdir="your directory path", title="save")
def download():
    link = video_link.get()
    print("link")

video_link = StringVar() 



widget()

window.mainloop()