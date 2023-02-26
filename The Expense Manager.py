import tkinter as tk                 #importing  Modules
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
import mysql.connector as exp
from mysql.connector import Error
from pandas import DataFrame
from tkinter import messagebox
import center_tk_window
#=====================================================================================================================================================================================
create=open("Password.txt","a+")
create.close()
create=open("Userdetails.txt","a+")
create.close()
good=open("Password.txt")           #opening files to save required password and other
batman=good.readline()
good.close()
good12=open("Userdetails.txt")
batman1=good12.readline()
good12.close()
#===================================================================================================================================
list1=[]#presence of table          #Create an empty list to use it to find the presence of table and Frame3 and for sub category
list2=[]#presence of frame3
list3=[]#creating sub category
#===================================================================================================
def createusers3():
    root9.destroy()
    createusers()
def createusers():                  #sign in window Function
    root7=tk.Tk()
    root7.title("Sign in")
    root7.iconbitmap('sat1.ico')
    root7.geometry('230x250')
    root7.resizable(0,0)
    center_tk_window.center_on_screen(root7)
    frame23=tk.Frame(root7,bg="pale green")
    frame23.place(relheight=1,relwidth=1)
    label4=tk.Label(frame23,text="Create username",bg="SpringGreen4",fg="snow",font=('Times',17,'bold'),relief=RAISED,bd=3)
    label4.pack(pady=5)
    entry7=tk.Entry(frame23,font=('Times',12,'bold'))
    entry7.pack(pady=2)
    label14=tk.Label(frame23,text="Create password",bg="SpringGreen4",fg="snow",font=('Times',17,'bold'),relief=RAISED,bd=3)
    label14.pack(pady=5)
    entry17=tk.Entry(frame23,font=('Times',12,'bold'))
    entry17.pack(pady=2)
    label14=tk.Label(frame23,text="Confirm password",bg="SpringGreen4",fg="snow",font=('Times',17,'bold'),relief=RAISED,bd=3)
    label14.pack(pady=5)
    entry18=tk.Entry(frame23,font=('Times',12,'bold'),show="*")
    entry18.pack(pady=2)
    def info():
        messagebox.showinfo("info", "The Password Must Contain Atleast one \nSpecial character,Digit,UpperCase\n And strength must be atleast 8")
    entry18.after(200,info)
    def safe():
        usr=entry7.get()
        v=0
        for i in usr:
            if i.isalnum()==False:
                v+=1    
        if usr=="":
            msg=messagebox.showwarning("Warning", "Username Must Be Provided to Proceed Further")
        elif v>0:
            msg=messagebox.showwarning("Warning", "Username should not contain special characters ")      
        else:
            paswd=entry17.get()
            e=0
            d=0
            u=0
            s=0
            j=0
            for i in paswd:
                    j+=1
                    if i.isdigit()==True:
                            d+=1        
                    if i.isupper()==True:
                            u+=1
                    if i.isalnum()==False:
                            s+=1
            if j<8:
                    msg=messagebox.showwarning("Warning", "Password must contain atleast 8 charcters")
            else:
                if d==0:
                    msg=messagebox.showwarning("Warning", "Password must contain atleast 1 digit")
                else:
                    if u==0:
                        msg=messagebox.showwarning("Warning", "Password must contain atleast 1 UpperCase Charcter")
                    else:
                        if s==0:
                            msg=messagebox.showwarning("Warning", "Password must contain atleast 1 Special Charcter")
                        else:
                            if j>=8 and d!=0 and u!=0 and s!=0:
                                save()
    def save():
        en7=entry7.get()
        en17=entry17.get()
        en18=entry18.get()
        if en17!=en18:
            messagebox.showwarning("Warning", "Password Not Matching")
        elif en17==en18:
            opener=open("Userdetails.txt")
            data=opener.readlines()
            opener.close()
            de=en7+'\t'+en17+'\n'
            de3=en7+'\t'+en17
            if len(data)>1:
                d5=data[-1]
                d24=d5.split("\t")
                d4=d24[0]
                for i in data:
                    if i!="\n":
                        d1=i.split("\t")
                        d2=d1[0]
                        if d2==en7:
                            msg=messagebox.showwarning("Warning", "The User Name already Present Must be unique")
                        elif d2==d4:
                            if data[-1]!=d2:
                                question=messagebox.askquestion("INFO", "Kindly Note That Your Password and Username\n\n will Be Saved in the Folder Named \"Userdetails.txt\"\n\n Are You Sure?")
                                if question=="yes":
                                    userdetails=open("Userdetails.txt","a+")
                                    userdetails.write('\n')
                                    userdetails.write(en7)
                                    userdetails.write('\t')
                                    userdetails.write(en17)
                                    userdetails.close()
                                    root7.withdraw()
                                    program()
            else:
                question=messagebox.askquestion("INFO", "Kindly Note That Your Password and Username\n\n will Be Saved in the Folder Named \"Userdetails.txt\"\n\n Are You Sure?")
                if question=="yes":
                    userdetails=open("Userdetails.txt","a+")
                    userdetails.write('\n')
                    userdetails.write(en7)
                    userdetails.write('\t')
                    userdetails.write(en17)
                    userdetails.close()
                    root7.withdraw()
                    program()
    button9=tk.Button(frame23,text="confirm",command=safe,bg="SpringGreen4",fg="snow",relief=RAISED,bd=3)
    button9.pack(pady=3)
