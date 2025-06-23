
import mysql.connector as mysql
db = mysql.connect(host="localhost",user="root",password="root",database="college")
cmdd = db.cursor()

def teacherlayout():
    while 1: #This is what the teacher will be able to see
        print("=================================")
        print("Teacher's Menu")
        print("1. Mark student attendance")
        print("2. View")
        print("3. Logout")
        print("=================================")

        opt = input(str("Option : ")) 
        if opt == "1":
            print("=================================")
            print("Mark student attendance")
            cmdd.execute("SELECT username FROM users WHERE privilege = 'student'")
            recs = cmdd.fetchall()
            date = input(str("Date : DD/MM/YYYY : "))
            for rec in recs:
                rec = str(rec).replace("'","")
                rec = str(rec).replace(",","")
                rec = str(rec).replace("(","")
                rec = str(rec).replace(")","") 
                status = input(str("Status for " + str(rec) + " Present or Abesnt :")) #The teacher can input P or A for present or absent
                val = (str(rec),date,status)
                cmdd.execute("INSERT INTO attendance (username, date, status) VALUES(%s,%s,%s)",val)
                db.commit()
                print(rec + " Marked as " + status)
        elif opt == "2":
            print("=================================")
            print("Viewing all student registers")
            cmdd.execute("SELECT username, date, status FROM attendance")
            recs = cmdd.fetchall()
            print("Displaying all registers")
            for rec in recs:
                print(rec)
        elif opt == "3":
            print ("Logging out. . .")
            print ("You have been successfully logged out!")
            break
        else:
            print("Invalid option.")


def adminlayout():
    while 1:
        print("=================================")
        print("Admin Menu")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. Logout")
        print("=================================")

        opt = input(str("Option : "))
        if opt == "1":
            print("=================================")
            print("Register New Student")
            username = input(str("Student username : "))
            password = input(str("Student password : "))
            val = (username,password) #takes in username and password
            cmdd.execute("INSERT INTO users (username,password,privilege) VALUES (%s, %s,'student')",val)
            db.commit() #saves changes to the database
            print(username + " has been registered as a student!")
        elif opt == "2":
            print("=================================")
            print("Register New Teacher")
            username = input(str("Teacher username : "))
            password = input(str("Teacher password : "))
            val = (username,password) #takes in username and password
            cmdd.execute("INSERT INTO users (username,password,privilege) VALUES (%s, %s,'teacher')",val)
            db.commit()
            print(username + " has been registered as a teacher!")
        elif opt == "3":
            print("=================================")
            print("Delete Existing student account")
            username = input(str("Student username : "))
            val=(username,"student") #takes in username of the student
            cmdd.execute("DELETE FROM users WHERE username = %s AND privilege = %s",val) #deletes the user(student)
            db.commit()
            if cmdd.rowcount <1: #Incase the wrong value is entered
                print("User not found")
            else:
                print(username + " has been deleted")
        elif opt == "4":
            print("=================================")
            print("Delete Existing Teacher account")
            username = input(str("Teacher username : "))
            val=(username,"Teacher") #takes in username of the teacher
            cmdd.execute("DELETE FROM users WHERE username = %s AND privilege = %s",val) #deletes the user(teacher)
            db.commit()
            if cmdd.rowcount <1: #Incase the wrong value is entered
                print("User not found")
            else:
                print(username + " has been deleted")
        elif opt == "5":
            break
        else:
            print("Invalid option")

def teacher_authorisation():
    print("=================================")
    print("Teacher's login")
    print("=================================")
    username = input(str("Username : "))
    password = input(str("Password : "))
    teacherlayout()

def admin_authorisation():
    print("=================================")
    print("Admin login")
    print("=================================")
    username = input(str("Username : ")) #String input for username
    password = input(str("Password : ")) #String input for password
    if username == "admin": #username of the administrator
        if password == "password": #password for administrator
            adminlayout()
        else:
            print("Incorrect password!")
    else:
        print("Not found..")

def main(): #main method
    while 1:
        print("WELCOME TO THE COLLEGE MANAGEMENT") #welcome message
        print("=================================")
        print("1. Teacher") #press 1 for teacher login
        print("2. Admin") #press 2 for Administrator/Moderator login
        print("=================================")
        opt = input(str("Option :"))
        if opt=="1":
            teacher_authorisation()
        elif opt=="2":
            admin_authorisation() #verifies if the person logging is the admin or not
        else:
            print("Invalid option.")

main() #method calling