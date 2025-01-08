from tkinter import *
from tkinter import messagebox, ttk
import login_backend
#login page n register page.
class login:
     def __init__(self,window):

        self.window = window
        self.flag = 0

        self.frame = Frame(self.window,bg='Orange',width=700,height=400)  #creating frame

     def loginfn(self):

        self.label = Label(self.frame,text='Log In',bg='Orange',font=('Georgia',36,'bold'))

        self.name = Label(self.frame,text='Enter User_Name: ',bg='Orange',font=('Arial',18,'bold'))

        self.namee_text=StringVar()
        self.namee = Entry(self.frame,textvariable=self.namee_text,fg='gray',width=25,font=('Arial',16,'bold'))

        self.password1 = Label(self.frame,text='Enter Password : ',bg='Orange', fg='Green',font=('Arial',18,'bold'))

        self.password1e_text=StringVar()
        self.password1e = Entry(self.frame,textvariable=self.password1e_text,bg='White',fg='gray',width=25,font=('Arial',16,'bold'),show='*')

        self.buttonlogin = Button(self.frame,text='LOG IN',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.login_admin)


        if self.flag !=0:
            self.buttonAdmin = Button(self.frame,text='Admin',bg='Orange',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.adminbutton2)
        else:
            self.buttonAdmin = Button(self.frame,text='Admin',bg='Orange',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.adminbutton)

        self.buttonStudent = Button(self.frame,text='Student',bg='Orange',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.studentbutton)
	#placing

        self.label.place(x=40,y=40,width=200,height=80)

        self.name.place(x=100,y=140,width=240,height=60)

        self.namee.place(x=380,y=150,width=200,height=30)

        self.password1.place(x=85,y=220,width=240,height=30)

        self.password1e.place(x=380,y=215,width=200,height=30)

        self.buttonAdmin.place(x=320,y=30,width=140,height=50)

        self.buttonStudent.place(x=520,y=30,width=140,height=50)

        self.buttonlogin.place(x=180,y=300,width=140,height=50)

        self.frame.pack()


     def register(self):
         self.buttonAdmin.destroy()
         self.buttonStudent.destroy()
         self.label.destroy()
         self.name.destroy()
         self.namee.destroy()
         self.password1.destroy()
         self.password1e.destroy()
         self.buttonlogin.destroy()
         self.button2.destroy()

         self.labelr = Label(self.frame,text='Register',bg='Orange',font=('Georgia',32,'bold'))

         self.namer = Label(self.frame,text='Name : ',bg='Orange',font=('Arial',14,'bold'))

         self.namere_text=StringVar()
         self.namere = Entry(self.frame,textvariable=self.namere_text,fg='gray')

         self.idr = Label(self.frame,text='Roll No. : ',bg='Orange',font=('Arial',14,'bold'))

         self.rollno_text=StringVar()
         self.idre = Entry(self.frame,textvariable=self.rollno_text,fg='gray',width=25,font=('Arial',12,'bold'))

         self.passwordr1 = Label(self.frame,text='Create Password : ',bg='Orange', fg='Green',font=('Arial',14,'bold'))

         self.passwordr1e_text=StringVar()
         self.passwordr1e = Entry(self.frame,textvariable=self.passwordr1e_text,bg='White',fg='gray',width=25,font=('Arial',12,'bold'),show='*')

         self.passwordr2e_text=StringVar()
         self.passwordr2 = Label(self.frame,text='Reenter Password : ',bg='Orange', fg='Green',font=('Arial',14,'bold'))

         self.passwordr2e = Entry(self.frame,bg='White',fg='gray',width=25,font=('Arial',12,'bold'),show='*')

         self.buttonr = Button(self.frame,text='Register',bg='gray',fg='gray12',font=('Georgia',14,'bold'),cursor='hand2', command = self.create)

         self.buttonr2 = Button(self.frame,text='Back',bg='gray',fg='gray12',font=('Georgia',14,'bold'),cursor='hand2',  command= self.destroy)


         #placing
         self.labelr.place(x=40,y=10,width=200,height=80)

         self.namer.place(x=80,y=100,width=240,height=60)

         self.namere.place(x=300,y=115,width=200,height=30)

         self.idr.place(x=70,y=150,width=240,height=60)

         self.idre.place(x=300,y=165,width=200,height=30)

         self.passwordr1.place(x=28,y=210,width=240,height=30)

         self.passwordr1e.place(x=300,y=210,width=200,height=30)

         self.passwordr2.place(x=23,y=253,width=240,height=30)

         self.passwordr2e.place(x=300,y=253,width=200,height=30)

         self.buttonr.place(x=160,y=330,width=140,height=50)

         self.buttonr2.place(x=320,y=330,width=140,height=50)

     def create(self):
         if self.passwordr1e.get() != self.passwordr2e.get():
             messagebox.showinfo('error','Passwords do not match')
         elif len(self.namere.get()) == 0:
             messagebox.showinfo('error', 'Name field is empty')
         elif len(self.idre.get()) == 0:
            messagebox.showinfo('error', 'ID field is empty')
         elif len(self.passwordr1e.get()) == 0:
               messagebox.showinfo('error', 'PASSWORD field is empty')

         else:
             login_backend.insert(self.rollno_text.get(),self.namere_text.get(),self.passwordr1e_text.get())



     def adminbutton2(self):
        #z =button2.winfo_exists()
        #if z==1:
        self.button2.destroy()
        #messagebox.showinfo('<title>','<show>')
        self.name = Label(self.frame,text='Enter User_Name: ',bg='Orange',font=('Arial',18,'bold'))
        self.name.place(x=100,y=140,width=240,height=60)

     def adminbutton(self):
        self.name = Label(self.frame,text='Enter User_Name: ',bg='Orange',font=('Arial',18,'bold'))
        self.name.place(x=100,y=140,width=240,height=60)


     def studentbutton(self):
        self.flag =1
        self.buttonlogin.destroy()
        self.buttonlogin = Button(self.frame,text='LOG IN',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.login_student)
        self.buttonlogin.place(x=180,y=300,width=140,height=50)

        self.name = Label(self.frame,text='Enter Name: ',bg='Orange',font=('Arial',18,'bold'))
        self.name.place(x=100,y=140,width=240,height=60)
        self.button2 = Button(self.frame,text='SIGN UP',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.register)
        self.button2.place(x=340,y=300,width=140,height=50)

     def login_admin(self):
         if len(self.namee.get()) ==0:
                    messagebox.showinfo("ERROR", "Mendatory Field is empty")
         elif  len(self.password1e.get()) == 0:
                 messagebox.showinfo("ERROR", "Mendatory Field is empty")
         else:
             login_backend.check(self.namee_text.get(),self.password1e_text.get())

     def login_student(self):
          if len(self.namee.get()) ==0:
                     messagebox.showinfo("ERROR", "Mendatory Field is empty")
          elif  len(self.password1e.get()) == 0:
                  messagebox.showinfo("ERROR", "Mendatory Field is empty")
          else:
              login_backend.checks(self.namee_text.get(),self.password1e_text.get())

     def destroy(self):
         self.labelr.destroy()
         self.namer.destroy()
         self.namere.destroy()
         self.idr.destroy()
         self.idre.destroy()
         self.passwordr1.destroy()
         self.passwordr1e.destroy()
         self.passwordr2.destroy()
         self.passwordr2e.destroy()
         self.buttonr.destroy()
         self.buttonr2.destroy()
         self.buttonlogin.destroy()

         self.loginfn() #calling the loginfn function