#===========================================================================================================
if batman=='':                     #following lines for saving the Mysql Password from user for future executions
    rooter=tk.Tk()
    rooter.geometry("275x120")
    rooter.resizable(0,0)
    rooter.title("Expense Manager")
    rooter.iconbitmap('sat1.ico')
    center_tk_window.center_on_screen(rooter)
    frame343=tk.Frame(rooter,bg="pale green")
    frame343.place(relwidth=1,relheight=1)
    label=Label(frame343,text="Enter MySql Password",font=('Times',15,'bold'), fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
    label.pack(pady=5)
    e = Entry(frame343,show="*",font=('Times',13,'bold'),bd=4)
    e.pack(padx=5,pady=1)
    def connecter():
        en2=e.get()
        if en2=='':
            messagebox.showwarning("Warning", "Password Must Be Provided\n To Proceed Further")
        else:
            try:
                mydb1=exp.connect(host='localhost',user='root',passwd=en2)
                if mydb1.is_connected():
                    question=messagebox.askquestion("INFO", "Kindly Note That Your Password is Saved in the Folder Named \"Password.txt\"\n\n Are You Sure?")
                    if question=="yes":
                        password=open("Password.txt","w")
                        password.write(en2)
                        password.close()
                        rooter.withdraw()
                        createusers()
            except Error:
                messagebox.showwarning("Warning", "Enter the Valid Mysql Password to Continue")
        
    b = Button(frame343, text="Confirm Password",fg='snow',font=('Times',13,'bold'),relief=RAISED, bd=4, bg='SpringGreen4', command=connecter)
    b.pack(pady=5)
#==========================================================================================================================================================================
def program():                      #following Function "Program" is the Body of the Expense Manager, it connects the python with mysql     
    good1=open("Password.txt")
    batman=good1.readline()
    good1.close()
    good12=open("Userdetails.txt")
    batman1=good12.readlines()
    good12.close()
    if batman!='' and batman1!='':
        root342=tk.Tk()
        root342.iconbitmap('sat1.ico')
        root342.withdraw()
        global root9
#=============================Login window======================================================
        root9=tk.Tk()                  #It opens on every execution to ensure the privacy and security of user
        root9.resizable(0,0)
        root9.iconbitmap('sat1.ico')
        root9.title("Login")
        center_tk_window.center_on_screen(root9)
        frame23=tk.Frame(root9,bg="pale green")
        frame23.place(relheight=1,relwidth=1)
        label4=tk.Label(frame23,text="Enter Username",bg="SpringGreen4",fg="snow",font=('Times',17,'bold'),relief=RAISED,bd=3)
        label4.pack(pady=5)
        entry71=tk.Entry(frame23,font=('Times',12,'bold'))
        entry71.pack(padx=1)
        label14=tk.Label(frame23,text="Enter Password",bg="SpringGreen4",fg="snow",font=('Times',17,'bold'),relief=RAISED,bd=3)
        label14.pack(pady=5)
        entry171=tk.Entry(frame23,font=('Times',12,'bold'),show="*")
        entry171.pack(pady=1)
        def user():
            f=open("Userdetails.txt")
            d=f.readlines()
            d.remove("\n")
            userdetails=[]
            user=entry71.get()
            passw=entry171.get()
            username=''
            for i in d:
                s=i.split("\t")
                w=s[1].split("\n")
                userdetails.append(s[0])
                userdetails.append(w[0])
            if user=='':
                messagebox.showwarning("Warning", "Invalid Username")
            elif user in userdetails:
                d=userdetails.index(user)
                if passw==userdetails[d+1]:
                    username+=user
                elif passw=='':
                    messagebox.showwarning("Warning", "Empty Password Not Accepted")
                else:
                    messagebox.showwarning("Warning", "Invalid password for the Username: "+user)
                if batman!='' and username!='':
                    root9.withdraw()
                    root5=tk.Tk()                  #Creating The Main Window
                    root5.withdraw()
                    root=tk.Toplevel()
                    root.title("Expense Manager")
                    root.geometry('1159x600')
                    root.resizable(0,0)
                    root.iconbitmap('sat1.ico')
                    center_tk_window.center_on_screen(root)
                    notebook=ttk.Notebook(root)
                    notebook.place(relwidth=1,relheight=1)
                    frame=tk.Frame(root)
                    frame.place(relwidth=1, relheight=1)
                    frame8=tk.Frame(notebook)
                    frame8.place(relwidth=1, relheight=1)
                    frame7=tk.Frame(notebook)
                    frame7.place(relheight=1,relwidth=1)
                    notebook.add(frame,text="MANAGER")
                    notebook.add(frame8,text="HELP")
                    notebook.add(frame7,text="REPORT")
                    en1=batman                    
                    import mysql.connector as exp              #Connectivity with Mysql
                    mydb=exp.connect(host="localhost",user="root",passwd=en1)
                    cursor= mydb.cursor()
                    cursor.execute("create database if not exists "+username)
                    mydb.commit()
                    mydb=exp.connect(host="localhost",user="root",passwd=en1,database=username)
                    cursor= mydb.cursor()
                    maincatgs=["Expense","Vehicle_Maintenance","Children","Food","Network","Energy","House","Insurance",
                               "Loan","Personal_Care","Pet","Taxes","Travel","Miscellaneous"]
                    for i in maincatgs:
                        insert="create table if not exists "+i+"(Date varchar(30),Category varchar(30),Expense float(13,3),Description varchar(100))"
                        cursor.execute(insert)
                        mydb.commit()
                        cursor.execute("create table if not exists budget(budget float(13,3))")
                        mydb.commit()
                    mydb=exp.connect(host="localhost",user="root",passwd=en1,database=username)
                    cursor= mydb.cursor()
#=======================Expense Categories======================================================================================================================================================================
                    maincatgs=["Vehicle_Maintenance","Children","Food","Network","Energy","House","Insurance",
                               "Loan","Personal_Care","Pet","Taxes","Travel","Miscellaneous"]
                    Vehicle_Maintenance=['Car Maintenance','Fuel','2 Wheeler Repair']
                    Children=['Toys','School Supplies','Educational Fees']
                    Food=['Grocery','Vegetables','Fruits','Meat']
                    Network=['Internet','Telephone','Mobile','Television']
                    Energy=['Gas','Electricity']
                    House=['Water','Maintenance','Maid','Appliances','Gadgets']
                    Insurance=['Health Insurance','House Insurance','Life Insurance']
                    Loan=['Vehicle Loan','House Loan']
                    Personal_Care=['Clothing','Medical','Parlour','Dry Cleaning']
                    Pet=['PetFood','Grooming','Vet']
                    Taxes=['Property tax','Income tax']
                    Travel=['Accomodation','Restaurent','Transportation','Tourism']
                    months={'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
                    flood={"Vehicle_Maintenance":Vehicle_Maintenance,'Children':Children,'Food':Food,'Network':Network,'Energy':Energy,'House':House,'Insurance':Insurance,'Loan':Loan,'Personal_Care':Personal_Care,'Pet':Pet,'Taxes':Taxes,'Travel':Travel}
#============================================================================================================================================================================================
                    canvas1= Canvas(frame8,width=600,heigh=400,bg="white")     #Adding User guide 
                    canvas1.place(relheight=1,relwidth=1)
                    img1=Image.open("help.png")
                    img1=img1.resize((1155,575))
                    img1 = ImageTk.PhotoImage(img1)
                    canvas1.create_image(0,0,anchor=NW, image=img1)
#==============================================================================================
                    canvas = Canvas(frame,width=600,heigh=400,bg="white")      #Adding Background Image 
                    canvas.place(relheight=1,relwidth=1)
                    img=Image.open("saving.png")
                    img=img.resize((1158,600))
                    img = ImageTk.PhotoImage(img)
                    canvas.create_image(0,0,anchor=NW, image=img)
                    d5=tk.Label(frame,text="Welcome To The Expense Mananger",bg="SpringGreen4",fg="ghost white",font=('Times',17,'bold'),relief=RAISED,bd=4)
                    d5.place(relx=0.15,rely=0.01)
#===========================================================================================================================================================================================================================
                    enor2=ttk.Combobox(frame,value=maincatgs)
                    enor2.place(relwidth=0.2, relheight=0.05, relx=0.15,rely=0.15)
                    def closer():
                        frame2.destroy()
                        buttoner.destroy()
                        global list1
                        list1.remove(0)
                        global list2
                        if list2!=[]:
                            list2.remove(0)
                    def inserting_by_category():
                        c=enor2.get()
                        g=[]
                        for i in flood:
                            if i==c:
                                f=flood[i]
                                for j in f:
                                    g.append(j)
                            if c=='Miscellaneous':
                                cursor.execute("select distinct category from Miscellaneous")
                                data3=cursor.fetchall()
                                g=[]
                                for i in data3:
                                    r=i[0]
                                    g.append(r)
                        if c in maincatgs:
                            global enor3
                            enor3=ttk.Combobox(frame,value=g)
                            enor3.place(relwidth=0.2, relheight=0.05,  relx=0.15,rely=0.27)
                            global list3
                            list3.append(0)
#================================================================================================================================================================================================================
                    def inserting_into_tables(dis="Not Provided"):
                        for e in range(1):
                            global list3
                            s=enor.get()
                            ex=enor1.get()
                            maincat=enor2.get()
                            if s=='':
                                messagebox.showwarning("Warning", "Date not Provided")
                            elif maincat=='':
                                messagebox.showwarning("Warning", "MainCategory Not Selected")
                            elif list3==[]:
                                messagebox.showwarning("Warning", "Main category Not Confirmed")
                            elif ex=='':
                                messagebox.showwarning("Warning", "Expense Not Provided")
                            else:
                                sub=enor3.get()
                                if sub=='':
                                    messagebox.showwarning("Warning", "Subgategory Not Provided")
                                else:
                                    d1=s[0:2]
                                    m1=s[3:5]
                                    y1=s[6:]
                                    dl=[]
                                    if len(s)!=10:
                                        messagebox.showwarning("Warning", "Entered Date Not in \"dd-mm-yyyy\" format")
                                    elif d1.isdigit()==False or m1.isdigit()==False:
                                        messagebox.showwarning("Warning", "Unexpected Value Identified in Date")
                                    elif y1.isdigit()==False:
                                        messagebox.showwarning("Warning", "Unexpected Value Identified in Date")
                                    elif int(m1)>12 or int(m1)<1:
                                        messagebox.showwarning("Warning", "Month not in Range")
                                    elif int(m1) in [1,3,5,7,8,10,12]:
                                        if int(d1)>31 or int(d1)<0:
                                            messagebox.showwarning("Warning", "Date not in Range for the Provided Month")
                                        else:
                                            dl.append(1)
                                    elif int(m1) not in [1,3,5,7,8,10,12]:
                                        if int(m1)==2:
                                            if int(y1)%4==0:
                                                if int(d1)>29 or int(d1)<1:
                                                    messagebox.showwarning("Warning", "Date not in Range for the Provided Month")
                                                else:
                                                    dl.append(1)                                    
                                            else:
                                                if int(d1)>28 or int(d1)<1:
                                                    messagebox.showwarning("Warning", "Date not in Range for the Provided Month")
                                                else:
                                                    dl.append(1)    
                                        else:
                                            if int(d1)>30 or int(d1)<1:
                                                messagebox.showwarning("Warning", "date not in Range for the Provided Month")
                                            else:
                                                dl.append(1)
                                    if len(dl)==1:
                                        d2=int(d1)
                                        m=int(m1)
                                        y=int(y1)
                                        n=datetime.date(y,m,d2)
                                        if n>k:
                                            messagebox.showwarning("Warning", "Date is not in range")
                                        elif ex.isdigit()==False:
                                            messagebox.showwarning("Warning", "Unexpected Expense Value\n\nOnly Integers are allowed")
                                        else:
                                            message=messagebox.askquestion("Sure", "Date Must Be in The Form \"dd-mm-yyyy\"\n\nOnly Integers Are Accepted For Expense\n\n\tAre you sure?")
                                            if message=="yes":
                                                enor3.destroy()
                                                list3.remove(0)
                                                for i in range(1):
                                                    d=enor4.get()
                                                    if d!='':
                                                        dis=d
                                                    if maincat in maincatgs:
                                                        ins="INSERT INTO "+maincat+"(date, category,Expense,description) values (%s,%s,%s,%s)"
                                                        record= (n, sub, ex,dis)
                                                        cursor.execute(ins, record)
                                                        mydb.commit()
                                                        insert="INSERT INTO Expense (date, category,Expense,description) values (%s,%s,%s,%s)"
                                                        record= (n, sub, ex,dis)
                                                        cursor.execute(insert, record)
                                                        mydb.commit() 
                                                    label1=tk.Label(frame, text='INSERTED',font=('Times',13,'bold'), fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                                                    label1.place(relwidth=0.1, relheight=0.05,relx=0.309,rely=0.45)
                                                    label1.after(2000,label1.destroy)
                                                    enor.delete(first=0,last=100)
                                                    enor2.delete(first=0,last=100)
                                                    enor1.delete(first=0,last=100)
                                                    enor4.delete(first=0,last=100)
                                                    dl.remove(1)
                #============================================================================================================================================================================
                                                cursor.execute("select sum(expense) from expense")      #codes for warning for Budget
                                                data1=cursor.fetchall()
                                                r=data1[0]
                                                r1=r[0]
                                                print("ok",r1,data1)
                                                if r1!=None:
                                                    cursor.execute("select * from budget")
                                                    datar=cursor.fetchall()
                                                    if datar==[]:
                                                        messagebox.showwarning("Warning", "Please Update Your Budget")
                                                    else:
                                                        cursor.execute("select budget from budget")
                                                        data3=cursor.fetchall()
                                                        r2=data3[-1]
                                                        target=r2[0]
                                                        r5=(r1/target)*100
                

                                                        if r5>=100:
                                                            messagebox.showwarning("Warning", "WARNING YOU HAVE REACHED YOUR BUDGET")
                                                        elif r5>=70:
                                                            messagebox.showwarning("Warning", "WARNING YOU HAVE CROSSED 70% OF YOUR BUDGET")
                                                          
#==================================================================================================================================================================================================
                    date=tk.Label(frame, text='Enter date',font=('Times',13,'bold'), fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                    date.place(relx=0.01, rely=0.08)
                    enor=tk.Entry(frame, bd=4, relief=RAISED,font=('Times',13,'bold'), fg='black', bg='snow')
                    enor.place(relwidth=0.15, relheight=0.05, relx=0.15,rely=0.08)
                    category=tk.Label(frame, text='Enter Category',font=('Times',13,'bold'), fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                    category.place(relx=0.01, rely=0.15)
                    Expense=tk.Label(frame, text='Enter Expense',font=('Times',13,'bold'), fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                    Expense.place(relx=0.01, rely=0.35)
                    enor1=tk.Entry(frame, bd=4, relief=RAISED,font=('Times',13,'bold'), fg='black', bg='snow')
                    enor1.place(relwidth=0.1, relheight=0.05, relx=0.15,rely=0.358)
                    needreport1=tk.Label(frame, text='Need Report?',font=('Times',30,'bold'), fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                    needreport1.place(relx=0.01,rely=0.55)
                    date=tk.Label(frame, text='Enter description',font=('Times',13,'bold'), fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                    date.place(relx=0.01, rely=0.45)
                    enor4=tk.Entry(frame, bd=4, relief=RAISED,font=('Times',13,'bold'), fg='black', bg='snow')
                    enor4.place(relwidth=0.15, relheight=0.05, relx=0.15,rely=0.45)
                    button2=tk.Button(frame, text='Enter', font=('Times',10,'bold'),command=inserting_into_tables,fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                    button2.place(relwidth=0.1, relheight=0.05, relx=0.309,rely=0.45)
#==================================================================================================================================================================================================
                    def no():
                        root.destroy()    
#===============================================================================================================================================================================================
                    def fullscreen():
                        root.attributes("-fullscreen", False)
                    def fullreport():
                        global list1
                        if list1==[]:
                            list1.append(0)
                            root.attributes('-fullscreen', True)
                            global frame2
                            frame2=tk.Frame(frame,bg="pale green",)
                            frame2.place(relheight=0.735,relwidth=0.446,relx=0.55,rely=0.15)
                            global buttoner
                            buttoner=tk.Button(frame,text="Close Table",command=closer, font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                            buttoner.place(relwidth=0.087, relheight=0.05,relx=0.909,rely=0.9)
                            canvas=tk.Canvas(frame2,bg="pale green")
                            canvas.place(relheight=0.96,relwidth=0.977,relx=0,rely=0)
                            scrollbar=ttk.Scrollbar(frame2,orient=VERTICAL,command=canvas.yview)
                            scrollbar.pack(side=RIGHT,fill=Y)
                            scrollbar2=ttk.Scrollbar(frame2,orient=HORIZONTAL,command=canvas.xview)
                            scrollbar2.pack(side=BOTTOM,fill=X)
                            canvas.configure(xscrollcommand=scrollbar2.set,yscrollcommand=scrollbar.set)
                            canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
                            frame3=tk.Frame(canvas,bg="pale green")
                            canvas.create_window((0,0),window=frame3,anchor="nw")
                            label1=tk.Label(frame3,text="Date" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                            label1.grid(row=0,column=0)
                            label2=tk.Label(frame3,text="Category" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                            label2.grid(row=0,column=1)
                            label3=tk.Label(frame3,text="Expense" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                            label3.grid(row=0,column=2)
                            label3=tk.Label(frame3,text="Description" ,font=('Times',15,'bold'),width=35,relief=RAISED, fg="green",bd=4,anchor="nw")
                            label3.grid(row=0,column=3)
                            cursor.execute("SELECT * FROM Expense")
                            x=1
                            for i in cursor:
                                for j in range(3):
                                    e=tk.Entry(frame3,font=('Times',15,'bold'),width=13, fg='blue',relief=RAISED,bd=4) 
                                    e.grid(row=x, column=j) 
                                    e.insert(END, i[j])
                                    label=tk.Label(frame3,font=('Times',15,'bold'),width=13, fg='blue',relief=RAISED,bd=4)
                                    label.grid(row=x, column=j)
                                    y=e.get()
                                    label['text']=y
                                for j in range(1):
                                    e=tk.Entry(frame3,font=('Times',15,'bold'),width=35, fg='blue',relief=RAISED,bd=4) 
                                    e.grid(row=x, column=3,) 
                                    e.insert(END, i[3])
                                    label=tk.Label(frame3,font=('Times',15,'bold'),width=35, fg='blue',relief=RAISED,bd=4,anchor="nw")
                                    label.grid(row=x, column=3)
                                    y=e.get()
                                    label['text']=y
                                x=x+1
                            root.after(500,fullscreen)
                            rows=cursor.rowcount
                            if rows>=1:
                                cursor.execute("select sum(Expense) from Expense")
                                data1=cursor.fetchall()
                                r=data1[0]
                                r1=r[0]
                                label3=tk.Label(frame3,text="Sum" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                label3.grid(row=rows+1,column=1)
                                label3=tk.Label(frame3,text=r1 ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                label3.grid(row=rows+1,column=2)
                                cat=[]
                                cat2=[]
                                for i in maincatgs:
                                    cursor.execute("select * from "+i)
                                    data=cursor.fetchall()
                                    if data!=[]:
                                        cursor.execute("select sum(Expense) from "+i)
                                        data2=cursor.fetchall()
                                        r=data2[0]
                                        r1=r[0]
                                        cat.append(i)
                                        cat2.append(r1)
                                data9 = {'Maincategory': cat,'Expense': cat2}
                                df1 = DataFrame(data9,columns=['Maincategory','Expense'])
                                e=1
                                figure1 = plt.Figure(figsize=(6,4))
                                for i in ['barh','pie']:
                                    ax1 = figure1.add_subplot(1,2,e)
                                    bar1 = FigureCanvasTkAgg(figure1, frame7)
                                    bar1.get_tk_widget().place(relwidth=1,relheight=1)
                                    if i=="barh":
                                        df1.plot(x='Maincategory',y='Expense',kind=i, legend=True,ax=ax1)
                                        ax1.set_title('MainCategory vs Expense')
                                        ax1.set_xlabel("Expense")
                                        ax1.set_ylabel("MainCategory")
                                    if i=="pie":
                                        df1.plot(x='Maincategory',y='Expense',kind=i,ax=ax1)
                                        ax1.legend(cat)
                                        ax1.set_title('MainCategory vs Expense')
                                        ax1.set_xlabel("Expense")
                                        ax1.set_ylabel("MainCategory")    
                                    e=e+1
                            else:
                                label7=tk.Label(canvas,text='''No Data''',font=('Times',40,'bold'),height=6,width=19,relief=RAISED, fg="green",bd=4)
                                label7.place(rely=0.087)
                        else:
                            messagebox.showwarning("Warning", " Previous Table\White value Frame not closed\n\n Kindly Close It with \"CLOSE TABLE\" or with \" Close\" \n\nTo Proceed Further")
#========================================================================================================
                    def main():
                        clear2=tk.Button(frame, text='Search Report By Category', font=('Times',13,'bold'),command=retrieving,fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                        clear2.place(relwidth=0.2, relheight=0.05, relx=0.01,rely=0.67)
                        clear3=tk.Button(frame, text='Search Report By Date', font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4',command=datereport)
                        clear3.place(relwidth=0.2, relheight=0.05, relx=0.01,rely=0.73)
                        clear4=tk.Button(frame, text='Search Report By Month', font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4',command=monthreport)
                        clear4.place(relwidth=0.2, relheight=0.05, relx=0.01,rely=0.79)
                        clear5=tk.Button(frame, text='Search Full Report', font=('Times',13,'bold'),command=fullreport,fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                        clear5.place(relwidth=0.2, relheight=0.05, relx=0.01,rely=0.85)
                        clear7.destroy()
                        clear8.destroy()
#============================================================================================================================================================================================
                    clear7=tk.Button(frame, text='Yes', font=('Times',10,'bold'),command=main,fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                    clear7.place(relwidth=0.07, relheight=0.05,relx=0.23,rely=0.543)
                    clear8=tk.Button(frame, text='No', font=('Times',10,'bold'),command=no,fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                    clear8.place(relwidth=0.07, relheight=0.05,relx=0.23,rely=0.6)
#============================================================================================================================================================================================ 
                    clear4=tk.Button(frame, text='Confirm Selection', font=('Times',13,'bold'),command=inserting_by_category,fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                    clear4.place(relwidth=0.15, relheight=0.05,  relx=0.15,rely=0.209)
                    clear5=tk.Button(root, text='Quit',command=no,fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                    clear5.place(relx=0.966,relheight=0.04)
                    def closer23():
                        frame3.destroy()
                        global list2
                        list2.remove(0)
                        global list1
                        list1.remove(0)
#============================================================================================================================================================================================
                    def retrieving():
                        global list1
                        global list2
                        if list1==[] and list2==[]:
                            list1.append(0)
                            global frame3
                            list2.append(0)
                            frame3=tk.Frame(frame,bg="snow")
                            frame3.place(relheight=0.345,relwidth=0.2,relx=0.232,rely=0.55)
                            label_sd=tk.Label(frame3,text='Select Main-Category',font=('Times',13,'bold'),fg='snow',bg='SpringGreen4',relief=RAISED,bd=4)
                            label_sd.place(relx=0.078) 
                            d2=ttk.Combobox(frame3,values=maincatgs,font=('Times',13))
                            d2.place(relx=0.078,rely=0.157)
                            Buttonda=tk.Button(frame3,text="Close",command=closer23,bg='SpringGreen4',bd=4,fg="snow")
                            Buttonda.pack(side=BOTTOM)
                            def main24():
                                c=d2.get()
                                if len(c)!=0:
                                    d1=tk.Label(frame3,text="Select Sub-Category",font=('Times',13,'bold'),fg='snow',bg='SpringGreen4',relief=RAISED,bd=4)
                                    d1.place(relx=0.07,rely=0.448)
                                    w=['all']
                                    for i in flood:
                                        if i==c:
                                            f=flood[i]
                                            for j in f:
                                                w.append(j)
                                    if c=="Miscellaneous":
                                         cursor.execute("select distinct category from Miscellaneous")
                                         data3=cursor.fetchall()
                                         for i in data3:
                                             r=i[0]
                                             w.append(r)
                                    d=ttk.Combobox(frame3,values=w,font=('Times',13))
                                    d.place(relx=0.078,rely=0.59)
                                    def graph():
                                        cat=[]
                                        cat2=[]
                                        cursor.execute("select category,sum(Expense) from "+c+" group by category")
                                        data2=cursor.fetchall()
                                        for i in data2:
                                            r2=i[0]
                                            r1=i[1]
                                            cat.append(r2)
                                            cat2.append(r1)
                                        data9 = {'Subcategory': cat,'Expense': cat2}
                                        df1 = DataFrame(data9,columns=['Subcategory','Expense'])
                                        e=1
                                        figure1 = plt.Figure(figsize=(6,4))
                                        for i in ['barh','pie']:
                                            ax1 = figure1.add_subplot(1,2,e)
                                            bar1 = FigureCanvasTkAgg(figure1, frame7)
                                            bar1.get_tk_widget().place(relwidth=1,relheight=1)
                                            if i=="barh":
                                                df1.plot(x='Subcategory',y='Expense',kind=i, legend=True,ax=ax1)
                                                ax1.set_title('Subategory vs Expense')
                                                ax1.set_xlabel("Expense")
                                                ax1.set_ylabel("Subcategory")
                                            if i=="pie":
                                                df1.plot(x='Subcategory',y='Expense',kind=i,ax=ax1)
                                                ax1.legend(cat)
                                                ax1.set_title('Subcategory vs Expense')
                                                ax1.set_xlabel("Expense")
                                                ax1.set_ylabel("Subcategory")    
                                            e=e+1
                                    def all1():
                                        d1=d.get()
                                        if len(d1)!=0:
                                            if d1=="all":
                                                global frame2
                                                global buttoner
                                                root.attributes('-fullscreen', True)
                                                frame3.destroy()
                                                list2.remove(0)
                                                buttoner=tk.Button(frame,text="Close Table",command=closer, font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                                                buttoner.place(relwidth=0.087, relheight=0.05,relx=0.909,rely=0.9)
                                                frame2=tk.Frame(frame,bg="pale green",)
                                                frame2.place(relheight=0.735,relwidth=0.446,relx=0.55,rely=0.15)
                                                canvas=tk.Canvas(frame2,bg="pale green")
                                                canvas.place(relheight=0.96,relwidth=0.977,relx=0,rely=0)
                                                scrollbar=ttk.Scrollbar(frame2,orient=VERTICAL,command=canvas.yview)
                                                scrollbar.pack(side=RIGHT,fill=Y)
                                                scrollbar2=ttk.Scrollbar(frame2,orient=HORIZONTAL,command=canvas.xview)
                                                scrollbar2.pack(side=BOTTOM,fill=X)
                                                canvas.configure(xscrollcommand=scrollbar2.set,yscrollcommand=scrollbar.set)
                                                canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
                                                frame4=tk.Frame(canvas,bg="pale green")
                                                canvas.create_window((0,0),window=frame4,anchor="nw")
                                                label1=tk.Label(frame4,text="Date" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                                label1.grid(row=0,column=0)
                                                label2=tk.Label(frame4,text="Category" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                                label2.grid(row=0,column=1)
                                                label3=tk.Label(frame4,text="Expense" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                                label3.grid(row=0,column=2)
                                                label3=tk.Label(frame4,text="Description" ,font=('Times',15,'bold'),width=35,relief=RAISED, fg="green",bd=4,anchor="nw")
                                                label3.grid(row=0,column=3)
                                                last="select * from "+c
                                                cursor.execute(last)
                                                x=1            
                                                for i in cursor: 
                                                    for j in range(3):
                                                        e=tk.Entry(frame4,font=('Times',15,'bold'),width=13, fg='blue',relief=RAISED,bd=4) 
                                                        e.grid(row=x, column=j) 
                                                        e.insert(END, i[j])
                                                        label=tk.Label(frame4,font=('Times',15,'bold'),width=13, fg='blue',relief=RAISED,bd=4)
                                                        label.grid(row=x, column=j)
                                                        y=e.get()
                                                        label['text']=y
                                                    for j in range(1):
                                                        e=tk.Entry(frame4,font=('Times',15,'bold'),width=35, fg='blue',relief=RAISED,bd=4) 
                                                        e.grid(row=x, column=3,) 
                                                        e.insert(END, i[3])
                                                        label=tk.Label(frame4,font=('Times',15,'bold'),width=35, fg='blue',relief=RAISED,bd=4,anchor="nw")
                                                        label.grid(row=x, column=3)
                                                        y=e.get()
                                                        label['text']=y
                                                    x=x+1
                                                rows=cursor.rowcount
                                                if rows>=1:
                                                    cursor.execute("select sum(Expense) from "+c)
                                                    data1=cursor.fetchall()
                                                    r=data1[0]
                                                    r1=r[0]
                                                    label3=tk.Label(frame4,text="Sum" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                                    label3.grid(row=rows+1,column=1)
                                                    label3=tk.Label(frame4,text=r1 ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                                    label3.grid(row=rows+1,column=2)
                                                    graph()
                                                else:
                                                    label7=tk.Label(canvas,text='''No Data''',font=('Times',40,'bold'),height=6,width=19,relief=RAISED, fg="green",bd=4)
                                                    label7.place(rely=0.087)
                                                root.after(500,fullscreen)
                                            else:
                                                root.attributes('-fullscreen', True)
                                                frame3.destroy()
                                                list2.remove(0)
                                                buttoner=tk.Button(frame,text="Close Table",command=closer, font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                                                buttoner.place(relwidth=0.087, relheight=0.05,relx=0.909,rely=0.9)
                                                frame2=tk.Frame(frame,bg="pale green",)
                                                frame2.place(relheight=0.735,relwidth=0.446,relx=0.55,rely=0.15)
                                                canvas=tk.Canvas(frame2,bg="pale green")
                                                canvas.place(relheight=0.96,relwidth=0.977,relx=0,rely=0)
                                                scrollbar2=ttk.Scrollbar(frame2,orient=HORIZONTAL,command=canvas.xview)
                                                scrollbar2.pack(side=BOTTOM,fill=X)
                                                scrollbar=ttk.Scrollbar(frame2,orient=VERTICAL,command=canvas.yview)
                                                scrollbar.pack(side=RIGHT,fill=Y)
                                                canvas.configure(xscrollcommand=scrollbar2.set,yscrollcommand=scrollbar.set)
                                                canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
                                                frame4=tk.Frame(canvas,bg="pale green")
                                                canvas.create_window((0,0),window=frame4,anchor="nw")
                                                label1=tk.Label(frame4,text="Date" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                                label1.grid(row=0,column=0)
                                                label2=tk.Label(frame4,text="Category" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                                label2.grid(row=0,column=1)
                                                label3=tk.Label(frame4,text="Expense" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                                label3.grid(row=0,column=2)
                                                label3=tk.Label(frame4,text="Description" ,font=('Times',15,'bold'),width=35,relief=RAISED, fg="green",bd=4,anchor="nw")
                                                label3.grid(row=0,column=3)
                                                salt="select * from " +c+" where category="+"'"+d1+"'"
                                                cursor.execute(salt)
                                                x=1            
                                                for i in cursor: 
                                                    for j in range(3):
                                                        e=tk.Entry(frame4,font=('Times',15,'bold'),width=13, fg='blue',relief=RAISED,bd=4) 
                                                        e.grid(row=x, column=j) 
                                                        e.insert(END, i[j])
                                                        label=tk.Label(frame4,font=('Times',15,'bold'),width=13, fg='blue',relief=RAISED,bd=4)
                                                        label.grid(row=x, column=j)
                                                        y=e.get()
                                                        label['text']=y
                                                    for j in range(1):
                                                        e=tk.Entry(frame4,font=('Times',15,'bold'),width=35, fg='blue',relief=RAISED,bd=4) 
                                                        e.grid(row=x, column=3,) 
                                                        e.insert(END, i[3])
                                                        label=tk.Label(frame4,font=('Times',15,'bold'),width=35, fg='blue',relief=RAISED,bd=4,anchor="nw")
                                                        label.grid(row=x, column=3)
                                                        y=e.get()
                                                        label['text']=y
                                                    x=x+1
                                                rows=cursor.rowcount
                                                if rows>=1:
                                                    cursor.execute("select sum(Expense) from " +c+" where category="+"'"+d1+"'")
                                                    data1=cursor.fetchall()
                                                    r=data1[0]
                                                    r1=r[0]
                                                    label3=tk.Label(frame4,text="Sum" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                                    label3.grid(row=rows+1,column=1)
                                                    label3=tk.Label(frame4,text=r1 ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                                    label3.grid(row=rows+1,column=2)
                                                    graph()
                                                else:
                                                    label7=tk.Label(canvas,text='''No Data''',font=('Times',40,'bold'),height=6,width=19,relief=RAISED, fg="green",bd=4)
                                                    label7.place(rely=0.087)
                                                root.after(138,fullscreen)
                                        else:
                                            messagebox.showwarning("Warning", "Sub Category Not Selected")
                                    abcde=tk.Button(frame3,text="Get Report",command=all1,bg='SpringGreen4',bd=4,fg="snow")
                                    abcde.place(relx=0.65, rely=0.729)
                                else:
                                    messagebox.showwarning("Warning", "Main Category Not Selected")
                            abcd=tk.Button(frame3,text="Confirm",command=main24,font=('Times',10,'bold'),bg='SpringGreen4',bd=4,fg="snow")
                            abcd.place(relx=0.7,rely=0.29)
                        else:
                            messagebox.showwarning("Warning", " Previous Table\Search Frame not closed\n\n Kindly Close It with \"CLOSE TABLE\" or with \" Close\"\n\nTo Proceed Further")
#==================================================================================================================================
                    def datereport():
                        global list1
                        global list2
                        if list1==[] and list2==[]:
                            list1.append(0)
                            list2.append(0)
                            global frame3
                            frame3=tk.Frame(frame,bg="snow",)
                            frame3.place(relheight=0.345,relwidth=0.2,relx=0.232,rely=0.55)
                            label_sd=tk.Label(frame3,text='Enter From Date',font=('Times',13,'bold'),fg='snow',bg='SpringGreen4',relief=RAISED,bd=4)
                            label_sd.pack(padx=23,anchor='w')
                            entry_sd=tk.Entry(frame3,bd=4,relief=RAISED,font=('Times',13,'bold'), fg='black', bg='snow')
                            entry_sd.pack()
                            label_sd1=tk.Label(frame3,text='Enter To Date',font=('Times',13,'bold'),fg='snow',bg='SpringGreen4',relief=RAISED,bd=4)
                            label_sd1.pack(padx=23,anchor='w')
                            entry_sd1=tk.Entry(frame3,bd=4,relief=RAISED,font=('Times',13,'bold'), fg='black', bg='snow')
                            entry_sd1.pack()
                            Buttonda=tk.Button(frame3,text="Close",command=closer23,bg='SpringGreen4',bd=4,fg="snow")
                            Buttonda.pack(side=BOTTOM)
                            def search():
                                dl=[]
                                dl2=[]
                                d=entry_sd.get()
                                if len(d)!=0:
                                    d1=d[0:2]
                                    m1=d[3:5]
                                    y1=d[6:]
                                    if len(d)!=10:
                                        messagebox.showwarning("Warning", "Entered,From Date Not in \"dd-mm-yyyy\" format")
                                    elif d1.isdigit()==False or m1.isdigit()==False:
                                        messagebox.showwarning("Warning", "Unexpected Value Identified in From Date")
                                    elif y1.isdigit()==False:
                                        messagebox.showwarning("Warning", "Unexpected Value Identified in From Date")
                                    elif int(m1)>12 or int(m1)<1:
                                        messagebox.showwarning("Warning", "Month not in Range(From Date)")
                                    elif int(m1) in [1,3,5,7,8,10,12]:
                                        if int(d1)>31 or int(d1)<0:
                                            messagebox.showwarning("Warning", "From Date not in Range for the Provided Month")
                                        else:
                                            dl.append(1)
                                    elif int(m1) not in [1,3,5,7,8,10,12]:
                                        if int(m1)==2:
                                            if int(y1)%4==0:
                                                if int(d1)>29 or int(d1)<1:
                                                    messagebox.showwarning("Warning", "From Date not in Range for the Provided Month")
                                                else:
                                                    dl.append(1)                                    
                                            else:
                                                if int(d1)>28 or int(d1)<1:
                                                    messagebox.showwarning("Warning", "From Date not in Range for the Provided Month")
                                                else:
                                                    dl.append(1)    
                                        else:
                                            if int(d1)>30 or int(d1)<1:
                                                messagebox.showwarning("Warning", "From Date not in Range for the Provided Month")
                                            else:
                                                dl.append(1)
                                else:
                                    messagebox.showwarning("Warning", "Value Not Provided in From Date")
                                e=entry_sd1.get()
                                if len(e)!=0:
                                    d12=e[0:2]
                                    m12=e[3:5]
                                    y12=e[6:]
                                    if len(e)!=10:
                                        messagebox.showwarning("Warning", "Entered, To Date Not in \"dd-mm-yyyy\" format")
                                    elif d12.isdigit()==False or m12.isdigit()==False:
                                        messagebox.showwarning("Warning", "Unexpected Value Identified in To Date")
                                    elif y12.isdigit()==False:
                                        messagebox.showwarning("Warning", "Unexpected Value Identified in To Date")
                                    elif int(m12)>12 or int(m12)<1:
                                        messagebox.showwarning("Warning", "Month not in Range(To Date)")
                                    elif int(m12) in [1,3,5,7,8,10,12]:
                                        if int(d12)>31 or int(d12)<0:
                                            messagebox.showwarning("Warning", "To Date not in Range for the Provided Month")
                                        else:
                                            dl2.append(1)
                                    elif int(m12) not in [1,3,5,7,8,10,12]:
                                        if int(m12)==2:
                                            if int(y12)%4==0:
                                                if int(d12)>29 or int(d12)<1:
                                                    messagebox.showwarning("Warning", "To Date not in Range for the Provided Month")
                                                else:
                                                    dl2.append(1)                                    
                                            else:
                                                if int(d12)>28 or int(d12)<1:
                                                    messagebox.showwarning("Warning", "To Date not in Range for the Provided Month")
                                                else:
                                                    dl2.append(1)    
                                        else:
                                            if int(d12)>30 or int(d12)<1:
                                                messagebox.showwarning("Warning", "To Date not in Range for the Provided Month")
                                            else:
                                                dl2.append(1)
                                else:
                                    messagebox.showwarning("Warning", "Value Not Provided in To Date")
                                if len(dl)==1 and len(dl2)==1:
                                    dl.remove(1)
                                    dl2.remove(1)
                                    d2=int(d1)
                                    m=int(m1)
                                    y=int(y1)
                                    n=datetime.date(y,m,d2)
                                    m=str(n)
                                    d3=int(d12)
                                    m2=int(m12)
                                    y2=int(y12)
                                    n1=datetime.date(y2,m2,d3)
                                    m1=str(n1)
                                    global frame2
                                    global buttoner
                                    root.attributes('-fullscreen', True)
                                    buttoner=tk.Button(frame,text="Close Table",command=closer, font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                                    buttoner.place(relwidth=0.087, relheight=0.05,relx=0.909,rely=0.9)
                                    frame2=tk.Frame(frame,bg="pale green",)
                                    frame2.place(relheight=0.735,relwidth=0.446,relx=0.55,rely=0.15)
                                    canvas=tk.Canvas(frame2,bg="pale green")
                                    canvas.place(relheight=0.96,relwidth=0.977,relx=0,rely=0)
                                    scrollbar2=ttk.Scrollbar(frame2,orient=HORIZONTAL,command=canvas.xview)
                                    scrollbar2.pack(side=BOTTOM,fill=X)
                                    scrollbar=ttk.Scrollbar(frame2,orient=VERTICAL,command=canvas.yview)
                                    scrollbar.pack(side=RIGHT,fill=Y)
                                    canvas.configure(xscrollcommand=scrollbar2.set,yscrollcommand=scrollbar.set)
                                    canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
                                    frame4=tk.Frame(canvas,bg="pale green")
                                    canvas.create_window((0,0),window=frame4,anchor="nw")
                                    label1=tk.Label(frame4,text="Date" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                    label1.grid(row=0,column=0)
                                    label2=tk.Label(frame4,text="Category" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                    label2.grid(row=0,column=1)
                                    label3=tk.Label(frame4,text="Expense" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                    label3.grid(row=0,column=2)
                                    label3=tk.Label(frame4,text="Description" ,font=('Times',15,'bold'),width=35,relief=RAISED, fg="green",bd=4,anchor="nw")
                                    label3.grid(row=0,column=3)
                                    search="select * from Expense where date between '"+m+"' and '"+m1+"' ;"
                                    cursor.execute(search)
                                    x=1
                                    for i in cursor:
                                        for j in range(3):
                                            e=tk.Entry(frame4,font=('Times',15,'bold'),width=13, fg='blue',relief=RAISED,bd=4) 
                                            e.grid(row=x, column=j) 
                                            e.insert(END, i[j])
                                            label=tk.Label(frame4,font=('Times',15,'bold'),width=13, fg='blue',relief=RAISED,bd=4)
                                            label.grid(row=x, column=j)
                                            y=e.get()
                                            label['text']=y
                                        for j in range(1):
                                            e=tk.Entry(frame4,font=('Times',15,'bold'),width=35, fg='blue',relief=RAISED,bd=4) 
                                            e.grid(row=x, column=3,) 
                                            e.insert(END, i[3])
                                            label=tk.Label(frame4,font=('Times',15,'bold'),width=35, fg='blue',relief=RAISED,bd=4,anchor="nw")
                                            label.grid(row=x, column=3)
                                            y=e.get()
                                            label['text']=y
                                        x=x+1
                                    rows=cursor.rowcount
                                    if rows>=1:
                                        cursor.execute("select sum(expense) from Expense where date between '"+m+"' and '"+m1+"' ;")
                                        data1=cursor.fetchall()
                                        r=data1[0]
                                        r1=r[0]
                                        label3=tk.Label(frame4,text="Sum" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                        label3.grid(row=rows+1,column=1)
                                        label3=tk.Label(frame4,text=r1 ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                        label3.grid(row=rows+1,column=2)
                                        cat=[]
                                        cat2=[]
                                        cursor.execute("select category,sum(Expense) from Expense where date between '"+m+"' and '"+m1+"'group by category")
                                        data2=cursor.fetchall()
                                        for i in data2:
                                            r2=i[0]
                                            r1=i[1]
                                            cat.append(r2)
                                            cat2.append(r1)
                                        data9 = {'Maincategory': cat,'Expense': cat2}
                                        df1 = DataFrame(data9,columns=['Maincategory','Expense'])
                                        e=1
                                        figure1 = plt.Figure(figsize=(6,4))
                                        for i in ['barh','pie']:
                                            ax1 = figure1.add_subplot(1,2,e)
                                            bar1 = FigureCanvasTkAgg(figure1, frame7)
                                            bar1.get_tk_widget().place(relwidth=1,relheight=1)
                                            if i=="barh":
                                                df1.plot(x='Maincategory',y='Expense',kind=i, legend=True,ax=ax1)
                                                ax1.set_title('Mainategory vs Expense')
                                                ax1.set_xlabel("Expense")
                                                ax1.set_ylabel("Maincategory")
                                            if i=="pie":
                                                df1.plot(x='Maincategory',y='Expense',kind=i,ax=ax1)
                                                ax1.legend(cat)
                                                ax1.set_title('Maincategory vs Expense')             
                                            e=e+1
                                    else:
                                        label7=tk.Label(canvas,text='''No Data''',font=('Times',40,'bold'),height=6,width=19,relief=RAISED, fg="green",bd=4)
                                        label7.place(rely=0.087)
                                    root.after(500,fullscreen)
                                    frame3.destroy()    
                            button_sd=tk.Button(frame3,text='Search',font=('Times',10,'bold'),command=search,fg='snow',bg='SpringGreen4',relief=RAISED,bd=4)
                            button_sd.place(relx=0.668,rely=0.65)
                        else:
                            messagebox.showwarning("Warning", " Previous Table\Search Frame not closed\n\n Kindly Close It with \"CLOSE TABLE\" or with \" Close\"\n\nTo Proceed Further")
#=========================================================================================================================================================================================================
                    def monthreport():
                        global list1
                        global list2
                        if list1==[] and list2==[]:
                            list1.append(0)
                            list2.append(0)
                            global frame3
                            frame3=tk.Frame(frame,bg="snow",)
                            frame3.place(relheight=0.345,relwidth=0.2,relx=0.232,rely=0.55)
                            label_sd=tk.Label(frame3,text='Enter Month',font=('Times',13,'bold'),fg='snow',bg='SpringGreen4',relief=RAISED,bd=4)
                            label_sd.place(relx=0.078)
                            Months=["January","February","March","April","May","June","July",
                                    "August","September","October","November","December"]        
                            Combo=ttk.Combobox(frame3,values=Months,font=('Times',13))
                            Combo.place(relx=0.078,rely=0.157)
                            Buttonda=tk.Button(frame3,text="Close",command=closer23,bg='SpringGreen4',bd=4,fg="snow")
                            Buttonda.pack(side=BOTTOM)
                            def search():
                                A=Combo.get()
                                if len(A)!=0: 
                                    for i in months:
                                        if A==i:
                                            d=months[i]
                                    frame3.destroy()
                                    global frame2
                                    global buttoner
                                    root.attributes('-fullscreen', True)
                                    buttoner=tk.Button(frame,text="Close Table",command=closer, font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
                                    buttoner.place(relwidth=0.087, relheight=0.05,relx=0.909,rely=0.9)
                                    frame2=tk.Frame(frame,bg="pale green",)
                                    frame2.place(relheight=0.735,relwidth=0.446,relx=0.55,rely=0.15)
                                    canvas=tk.Canvas(frame2,bg="pale green")
                                    canvas.place(relheight=0.96,relwidth=0.977,relx=0,rely=0)
                                    scrollbar2=ttk.Scrollbar(frame2,orient=HORIZONTAL,command=canvas.xview)
                                    scrollbar2.pack(side=BOTTOM,fill=X)
                                    scrollbar=ttk.Scrollbar(frame2,orient=VERTICAL,command=canvas.yview)
                                    scrollbar.pack(side=RIGHT,fill=Y)
                                    canvas.configure(xscrollcommand=scrollbar2.set,yscrollcommand=scrollbar.set)
                                    canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
                                    frame4=tk.Frame(canvas,bg="pale green")
                                    canvas.create_window((0,0),window=frame4,anchor="nw")
                                    label1=tk.Label(frame4,text="Date" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                    label1.grid(row=0,column=0)
                                    label2=tk.Label(frame4,text="Category" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                    label2.grid(row=0,column=1)
                                    label3=tk.Label(frame4,text="Expense" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                    label3.grid(row=0,column=2)
                                    label3=tk.Label(frame4,text="Description" ,font=('Times',15,'bold'),width=35,relief=RAISED, fg="green",bd=4,anchor="nw")
                                    label3.grid(row=0,column=3)
                                    search="select * from Expense where date like \"_____"+d+'%\"'
                                    cursor.execute(search)
                                    x=1
                                    for i in cursor:
                                        for j in range(3):
                                            e=tk.Entry(frame4,font=('Times',15,'bold'),width=13, fg='blue',relief=RAISED,bd=4) 
                                            e.grid(row=x, column=j) 
                                            e.insert(END, i[j])
                                            label=tk.Label(frame4,font=('Times',15,'bold'),width=13, fg='blue',relief=RAISED,bd=4)
                                            label.grid(row=x, column=j)
                                            y=e.get()
                                            label['text']=y
                                        for j in range(1):
                                            e=tk.Entry(frame4,font=('Times',15,'bold'),width=35, fg='blue',relief=RAISED,bd=4) 
                                            e.grid(row=x, column=3,) 
                                            e.insert(END, i[3])
                                            label=tk.Label(frame4,font=('Times',15,'bold'),width=35, fg='blue',relief=RAISED,bd=4,anchor="nw")
                                            label.grid(row=x, column=3)
                                            y=e.get()
                                            label['text']=y
                                        x=x+1
                                    rows=cursor.rowcount
                                    if rows>=1:
                                        cursor.execute("select sum(Expense) from Expense where date like \"_____"+d+'%\"')
                                        data1=cursor.fetchall()
                                        r=data1[0]
                                        r1=r[0]
                                        label3=tk.Label(frame4,text="Sum" ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                        label3.grid(row=rows+1,column=1)
                                        label3=tk.Label(frame4,text=r1 ,font=('Times',15,'bold'),width=13,relief=RAISED, fg="green",bd=4)
                                        label3.grid(row=rows+1,column=2)
                                        cat=[]
                                        cat2=[]
                                        cursor.execute("select category,sum(Expense) from Expense "+"where date like \"_____"+d+'%\"'+" group by category")
                                        data2=cursor.fetchall()
                                        for i in data2:
                                            r2=i[0]
                                            r1=i[1]
                                            cat.append(r2)
                                            cat2.append(r1)
                                        data9 = {'Maincategory': cat,'Expense': cat2}
                                        df1 = DataFrame(data9,columns=['Maincategory','Expense'])
                                        e=1
                                        figure1 = plt.Figure(figsize=(6,4))
                                        for i in ['barh','pie']:
                                            ax1 = figure1.add_subplot(1,2,e)
                                            bar1 = FigureCanvasTkAgg(figure1, frame7)
                                            bar1.get_tk_widget().place(relwidth=1,relheight=1)
                                            if i=="barh":
                                                df1.plot(x='Maincategory',y='Expense',kind=i, legend=True,ax=ax1)
                                                ax1.set_title('Mainategory vs Expense')
                                                ax1.set_xlabel("Expense")
                                                ax1.set_ylabel("Maincategory")
                                            if i=="pie":
                                                df1.plot(x='Maincategory',y='Expense',kind=i,ax=ax1)
                                                ax1.legend(cat)
                                                ax1.set_title('Maincategory vs Expense')             
                                            e=e+1
                                    else:
                                        label7=tk.Label(canvas,text='''No Data''',font=('Times',40,'bold'),height=8,width=23,relief=RAISED, fg="green",bd=4)
                                        label7.place(rely=0.087)
                                    root.after(500,fullscreen)
                                else:
                                    messagebox.showwarning("Warning", "Month Not Selected")
                            button_sd=tk.Button(frame3,text='Search',font=('Times',10,'bold'),command=search,fg='snow',bg='SpringGreen4',relief=RAISED,bd=4)
                            button_sd.place(relx=0.7,rely=0.29)
                        else:
                            messagebox.showwarning("Warning", " Previous Table\Search Frame not closed\n\n Kindly Close It with \"CLOSE TABLE\" or with \" Close\"\n\nTo Proceed Further")
#============================================================================================================================================================================================
                    def clock():
                        x=datetime.datetime.now()
                        hour=x.strftime("%I")
                        minute=x.strftime("%M")
                        second=x.strftime("%S")
                        day=x.strftime("%A")
                        AMORPM=x.strftime("%p")
                        d=x.strftime("%d")
                        global Tdate
                        Tdate=d
                        m=x.strftime("%m")
                        global h
                        h=x.strftime("%m")
                        y=x.strftime("%Y")
                        clocklabel=tk.Label(frame,text="",fg="snow",font=('Times',10,'bold'),bg="SpringGreen4")
                        clocklabel.place(rely=0.958,relwidth=0.19,relx=0.808)
                        clocklabel.config(text=hour+":"+minute+":"+second+"  "+AMORPM+'  '+d+"-"+m+"-"+y+"  "+day)
                        clocklabel.after(1000,clock)
                        global k
                        k=x.date()
                    clock()
#=======================================================================================================
                    def warning():
                        d7=tk.Label(frame,text="SET BUDGET",font=('Times',17,'bold'),bg="SpringGreen4",fg="snow",relief=RAISED,bd=4)
                        d7.place(relx=0.63,rely=0.02)
                        d5=tk.Entry(frame,font=('Times',17,'bold'),relief=RAISED,bd=4)
                        d5.place(relx=0.78,rely=0.02)
                        button1.destroy()
                        def destroyer():
                            d5.destroy()
                            d7.destroy()
                            button2.destroy()
                            button3.destroy()
                            button1=tk.Button(frame,text="UPDATE BUDGET",font=('Times',12,'bold'),command=warning,bg="SpringGreen4",fg="snow")
                            button1.place(relx=0.868,rely=0.02)
                        def setter():
                            t=d5.get()
                            if t=='':
                                messagebox.showwarning("Warning", "ALERT No BUDGET IS PROVIDED")
                            else:
                                inserter="INSERT INTO budget values (%s)"
                                inserter2=(t,)
                                cursor.execute(inserter,inserter2)
                                mydb.commit()
                                d5.destroy()
                                d7.destroy()
                                button2.destroy()
                                button3.destroy()
                                BOX=messagebox.showinfo("UPDATED", "BUDGET UPDATED SUCCESSFULLY")
                                if BOX=="ok":
                                    button1=tk.Button(frame,text="UPDATE BUDGET",font=('Times',12,'bold'),command=warning,bg="SpringGreen4",fg="snow")
                                    button1.place(relx=0.868,rely=0.02)
                                    
                        button2=tk.Button(frame,text="confirm",font=('Times',11,'bold'),command=setter,bg="SpringGreen4",fg="snow")
                        button2.place(relheight=0.0459,relx=0.941,rely=0.0269)
                        button3=tk.Button(frame,text="cancel ",font=('Times',11,'bold'),command=destroyer,bg="SpringGreen4",fg="snow")
                        button3.place(relheight=0.0459,relx=0.78,rely=0.09)
                    button1=tk.Button(frame,text="UPDATE BUDGET",font=('Times',12,'bold'),command=warning,bg="SpringGreen4",fg="snow")
                    button1.place(relx=0.868,rely=0.02)
#============================================================================================================================================================================================
                    def setter2():
                        global root3
                        root3=tk.Tk()
                        root3.title("Budget")
                        root3.iconbitmap('sat1.ico')
                        root3.resizable(0,0)
                        root3.geometry("200x119")
                        center_tk_window.center_on_screen(root3)
                        frame5=tk.Frame(root3,bg="pale green")
                        frame5.place(relwidth=1,relheight=1)
                        d7=tk.Label(frame5,text="Set Budget",bg="SpringGreen4",fg="ghost white",font=('Times',15,'bold'),relief=RAISED,bd=4,width=10)
                        d7.place(relx=0.04,rely=0.028999)
                        d5=tk.Entry(frame5,font=('Times',13,'bold'),relief=RAISED,bd=3)
                        d5.place(relx=0.04,rely=0.38)
                        def entry2():
                            d4=d5.get()
                            if d4=='':
                                messagebox.showwarning("Warning", " A Budget must be Provided")   
                            else:
                                inserter="INSERT INTO budget values (%s)"
                                inserter2=(d4,)
                                cursor.execute(inserter,inserter2)
                                mydb.commit()
                                root3.destroy()
                        button2=tk.Button(frame5,text="Enter",command=entry2,bg="SpringGreen4",fg="snow",font=('Times',11,'bold'),relief=RAISED,bd=4)
                        button2.place(relx=0.7,rely=0.64)
                    if Tdate=='01':
                        setter2()
                    cursor.execute("select * from budget")
                    budget2=cursor.fetchall()
                    if budget2==[]:
                        setter2()
                    root.mainloop()
            else:
                mess=messagebox.askokcancel("Warning", "NEW User Identified\n\n Create User")
                if mess==True:
                    createusers()
                    root9.destroy()    
        button9=tk.Button(frame23,text="Confirm",bg="SpringGreen4",fg="snow",command=user)
        button9.place(rely=0.68,relx=0.65)
        button9=tk.Button(frame23,text="New User: Sign in",bg="SpringGreen4",fg="snow",command=createusers3,font=('Times',10,'bold'),relief=RAISED,bd=3)
        button9.place(rely=0.83,relx=0.03)#Login window Ends here
#============================================================================================================================================================================================
program()#Calling the program to Execute while Execution
