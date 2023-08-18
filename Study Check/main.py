import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

def fetchdate():
    today = str(date.today())
    newdate = today[-2:]
    return newdate

def storage():
    #storing the data inputted by the user
    with open('data.csv','a') as st: #study hrs data
        st.write(str(f"{studyhrs},\n"))
    
    with open('date.csv','a') as dt: #dates
        dt.write(str(f"{fetchdate()},\n"))

def display():
    hrs_df = pd.read_csv('data.csv')
    date_df = pd.read_csv('date.csv')
    plt.title("Your study hours:")
    plt.xlabel('Date')
    plt.ylabel('Study(in hrs.)')
    plt.plot(date_df,hrs_df,color = 'orange', marker = 'o', markersize = 8, label ='Hours')
    plt.show()


if __name__ == "__main__":
    #user inputs the times he has studied here
    studyhrs = float(input("Enter the no. of hours you've studied\nIn the format [hrs.minutes] strictly.\n"))

    print(f"So...\nYou studied for {studyhrs} hours today? that's great!\n")

    storage()
    display()