#creating the window
window = Tk()
window.title('Login')
window.geometry('700x400')
#creating object to login class
obj = login(window)
obj.loginfn()
window.mainloop()


import sqlite3
from tkinter import *
from admin.py import admin # type: ignore
from student.py import student  # type: ignore

def connect():
    conn=sqlite3.connect("login.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists user(roll no INTEGER PRIMARY KEY,name text,password text)")
    #cur.execute("drop table user")
    #ek admin table create kar isme 'admin' following by adding the entries,by applying same procedure done to add some entries in user table,
    #before that replace user by admin in the 'insert' function.after adding up the entries roll back the changes.
    conn.commit()
    conn.close()

def insert(rollno,name,password):
    conn=sqlite3.connect('login.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO user VALUES(?,?,?)',(rollno,name,password))
    conn.commit()
    conn.close()

def check(name,password):
    conn=sqlite3.connect('login.db')
    cur = conn.cursor()
    if   (cur.execute('SELECT * FROM admin WHERE name =? AND password = ?',(name,password))):
        if cur.fetchone():
            window = Tk()
            window.title('Admin_User')
            window.geometry('700x450')
            obj=admin(window)
            window.mainloop()
        else:
            messagebox.showinfo('error','INVALID CREDENTIALS for ADMIN LOGIN')

