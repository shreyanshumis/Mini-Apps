#A simple CLI based notes app

from datetime import datetime
import os

def datentime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def create():
    print("Enter the file name you want to create!")
    user = input()
    open(f'{user.lower()}.txt','x')

def reading(): #Reading
    print(os.listdir(), "\n Select a File to work on by typing the file name \n")
    user = input()
    try:
        inp = open(f'{user.lower()}.txt','r')
        print("The File content - \n", inp.readlines())
    except:
        print("The file name you entered either does not exist or you entered the name wrong!")
        
def wrapp(): #Writing and append
    print(os.listdir(), "\n Select a File to work on //\n If the file does not exist, then enter a new file name.")
    user = input()
    try:
        inp = open(f'{user.lower()}.txt','a')
        inp.write(datentime())
        while(True):
            lekha = input("You can write whatever you wanted to now! \n To exit, type 'exit\n")
            if lekha == "exit".lower():
                inp.close()
                break
            else:
                inp.write("\n")
                inp.writelines(lekha)
                inp.write("\n")
    except:
        print("The file name you entered either does not exist or you entered the name wrong!")

#main method

if __name__ == "__main__":
    while(True):
        readWriteInp = input("Do you wish to read or write? \n-> Type 'read' to open and read existing notes \n-> 'write' to write new notes \n-> 'create' to add new files \n-> 'close' to close the program. \n")
        if readWriteInp== "read".lower():
            reading()
            continue
        elif readWriteInp== "write".lower():
            wrapp()
            continue
        elif readWriteInp== "create".lower():
            create()
            continue
        elif readWriteInp== "close".lower():
            break
        else:
            print("invalid input")
            continue
