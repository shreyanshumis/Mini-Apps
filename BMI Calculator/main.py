from tkinter import *

def onClick():
    weight = float(wt.get())
    height = float(ht.get())
    bmi = weight/pow((height/100),2) #bmi formula
    disp = Label(window, text = f"Your BMI is: {bmi}").pack() #Result display

#window
window =Tk()
window.title("BMI Calculator")
window.geometry('500x300')

#labels
bmiTitle = Label(window, text= "Calculate your BMI").pack()

header = Label(window, text="Enter Weight(in kg) and Height(in cm.)").pack()

wt = Entry(window)
wt.pack()
ht = Entry(window)
ht.pack()
bmi = StringVar()

#BUttons 
MyButton = Button(window, text="Calculate", padx=25, pady=10, command=onClick).pack()


#run
window.mainloop()