def checks(name,password):                       # for student login
    conn=sqlite3.connect('login.db')
    cur = conn.cursor()
    if   (cur.execute('SELECT * FROM user WHERE name = ? AND password = ?', (name, password))):
        if cur.fetchone():
            window = Tk()
            window.title('Student_User')
            window.geometry('700x400')
            obj = student(window)
            window.mainloop()
        else:
            messagebox.showinfo('error','INVALID CREDENTIALS for STUDENT LOGIN')


    conn.commit()
    conn.close()

connect()



import sqlite3
from tkinter import *
from tkinter import messagebox
from admin.py import admin # type: ignore
from student.py import student # type: ignore

def connect():
    conn=sqlite3.connect("login.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists user(roll no INTEGER PRIMARY KEY,name text,password text)")
    #cur.execute("drop table user")
    # create table 'admin' add some entries in it, by applying same procedure done to add some entries in user table,
    # before that replace user by admin in the 'insert' function . After adding up the entries roll back the changes.
    conn.commit()
    conn.close()

def insert(rollno,name,password):
    conn=sqlite3.connect('login.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO user VALUES(?,?,?)',(rollno,name,password))
    conn.commit()
    conn.close()

def check(name,password):
    conn=sqlite3.connect('login.db')
    cur = conn.cursor()
    if   (cur.execute('SELECT * FROM admin WHERE name =? AND password = ?',(name,password))):
        if cur.fetchone():
            window = Tk()
            window.title('Admin_User')
            window.geometry('700x450')
            obj= admin(window)
            window.mainloop()
        else:
            messagebox.showinfo('error','INVALID CREDENTIALS for ADMIN LOGIN')

def checks(name,password):                       # student login ke liye
    conn=sqlite3.connect('login.db')
    cur = conn.cursor()
    if   (cur.execute('SELECT * FROM user WHERE name = ? AND password = ?', (name, password))):
        if cur.fetchone():
            window = Tk()
            window.title('Student_User')
            window.geometry('700x400')
            obj = student(window)
            window.mainloop()
        else:
            messagebox.showinfo('error','INVALID CREDENTIALS for STUDENT LOGIN')


    conn.commit()
    conn.close()

connect()


from tkinter import *
import backend

