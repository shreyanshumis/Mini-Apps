#reminder app - with notifications and dedicated GUI

from tkinter import *
import time
from winotify import Notification, audio

def onClick():
    names = name.get()
    contents = content.get()
    times = float(float(time1.get())*60)
    seconds = times
    time.sleep(seconds)
    refresh(names, contents)

def refresh(name2, content2):
    toast = Notification(app_id="Rey Reminder",
                        title = f"{name2}",
                        msg=f"{content2}",
                        duration="long")
    toast.set_audio(audio.LoopingCall, loop=True)
    toast.show()
    

def content():
    #sends title, message and actions to refresh()
    pass

if __name__== "__main__":
    #main window which opens upon the start of this program.
    window = Tk()
    window.title("Rey Reminder")
    window.geometry('800x400')

    #The title
    Label(window, text= "Study Alarm Application", font=("Arial", 20)).pack()
    Label(window, text= "Enter the following", font=("Arial", 12)).pack()
    #===========

    Label(window, text="Name",font=("Arial", 8)).pack()
    name = Entry(window,width=50,font=("arial", 18))
    name.pack()
    Label(window, text="Content",font=("Arial", 8)).pack()
    content = Entry(window,width=50,font=("arial", 18))
    content.pack()
    Label(window, text="Time(in minutes)",font=("Arial", 8)).pack()
    time1 = Entry(window,width=50,font=("arial", 18))
    time1.pack()
    seconds = StringVar()

    setTimer = Button(window, text="Set Timer", padx=25, pady=18,font= ('Poppins bold', 15), command=onClick).pack()

    #keep it running
    window.mainloop()