class admin:
        def __init__(self,window):
            self.window = window

            self.frame = Frame(self.window, bg = 'orange', width=800,height=450)

            self.frame.pack()

            self.label = Label(self.frame,text='Admin User',bg='Orange',font=('Georgia',30,'bold'))
            self.label.place(x=20,y=20,width=400,height=50)

            self.label_title = Label(self.frame, text='TITLE',bg='orange',font=('Georgia',14,'bold'))
            self.label_title.place(x=20,y=100,width=100,height=50)

            self.label_year = Label(self.frame, text='YEAR',bg='orange',font=('Georgia',14,'bold'))
            self.label_year.place(x=20,y=150,width=100,height=30)

            self.label_author = Label(self.frame, text='AUTHOR',bg='orange',font=('Georgia',14,'bold'))
            self.label_author.place(x=350,y=100,width=100,height=30)

            self.label_isbn = Label(self.frame, text='ISBN',bg='orange',font=('Georgia',14,'bold'))
            self.label_isbn.place(x=350,y=150,width=100,height=30)

            self.title_text=StringVar()
            self.entry_title = Entry(self.frame, fg='gray',textvariable=self.title_text,width=25,font=('Arial',12,'bold'))
            self.entry_title.place(x=120,y=100,width=150,height=30)

            self.year_text=StringVar()
            self.entry_year = Entry(self.frame, fg='gray',textvariable=self.year_text,width=25,font=('Arial',12,'bold'))
            self.entry_year.place(x=120,y=150,width=150,height=30)

            self.author_text=StringVar()
            self.entry_author = Entry(self.frame, fg='gray',textvariable=self.author_text,width=25,font=('Arial',12,'bold'))
            self.entry_author.place(x=470,y=100,width=150,height=30)

            self.isbn_text=StringVar()
            self.entry_isbn = Entry(self.frame, fg='gray',textvariable=self.isbn_text,width=25,font=('Arial',12,'bold'))
            self.entry_isbn.place(x=470,y=150,width=150,height=30)

            self.listbox = Listbox(self.frame)
            self.listbox.place(x=100,y=200,width=500,height=100)

            self.button_view = Button(self.frame,text='View All', command=self.view_command)
            self.button_view.place(x=100,y=320,width=100,height=40)

            self.button_search = Button(self.frame,text='Search ', command=self.search_command)
            self.button_search.place(x=200,y=320,width=100,height=40)

            self.button_add = Button(self.frame,text='Add entry', command=self.add_command)
            self.button_add.place(x=300,y=320,width=100,height=40)

            self.button_update = Button(self.frame, text='Update entry', command=self.update_command)
            self.button_update.place(x=400, y=320,width=100,height=40)

            self.button_delete = Button(self.frame, text='Delete entry', command=self.delete_command)
            self.button_delete.place(x=500, y=320,width=100,height=40)

            self.button_issue = Button(self.frame, text='Clear Fields', command=self.clear_command)
            self.button_issue.place(x=100, y=360,width=100,height=40)

            self.button_request = Button(self.frame, text='Requested Books', command=self.requestsearch_command)
            self.button_request.place(x=300, y=360,width=100,height=40)

            self.button_issue = Button(self.frame, text='Issued Books', command=self.issuesearch_command)
            self.button_issue.place(x=500, y=360,width=100,height=40)


        def destroy(self):
            self.button_issuedelete.destroy()
            self.button_requestdelete.destroy()

        def clear_command(self):
            self.entry_title.delete(0,END)
            self.entry_year.delete(0,END)
            self.entry_author.delete(0,END)
            self.entry_isbn.delete(0,END)

        def issuedelete_command(self):
            selected_tuple=self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            backend.issue_delete(value[0])
            self.entry_title.delete(0,END)
            #self.entry_title.insert(END,value[1])
            self.entry_year.delete(0,END)
            #self.entry_year.insert(END,value[3])
            self.entry_author.delete(0,END)
            #self.entry_author.insert(END,value[2])
            self.entry_isbn.delete(0,END)
            #self.entry_isbn.insert(END,value[4])

        def issuesearch_command(self):
            self.listbox.delete(0,END) # it will empty the list every time it is called
            for row in backend.issue_view(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
                self.listbox.insert(END,row)

            self.button_issuedelete = Button(self.frame, text='Book Returned', command=self.issuedelete_command)
            self.button_issuedelete.place(x=400, y=360,width=100,height=40)

        def requestsearch_command(self):
            self.listbox.delete(0,END)
            for row in backend.request_view(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
                self.listbox.insert(END,row)

            self.button_requestdelete = Button(self.frame, text='Request Listened', command=self.requestcomplete_command)
            self.button_requestdelete.place(x=200, y=360,width=100,height=40)

        def requestcomplete_command(self):
            selected_tuple=self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            backend.request_delete(value[0])
            self.entry_title.delete(0,END)
            #self.entry_title.insert(END,value[0])
            self.entry_year.delete(0,END)
            #self.entry_year.insert(END,value[2])
            self.entry_author.delete(0,END)
            #self.entry_author.insert(END,value[1])
            self.entry_isbn.delete(0,END)
            #self.entry_isbn.insert(END,value[3])

        def view_command(self):
            self.listbox.delete(0,END)
            for row in backend.view():
                self.listbox.insert(END,row) # END ensures that every new entry is stored at end of the all rows
            self.destroy()

        def search_command(self):
            self.listbox.delete(0,END)
            for row in backend.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
                self.listbox.insert(END,row)
                self.destroy()

        def add_command(self):
            backend.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            self.listbox.delete(0,END)
            self.listbox.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))
            self.destroy()

        def delete_command(self):
            selected_tuple=self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            backend.delete(value[0])    # i have to use value[0] here or at backend use id[0]
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,value[1])
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,value[3])
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,value[2])
            self.entry_isbn.delete(0,END)
            self.entry_isbn.insert(END,value[4])
            self.destroy()

        def update_command(self):
            selected_tuple=self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,value[0])
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,value[2])
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,value[1])
            self.entry_isbn.delete(0,END)
            self.entry_isbn.insert(END,value[3])
            backend.update(value[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())

'''
window = Tk()
window.title('Admin_User')
window.geometry('700x450')
obj = admin(window)
window.mainloop()'''


from tkinter import *
from tkinter import ttk, messagebox
import backend

class student:
        def __init__(self,window):
            self.window = window

            self.frame = Frame(self.window, bg = 'orange', width=700,height=400)

            self.label = Label(self.frame,text='Student User',bg='Orange',font=('Georgia',30,'bold'))
            self.label.place(x=20,y=20,width=400,height=50)

            self.label_title = Label(self.frame, text='TITLE',bg='orange',font=('Georgia',14,'bold'))
            self.label_title.place(x=20,y=100,width=100,height=50)

            self.label_year = Label(self.frame, text='YEAR',bg='orange',font=('Georgia',14,'bold'))
            self.label_year.place(x=20,y=150,width=100,height=30)

            self.label_author = Label(self.frame, text='AUTHOR',bg='orange',font=('Georgia',14,'bold'))
            self.label_author.place(x=350,y=100,width=100,height=30)

            self.label_isbn = Label(self.frame, text='ISBN',bg='orange',font=('Georgia',14,'bold'))
            self.label_isbn.place(x=350,y=150,width=100,height=30)

            self.title_text=StringVar()
            self.entry_title = Entry(self.frame, fg='gray',textvariable=self.title_text,width=25,font=('Arial',12,'bold'))
            self.entry_title.place(x=120,y=100,width=150,height=30)

            self.year_text=StringVar()
            self.entry_year = Entry(self.frame, fg='gray',textvariable=self.year_text,width=25,font=('Arial',12,'bold'))
            self.entry_year.place(x=120,y=150,width=150,height=30)

            self.author_text=StringVar()
            self.entry_author = Entry(self.frame, fg='gray',textvariable=self.author_text,width=25,font=('Arial',12,'bold'))
            self.entry_author.place(x=470,y=100,width=150,height=30)

            self.isbn_text=StringVar()
            self.entry_isbn = Entry(self.frame, fg='gray',textvariable=self.isbn_text,width=25,font=('Arial',12,'bold'))
            self.entry_isbn.place(x=470,y=150,width=150,height=30)

            self.listbox = Listbox(self.frame)
            self.listbox.place(x=100,y=200,width=500,height=100)

            self.button_view = Button(self.frame,text='View All', command=self.view_command)
            self.button_view.place(x=100,y=320,width=100,height=40)

            self.button_search = Button(self.frame,text='Search ', command=self.search_command)
            self.button_search.place(x=200,y=320,width=100,height=40)

            self.button_issue = Button(self.frame,text='Issue', command=self.issue_command)
            self.button_issue.place(x=300,y=320,width=100,height=40)

            self.button_request = Button(self.frame, text='Request', command = self.request_command)
            self.button_request.place(x=400, y=320,width=100,height=40)

            self.button_issue = Button(self.frame, text='Clear Fields', command=self.clear_command)
            self.button_issue.place(x=500, y=320,width=100,height=40)

            self.frame.pack()

        def clear_command(self):
            self.entry_title.delete(0,END)
            self.entry_year.delete(0,END)
            self.entry_author.delete(0,END)
            self.entry_isbn.delete(0,END)

        def request_command(self):
            backend.request_insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            self.listbox.delete(0,END)
            self.listbox.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

        def issue_command(self):
            selected_tuple=self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,value[1])
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,value[2])
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,value[3])
            self.entry_isbn.delete(0,END)
            self.entry_isbn.insert(END,value[4])
            backend.issue_insert(value[0])

        def view_command(self):
            self.listbox.delete(0,END)
            for row in backend.view():
                self.listbox.insert(END,row)

        def search_command(self):
            self.listbox.delete(0,END)
            for row in backend.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
                self.listbox.insert(END,row)

        def add_command(self):
            backend.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            self.listbox.delete(0,END)
            self.listbox.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

        def delete_command(self):
            selected_tuple=self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,value[1])
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,value[2])
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,value[3])
            self.entry_isbn.delete(0,END)
            self.entry_isbn.insert(END,value[4])
            backend.delete(value[0])

        def update_command(self):
            selected_tuple=self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,value[0])
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,value[1])
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,value[2])
            self.entry_isbn.adelete(0,END)
            self.entry_isbn.insert(END,value[3])
            backend.update(value[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
'''
window = Tk()
window.title('Student_User')
window.geometry('700x400')
obj = student(window)
window.mainloop()'''