import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from tkcalendar import DateEntry
from datetime import date
import random
root=Tk()

root.geometry('700x500')
root.resizable(False,False)
menubar=Menu(root)
root.configure(menu=menubar)
file=Menu(root,tearoff=0)
file.add_command(label="exit",command=root.destroy)
file.add_separator()
menubar.add_cascade(label="exit",menu=file)
root.title('FINAL YEAR PROJECT ALLOCATION')
#Student Page !
no=StringVar()
noTwo=StringVar()
def student_login(x,y):
    def student_login_page():
        no.set(x)
        noTwo.set(y)
        def logout():
            main_frame.destroy()
            option_frame.destroy()
            registeration_login()
        
        def home_page():
            home_frame=Frame(main_frame,width=500,height=400)
            home_frame.pack()
            logout_btn=Button(home_frame,text="LOGOUT",bd=0,fg='red',command=logout)
            logout_btn.place(x=450,y=20)
            label_home=Label(home_frame,text='HOME',foreground="purple",font=('bold',15))
            label_home.place(x=200,y=50)
    
            label_UserId=Label(home_frame,text='Student Id',font=("Helvetica",11))
            label_UserId.place(x=35,y=80)
            usrName=Entry(home_frame,textvariable=no)
            usrName.place(x=10,y=105)

            name=""

            label2_page1=Label(home_frame,text="Schdule",font=("Helvetica",11))
            label2_page1.place(x=385,y=210)
            textTwo=Text(home_frame,width=21,height=11)
            textTwo.insert(END,name)
            textTwo.place(x=330,y=230)

        
            label_UserId=Label(home_frame,text='Guide',font=("Helvetica",11))
            label_UserId.place(x=355,y=80)
            guideName=Label(home_frame,text='Click the button',font=("Helvetica",11),foreground='green')
            guideName.place(x=350,y=105)
    
            message=""
        
            label2_page1=Label(home_frame,text="Message",font=("Helvetica",11))
            label2_page1.place(x=40,y=200)
            textOne=Text(home_frame,width=20,height=10)
            textOne.insert(END,message)
            textOne.place(x=10,y=230)

            title=StringVar()
            title.set("")
        
            label2_page1=Label(home_frame,text="Title :")
            label2_page1.place(x=10,y=150)
            titleentry=Entry(home_frame,width=100,textvariable=title)
            titleentry.place(x=60,y=150)

            def dbtitle1(userID):
                conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                cursor = conn.cursor()
                cursor.execute("select * from student where studid1='%s'"%userID)
                t=cursor.fetchall()
                if t:
                    st="select * from title where userID='%s'";
                    cursor.execute(st%(userID))
                    r1=cursor.fetchall()
                    for i in r1:
                        x=str(i[2])
                    title.set(x)
                    conn.commit()
                else:
                    messagebox.showinfo("Title",'Repost the Title')

            def dbtitle2(userId):
                conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                cursor = conn.cursor()
                cursor.execute("select * from student where studid2='%s'"%userId)
                t=cursor.fetchall()
                if t:
                    st="select * from title where userID2='%s'";
                    cursor.execute(st%(userId))
                    r1=cursor.fetchall()
                    for i in r1:
                        x=str(i[2])
                    title.set(x)
                    conn.commit()
                else:
                    messagebox.showinfo("Title",'Repost the Title')
                
            def dbMessage1(userId):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                try:
                    pass
                except:
                    messagebox.showinfo("Message","There is no message from Guide")
                    
            def search():
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                userId=usrName.get()
                textTwo.delete("1.0","end")
                textOne.delete("1.0","end")
                title.set("")
                if(userId!=""):
                    try:
                        cursor.execute("select * from student where studid1='%s'"%userId)
                        r=cursor.fetchall()
                        if r:
                            dbfound(userId)
                            dbtitle1(userId)
                        else:
                            cursor.execute("select * from student where studid2='%s'"%userId)
                            e=cursor.fetchall()
                            if e:
                                dbfound2(userId)
                                dbtitle2(userId)
                            else:
                               messagebox.showerror("Failed","please Fill The Rollno")

                    except:
                        pass
                else:
                    messagebox.showerror("Failed","please Fill the Student Id Entry")

                    
            def dbMessage2(userId):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()        
                try:
                    cursor.execute("select * from abstractmessage where userId2='%s'"%userId)
                    m=cursor.fetchall()
                    ##print(m)
                    for i in m:
                        message=str(i[2])
                    textOne.insert(END,message)
                    #print(message)
                except:
                    messagebox.showinfo("Message","There is no message from Guide")


            def dbfound(userId):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                try:
                    cursor.execute("select * from student where studid1='%s'"%userId)
                    r=cursor.fetchall()
                    ##print(r)
                    for i in r:
                        s1=str(i[0])
                        s2=str(i[1])
                        s3=st=(i[6])
                    #display reviewSchdule
                    cursor.execute("select * from reviewschdule where batch='%s' and dept='%s' AND stream='%s'"%(s1,s2,s3))
                    e=cursor.fetchall()
                    for i in e:
                        abstract=str(i[3])
                        proposal=str(i[4])
                        reviewOne=str(i[5])
                        reviewTwo=str(i[6])
                        reviewThree=str(i[7])
                        report=str(i[8])
                        final=str(i[9])
                    value="Abstract :"+abstract+"\nProposal :"+proposal+"\nReview1  :"+reviewOne+"\nReview2  :"+reviewTwo+"\nReview3  :"+reviewThree+"\nReport   :"+report+"\nFinal    :"+final
                    ##print(value)
                    textTwo.insert(END,value)
                    #fetching from Allocation
                    cursor.execute("select * from allocation where student1='%s'"%userId)
                    a=cursor.fetchall()
                    ##print(a)
                    for i in a:
                        guide=str(i[3])
                    guideName['text']=guide
                    try:
                        cursor.execute("SELECT * FROM `abstractmessage` WHERE userID='%s'"%userId)
                        m=cursor.fetchall()
                        for i in m:
                            mess=str(i[2])
                        #rint(mess)
                        textOne.insert(END,mess)
                    except:
                        messagebox.showinfo("Message","There is no message from guide")

                except:
                    messagebox.showerror("Failed","There is no ID Found")

            def dbfound2(userId):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                try:
                    cursor.execute("select * from student where studid2='%s'"%userId)
                    r=cursor.fetchall()
                    ##print(r)
                    for i in r:
                        s1=str(i[0])
                        s2=str(i[1])
                        s3=st=(i[6])
                    #display reviewSchdule
                    cursor.execute("select * from reviewschdule where batch='%s' and dept='%s' AND stream='%s'"%(s1,s2,s3))
                    e=cursor.fetchall()
                    for i in e:
                        abstract=str(i[3])
                        proposal=str(i[4])
                        reviewOne=str(i[5])
                        reviewTwo=str(i[6])
                        reviewThree=str(i[7])
                        report=str(i[8])
                        final=str(i[9])
                    value="Abstract :"+abstract+"\nProposal :"+proposal+"\nReview1  :"+reviewOne+"\nReview2  :"+reviewTwo+"\nReview3  :"+reviewThree+"\nReport   :"+report+"\nFinal    :"+final
                    ##print(value)
                    textTwo.insert(END,value)
                    #fetching from Allocation
                    cursor.execute("select * from allocation where student2='%s'"%userId)
                    a=cursor.fetchall()
                    ##print(a)
                    for i in a:
                        guide=str(i[3])
                    guideName['text']=guide
                    try:
                        cursor.execute("SELECT * FROM `abstractmessage` WHERE userID2='%s'"%userId)
                        m=cursor.fetchall()
                        for i in m:
                            mess=str(i[2])
                        textOne.insert(END,mess)
                        
                    except:
                        messagebox.showinfo("Message","There is no message from guide")

                except:
                    messagebox.showerror("Failed","There is no ID Found")
            
            btn=Button(home_frame,text="click",command=search)
            btn.place(x=150,y=100)



            


            
            
        def student_Abstract_page():
            def page1go(): 
                page1=Frame(main_frame,width=500,height=400)
                page1.pack()
                label_page1=Label(page1,text="ABSTRACT",foreground="cyan",font=('bold',15))
                label_page1.place(x=200,y=50)
                label2_page1=Label(page1,text="Student ID First :")
                label2_page1.place(x=10,y=100)
                usrName=Entry(page1,textvariable=no)
                usrName.place(x=110,y=100)
                label3_page1=Label(page1,text="Student ID Second :")
                label3_page1.place(x=10,y=150)
                usrNameTwo=Entry(page1,textvariable=noTwo)
                usrNameTwo.place(x=120,y=150)
                l4=Label(page1,text='Type :')
                l4.place(x=10,y=200)
                def des():
                    if(var_radio.get()=='s'):
                        usrNameTwo.config(state='disabled')
                    elif(var_radio.get()=='p'):
                        usrNameTwo.config(state='normal')

                var_radio=StringVar()
                r1=Radiobutton(page1,text='single',value='s',variable=var_radio,command=des)
                r1.place(x=85,y=200)
                r2=Radiobutton(page1,text='Pair',value='p',variable=var_radio,command=des)
                r2.place(x=140,y=200)
                var_radio.set('s')
                usrNameTwo.config(state='disabled')
                label2_page1=Label(page1,text="Title :")
                label2_page1.place(x=10,y=250)
                titleentry=Entry(page1,width=100)
                titleentry.place(x=60,y=250)
                label4_page1=Label(page1,text="Abstract Submission :")
                label4_page1.place(x=10,y=300)
                def db():
                    # Connect to the database
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cur = conn.cursor()
                    userID1=usrName.get()
                    title=titleentry.get()
                    userID2=usrNameTwo.get()
                    s=var_radio.get()
                    def upload_file():

                        # Open a file dialog to select a PDF file to upload
                        from tkinter.filedialog import askopenfilename
                        file_path = askopenfilename(filetypes=[('PDF Files', '*.pdf')])
                        if not file_path:
                            return
                        
                        # Extract the file name from the file path
                        import os
                        file_name = os.path.basename(file_path)

                        # Read the contents of the file
                        with open(file_path, 'rb') as file:
                            data = file.read()

                        # Insert the file into the database
                        try:
                           
                            if(s=='s'):
                                cur.execute('INSERT INTO abstract (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                cur.execute('insert into title(userID,userID2,title) values(%s,%s,%s)',(userID1,userID2,title))
                                conn.commit()
                                message = f"The file '{file_name}' and Title was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                            else:
                                cur.execute('INSERT INTO abstract (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                cur.execute('insert into title(userID,userID2,title) values(%s,%s,%s)',(userID1,userID2,title))
                                conn.commit()
                                message = f"The file '{file_name}' and Title was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                        except:
                            messagebox.showerror("Fileupload","ERROR Aquired");

                    # Display a success message

                    upload_file()
                btn_upload=Button(page1,text='Upload here !',command=db)
                btn_upload.place(x=180,y=300)
            page1go()
        def student_proposal_page():
            def page1go(): 
                page1=Frame(main_frame,width=500,height=400)
                page1.pack()
                label_page1=Label(page1,text="PROPOSAL",foreground="gold",font=('bold',15))
                label_page1.place(x=200,y=50)
                label2_page1=Label(page1,text="Student ID First :")
                label2_page1.place(x=10,y=100)
                usrName=Entry(page1,textvariable=no)
                usrName.place(x=110,y=100)
                label3_page1=Label(page1,text="Student ID Second :")
                label3_page1.place(x=10,y=150)
                usrNameTwo=Entry(page1,textvariable=noTwo)
                usrNameTwo.place(x=120,y=150)
                l4=Label(page1,text='Type :')
                l4.place(x=10,y=200)
                def des():
                    if(var_radio.get()=='s'):
                        usrNameTwo.config(state='disabled')
                    elif(var_radio.get()=='p'):
                        usrNameTwo.config(state='normal')

                var_radio=StringVar()
                r1=Radiobutton(page1,text='single',value='s',variable=var_radio,command=des)
                r1.place(x=85,y=200)
                r2=Radiobutton(page1,text='Pair',value='p',variable=var_radio,command=des)
                r2.place(x=140,y=200)
                var_radio.set('s')
                usrNameTwo.config(state='disabled')
                name=StringVar()
                name.set("")
                def dbfuntitle():
                    userID=usrName.get()
                    if(userID!=""):
                        dbtitle()
                    else:
                        messagebox.showerror("Required","Please fill the Student ID")
                def dbtitle():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    try:
                        cursor.execute("select * from student where studid1='%s'"%userID)
                        r=cursor.fetchall()
                        if r:
                            st="select * from title where userID='%s'";
                            cursor.execute(st%(userID))
                            r1=cursor.fetchall()
                            for i in r1:
                                x=str(i[2])
                            name.set(x)
                            conn.commit()
                        else :
                            cursor.execute("select * from student where studid2='%s'"%userID)
                            r=cursor.fetchall()
                            if r:
                                st="select * from title where userID2='%s'";
                                cursor.execute(st%(userID))
                                r1=cursor.fetchall()

                                for i in r1:
                                    x=str(i[2])
                                name.set(x)
                                conn.commit()
                            else:
                                messagebox.showerror("Failed",'Check the Student Id')
                    except:
                        messagebox.showerror("Failed",'Check the Student Id')
                     
                    
                btn_found=Button(page1,text="click",command=dbfuntitle)
                btn_found.place(x=250,y=200)
                label2_page1=Label(page1,text="Title :")
                label2_page1.place(x=10,y=250)
                title=Entry(page1,width=100,textvariable=name)
                title.place(x=60,y=250)
                label4_page1=Label(page1,text="Proposal Submission :")
                label4_page1.place(x=10,y=300)
           

                def db():
                    # Connect to the database
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cur = conn.cursor()
                    userID1=usrName.get()
                    userID2=usrNameTwo.get()
                    s=var_radio.get()
                    def upload_file():

                        # Open a file dialog to select a PDF file to upload
                        from tkinter.filedialog import askopenfilename
                        file_path = askopenfilename(filetypes=[('PDF Files', '*.pdf')])
                        if not file_path:
                            return
                        
                        # Extract the file name from the file path
                        import os
                        file_name = os.path.basename(file_path)

                        # Read the contents of the file
                        with open(file_path, 'rb') as file:
                            data = file.read()

                        # Insert the file into the database
                        try:
                            m=""
                            if(s=='s'):
                                cur.execute('INSERT INTO proposal (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                cur.execute("update abstractmessage set message='%s' where userID='%s' and userID2='%s'"%(m,userID1,userID2))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                            else:
                                cur.execute('INSERT INTO proposal (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                cur.execute("update abstractmessage set message='%s' where userID='%s' and userID2='%s'"%(m,userID1,userID2))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                        except:
                            messagebox.showerror("Fileupload","ERROR Aquired");

                    # Display a success message

                    upload_file()
                btn_upload=Button(page1,text='Upload here !',command=db)
                btn_upload.place(x=180,y=300)
            page1go()
        def student_review1_page():
            def page1go(): 
                page1=Frame(main_frame,width=500,height=400)
                page1.pack()
                label_page1=Label(page1,text="REVIEW 1",foreground="chocolate2",font=('bold',15))
                label_page1.place(x=200,y=50)
                label2_page1=Label(page1,text="Student ID First :")
                label2_page1.place(x=10,y=100)
                usrName=Entry(page1,textvariable=no)
                usrName.place(x=110,y=100)
                label3_page1=Label(page1,text="Student ID Second :")
                label3_page1.place(x=10,y=150)
                usrNameTwo=Entry(page1,textvariable=noTwo)
                usrNameTwo.place(x=120,y=150)
                l4=Label(page1,text='Type :')
                l4.place(x=10,y=200)
                def des():
                    if(var_radio.get()=='s'):
                        usrNameTwo.config(state='disabled')
                    elif(var_radio.get()=='p'):
                        usrNameTwo.config(state='normal')

                var_radio=StringVar()
                r1=Radiobutton(page1,text='single',value='s',variable=var_radio,command=des)
                r1.place(x=85,y=200)
                r2=Radiobutton(page1,text='Pair',value='p',variable=var_radio,command=des)
                r2.place(x=140,y=200)
                var_radio.set('s')
                usrNameTwo.config(state='disabled')
                name=StringVar()
                name.set("")
                def dbfuntitle():
                    userID=usrName.get()
                    if(userID!=""):
                        dbtitle()
                    else:
                        messagebox.showerror("Required","Please fill the Student ID")
                def dbtitle():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    try:
                        cursor.execute("select * from student where studid1='%s'"%userID)
                        r=cursor.fetchall()
                        if r:
                            st="select * from title where userID='%s'";
                            cursor.execute(st%(userID))
                            r1=cursor.fetchall()
                            for i in r1:
                                x=str(i[2])
                            name.set(x)
                            conn.commit()
                        else :
                            cursor.execute("select * from student where studid2='%s'"%userID)
                            r=cursor.fetchall()
                            if r:
                                st="select * from title where userID2='%s'";
                                cursor.execute(st%(userID))
                                r1=cursor.fetchall()

                                for i in r1:
                                    x=str(i[2])
                                name.set(x)
                                conn.commit()
                            else:
                                messagebox.showerror("Failed",'Check the Student Id')
                    except:
                        messagebox.showerror("Failed",'Check the Student Id')
                     
                        
                btn_found=Button(page1,text="click",command=dbfuntitle)
                btn_found.place(x=250,y=200)
                label2_page1=Label(page1,text="Title :")
                label2_page1.place(x=10,y=250)
                title=Entry(page1,width=100,textvariable=name)
                title.place(x=60,y=250)
                label3_page1=Label(page1,text="First Review Submission :")
                label3_page1.place(x=10,y=300)
                def db():
                    # Connect to the database
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cur = conn.cursor()
                    userID1=usrName.get()
                    userID2=usrNameTwo.get()
                    s=var_radio.get()
                    def upload_file():

                        # Open a file dialog to select a PDF file to upload
                        from tkinter.filedialog import askopenfilename
                        file_path = askopenfilename(filetypes=[('PPT Files', '*.ppt;*.pptx;')])
                        if not file_path:
                            return
                        
                        # Extract the file name from the file path
                        import os
                        file_name = os.path.basename(file_path)

                        # Read the contents of the file
                        with open(file_path, 'rb') as file:
                            data = file.read()

                        # Insert the file into the database
                        try:
                            if(s=='s'):
                                cur.execute('INSERT INTO reviewOne (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                            else:
                                cur.execute('INSERT INTO reviewOne (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                        except:
                            messagebox.showerror("Fileupload","ERROR Aquired");

                    # Display a success message

                    upload_file()
                btn_upload=Button(page1,text='Upload here !',command=db)
                btn_upload.place(x=180,y=300)
            page1go()
        def student_review2_page():
            def page2go(): 
                page2=Frame(main_frame,width=500,height=400)
                page2.pack()
                label_page2=Label(page2,text="REVIEW 2",foreground="magenta3",font=('bold',15))
                label_page2.place(x=200,y=50)
                label2_page1=Label(page2,text="Student ID First :")
                label2_page1.place(x=10,y=100)
                usrName=Entry(page2,textvariable=no)
                usrName.place(x=110,y=100)
                label3_page1=Label(page2,text="Student ID Second :")
                label3_page1.place(x=10,y=150)
                usrNameTwo=Entry(page2,textvariable=noTwo)
                usrNameTwo.place(x=120,y=150)
                l4=Label(page2,text='Type :')
                l4.place(x=10,y=200)
                def des():
                    if(var_radio.get()=='s'):
                        usrNameTwo.config(state='disabled')
                    elif(var_radio.get()=='p'):
                        usrNameTwo.config(state='normal')

                var_radio=StringVar()
                r1=Radiobutton(page2,text='single',value='s',variable=var_radio,command=des)
                r1.place(x=85,y=200)
                r2=Radiobutton(page2,text='Pair',value='p',variable=var_radio,command=des)
                r2.place(x=140,y=200)
                var_radio.set('s')
                usrNameTwo.config(state='disabled')
                name=StringVar()
                name.set("")
                label2_page1=Label(page2,text="Title :")
                label2_page1.place(x=10,y=250)
                def dbfuntitle():
                    userID=usrName.get()
                    if(userID!=""):
                        dbtitle()
                    else:
                        messagebox.showerror("Required","Please fill the Student ID")
                def dbtitle():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    try:
                        cursor.execute("select * from student where studid1='%s'"%userID)
                        r=cursor.fetchall()
                        if r:
                            st="select * from title where userID='%s'";
                            cursor.execute(st%(userID))
                            r1=cursor.fetchall()
                            for i in r1:
                                x=str(i[2])
                            name.set(x)
                            conn.commit()
                        else :
                            cursor.execute("select * from student where studid2='%s'"%userID)
                            r=cursor.fetchall()
                            if r:
                                st="select * from title where userID2='%s'";
                                cursor.execute(st%(userID))
                                r1=cursor.fetchall()

                                for i in r1:
                                    x=str(i[2])
                                name.set(x)
                                conn.commit()
                            else:
                                messagebox.showerror("Failed",'Check the Student Id')
                    except:
                        messagebox.showerror("Failed",'Check the Student Id')
                    
                btn_found=Button(page2,text="click",command=dbfuntitle)
                btn_found.place(x=250,y=200)

                title=Entry(page2,width=100,textvariable=name)
                title.place(x=60,y=250)
                label3_page2=Label(page2,text="Second Review Submission :")
                label3_page2.place(x=10,y=300)
                def db():
                    # Connect to the database
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cur = conn.cursor()
                    userID1=usrName.get()
                    userID2=usrNameTwo.get()
                    s=var_radio.get()
                    def upload_file():

                        # Open a file dialog to select a PDF file to upload
                        from tkinter.filedialog import askopenfilename
                        file_path = askopenfilename(filetypes=[('PPT Files', '*.ppt;*.pptx;')])
                        if not file_path:
                            return
                        
                        # Extract the file name from the file path
                        import os
                        file_name = os.path.basename(file_path)

                        # Read the contents of the file
                        with open(file_path, 'rb') as file:
                            data = file.read()

                        # Insert the file into the database
                        try:
                            if(s=='s'):
                                cur.execute('INSERT INTO reviewTwo (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                            else:
                                cur.execute('INSERT INTO reviewTwo (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                        except:
                            messagebox.showerror("Fileupload","ERROR Aquired");

                    # Display a success message

                    upload_file()
                btn_upload=Button(page2,text='Upload here !',command=db)
                btn_upload.place(x=180,y=300)
            page2go()
        def student_review3_page():
            def page1go(): 
                page3=Frame(main_frame,width=500,height=400)
                page3.pack()
                label_page3=Label(page3,text="REVIEW 3",foreground="indianRed3",font=('bold',15))
                label_page3.place(x=200,y=50)
                label2_page1=Label(page3,text="Student ID First :")
                label2_page1.place(x=10,y=100)
                usrName=Entry(page3,textvariable=no)
                usrName.place(x=110,y=100)
                label3_page1=Label(page3,text="Student ID Second :")
                label3_page1.place(x=10,y=150)
                usrNameTwo=Entry(page3,textvariable=noTwo)
                usrNameTwo.place(x=120,y=150)
                l4=Label(page3,text='Type :')
                l4.place(x=10,y=200)
                def des():
                    if(var_radio.get()=='s'):
                        usrNameTwo.config(state='disabled')
                    elif(var_radio.get()=='p'):
                        usrNameTwo.config(state='normal')

                var_radio=StringVar()
                r1=Radiobutton(page3,text='single',value='s',variable=var_radio,command=des)
                r1.place(x=85,y=200)
                r2=Radiobutton(page3,text='Pair',value='p',variable=var_radio,command=des)
                r2.place(x=140,y=200)
                var_radio.set('s')
                usrNameTwo.config(state='disabled')
                name=StringVar()
                name.set("")
                label2_page1=Label(page3,text="Title :")
                label2_page1.place(x=10,y=250)
                def dbfuntitle():
                    userID=usrName.get()
                    if(userID!=""):
                        dbtitle()
                    else:
                        messagebox.showerror("Required","Please fill the Student ID")
                def dbtitle():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    try:
                        cursor.execute("select * from student where studid1='%s'"%userID)
                        r=cursor.fetchall()
                        if r:
                            st="select * from title where userID='%s'";
                            cursor.execute(st%(userID))
                            r1=cursor.fetchall()
                            for i in r1:
                                x=str(i[2])
                            name.set(x)
                            conn.commit()
                        else :
                            cursor.execute("select * from student where studid2='%s'"%userID)
                            r=cursor.fetchall()
                            if r:
                                st="select * from title where userID2='%s'";
                                cursor.execute(st%(userID))
                                r1=cursor.fetchall()

                                for i in r1:
                                    x=str(i[2])
                                name.set(x)
                                conn.commit()
                            else:
                                messagebox.showerror("Failed",'Check the Student Id')
                    except:
                        messagebox.showerror("Failed",'Check the Student Id')
                     
                    

                btn_found=Button(page3,text="click",command=dbfuntitle)
                btn_found.place(x=250,y=200)

                title=Entry(page3,width=100,textvariable=name)
                title.place(x=60,y=250)
                label3_page3=Label(page3,text="Third Review Submission :")
                label3_page3.place(x=10,y=300)
                def db():
                    # Connect to the database
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cur = conn.cursor()
                    userID1=usrName.get()
                    userID2=usrNameTwo.get()
                    s=var_radio.get()
                    def upload_file():

                        # Open a file dialog to select a PDF file to upload
                        from tkinter.filedialog import askopenfilename
                        file_path = askopenfilename(filetypes=[('PPT Files', '*.ppt;*.pptx;')])
                        if not file_path:
                            return
                        
                        # Extract the file name from the file path
                        import os
                        file_name = os.path.basename(file_path)

                        # Read the contents of the file
                        with open(file_path, 'rb') as file:
                            data = file.read()

                        # Insert the file into the database
                        try:
                            if(s=='s'):
                                cur.execute('INSERT INTO reviewThree (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                            else:
                                cur.execute('INSERT INTO reviewThree (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                        except:
                            messagebox.showerror("Fileupload","ERROR Aquired");

                    # Display a success message

                    upload_file()
                btn_upload=Button(page3,text='Upload here !',command=db)
                btn_upload.place(x=180,y=300)
            page1go()
        def student_final_page():
            def final(): 
                final=Frame(main_frame,width=500,height=400)
                final.pack()
                label_final=Label(final,text="FINAL DOCUMENTAION",foreground="lightCyan4",font=('bold',15))
                label_final.place(x=155,y=50)
                label2_page1=Label(final,text="Student ID First :")
                label2_page1.place(x=10,y=100)
                usrName=Entry(final,textvariable=no)
                usrName.place(x=110,y=100)
                label3_page1=Label(final,text="Student ID Second :")
                label3_page1.place(x=10,y=150)
                usrNameTwo=Entry(final,textvariable=noTwo)
                usrNameTwo.place(x=120,y=150)
                l4=Label(final,text='Type :')
                l4.place(x=10,y=200)
                def des():
                    if(var_radio.get()=='s'):
                        usrNameTwo.config(state='disabled')
                    elif(var_radio.get()=='p'):
                        usrNameTwo.config(state='normal')

                var_radio=StringVar()
                r1=Radiobutton(final,text='single',value='s',variable=var_radio,command=des)
                r1.place(x=85,y=200)
                r2=Radiobutton(final,text='Pair',value='p',variable=var_radio,command=des)
                r2.place(x=140,y=200)
                var_radio.set('s')
                usrNameTwo.config(state='disabled')
                name=StringVar()
                name.set("")
                label2_page1=Label(final,text="Title :")
                label2_page1.place(x=10,y=250)
                def dbfuntitle():
                    userID=usrName.get()
                    if(userID!=""):
                        dbtitle()
                    else:
                        messagebox.showerror("Required","Please fill the Student ID")
                def dbtitle():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    try:
                        cursor.execute("select * from student where studid1='%s'"%userID)
                        r=cursor.fetchall()
                        if r:
                            st="select * from title where userID='%s'";
                            cursor.execute(st%(userID))
                            r1=cursor.fetchall()
                            for i in r1:
                                x=str(i[2])
                            name.set(x)
                            conn.commit()
                        else :
                            cursor.execute("select * from student where studid2='%s'"%userID)
                            r=cursor.fetchall()
                            if r:
                                st="select * from title where userID2='%s'";
                                cursor.execute(st%(userID))
                                r1=cursor.fetchall()

                                for i in r1:
                                    x=str(i[2])
                                name.set(x)
                                conn.commit()
                            else:
                                messagebox.showerror("Failed",'Check the Student Id')
                    except:
                        messagebox.showerror("Failed",'Check the Student Id')
                btn_found=Button(final,text="click",command=dbfuntitle)
                btn_found.place(x=250,y=200)

                title=Entry(final,width=100,textvariable=name)
                title.place(x=60,y=250)
                label3_final=Label(final,text="Final Documentation Submission:")
                label3_final.place(x=10,y=300)
                def db():
                    # Connect to the database
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cur = conn.cursor()
                    userID1=usrName.get()
                    userID2=usrNameTwo.get()
                    s=var_radio.get()
                    def upload_file():

                        # Open a file dialog to select a PDF file to upload
                        from tkinter.filedialog import askopenfilename
                        file_path = askopenfilename(filetypes=[('PDF Files', '*.pdf')])
                        if not file_path:
                            return
                        
                        # Extract the file name from the file path
                        import os
                        file_name = os.path.basename(file_path)

                        # Read the contents of the file
                        with open(file_path, 'rb') as file:
                            data = file.read()

                        # Insert the file into the database
                        try:
                            if(s=='s'):
                                cur.execute('INSERT INTO final (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                            else:
                                cur.execute('INSERT INTO final (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                        except:
                            messagebox.showerror("Fileupload","ERROR Aquired");

                    # Display a success message

                    upload_file()
                btn_upload=Button(final,text='Upload here !',command=db)
                btn_upload.place(x=200,y=300)
            final()
            
        def Mark_View_page():
            mark_frame=Frame(main_frame,width=500,height=400)
            mark_frame.pack()
            
            label_mark=Label(mark_frame,text='MARK',foreground="saddlebrown",font=('bold',15))
            label_mark.place(x=200,y=50)
            label_mark=Label(mark_frame,text='Student Id')
            label_mark.place(x=10,y=100)
            usrName=Entry(mark_frame,textvariable=no)
            usrName.place(x=120,y=100)
            
            dept=Label(mark_frame,text='Department :')
            dept.place(x=10,y=140)
            stucombo2=ttk.Combobox(mark_frame)
            stucombo2.place(x=120,y=140)
            stucombo2.config(values=('CS','IT','CA','DS','BBA','CGS','MATHS','PHY','CH','EN','TAMIL','PSY','B.com-BPS','B.com-CA','B.com-PA','B.com','B.com-HONOURS','BIOTECH','MICRO-BIOLOGY','ZOLOGY'))
            stucombo2.set('--- select option ---')

            studentstream=Label(mark_frame,text='Stream :')
            studentstream.place(x=10,y=170)
            stucombo3=ttk.Combobox(mark_frame)
            stucombo3.place(x=120,y=170)
            stucombo3.config(values=('Aided','SF'))
            stucombo3.set('--- select option ---')

            batch=Label(mark_frame,text='Batch :')
            batch.place(x=10,y=210)
            stucombo1=ttk.Combobox(mark_frame)
            stucombo1.place(x=120,y=210)
            stucombo1.config(values=('2019','2020','2021','2021','2022','2023'))
            stucombo1.set('--- select option ---')

            def db():
                conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                cur = conn.cursor()
                userId=usrName.get()
                s=stucombo2.get()
                s1=stucombo3.get()
                s2=stucombo1.get()

                if(s=='--- select option ---' or s1=='--- select option ---' or s2=='--- select option ---'):
                    messagebox.showerror("Required","Please fill the Entry")
                elif(userId ==""):
                    messagebox.showerror("Required","Please Fill the Student Id")                    

                else:
                    try:
                        cur.execute("select * from student where studid1='%s' and dept='%s' and stream='%s' and batch='%s'"%(userId,s,s1,s2))
                        r=cur.fetchall()
                        if r:
                            cur.execute("select * from reviewmark where userId='%s'"%userId)
                            e=cur.fetchall()
                            for i in e:
                                x=str(i[4])
                                y=str(i[5])
                                z=str(i[6])
                                w=str(i[7])
                            reviewone.set(x)
                            reviewTwo.set(y)
                            reviewThree.set(z)
                            totalMark.set(w)
                        else:
                            cur.execute("Select * from student where studid2='%s' and dept='%s' and stream='%s' and batch='%s'"%(userId,s,s1,s2))
                            r=cur.fetchall()
                            if r:
                                cur.execute("select * from reviewmark where userId='%s'"%userId)
                                e=cur.fetchall()
                                for i in e:
                                    x=str(i[4])
                                    y=str(i[5])
                                    z=str(i[6])
                                    w=str(i[7])
                                reviewone.set(x)
                                reviewTwo.set(y)
                                reviewThree.set(z)
                                totalMark.set(w)
                            else:
                                messagebox.showerror("Failed","Review Mark can not Defined")

                    except:
                        messagebox.showerror("Failed","Review Mark can not Defined")
                

            btn=Button(mark_frame,text="get",command=db)
            btn.place(x=120,y=240)   
            reviewone=StringVar()
            reviewone.set("")
            label_mark=Label(mark_frame,text='Review one Mark :')
            label_mark.place(x=10,y=280)
            ReviewOne=Entry(mark_frame,textvariable=reviewone)
            ReviewOne.place(x=120,y=280)
            reviewTwo=StringVar()
            reviewTwo.set("")
            label_mark=Label(mark_frame,text='Review two mark :')
            label_mark.place(x=10,y=320)
            ReviewTwo=Entry(mark_frame,textvariable=reviewTwo)
            ReviewTwo.place(x=120,y=320)
            reviewThree=StringVar()
            reviewThree.set("")
            label_mark=Label(mark_frame,text='Review three mark :')
            label_mark.place(x=10,y=360)
            ReviewThree=Entry(mark_frame,textvariable=reviewThree)
            ReviewThree.place(x=120,y=360)
            totalMark=StringVar()
            totalMark.set("")
            label_mark=Label(mark_frame,text='Total Mark :')
            label_mark.place(x=260,y=320)
            total=Entry(mark_frame,textvariable=totalMark)
            total.place(x=330,y=320)
    
        def student_Report_page():
            def Report(): 
                Report=Frame(main_frame,width=500,height=400)
                Report.pack()
                label_Report=Label(Report,text="REPORT",foreground="SeaGreen4",font=('bold',15))
                label_Report.place(x=155,y=50)
                label2_page1=Label(Report,text="Student ID First :")
                label2_page1.place(x=10,y=100)
                usrName=Entry(Report,textvariable=no)
                usrName.place(x=110,y=100)
                label3_page1=Label(Report,text="Student ID Second :")
                label3_page1.place(x=10,y=150)
                usrNameTwo=Entry(Report,textvariable=noTwo)
                usrNameTwo.place(x=120,y=150)
                l4=Label(Report,text='Type :')
                l4.place(x=10,y=200)
                def des():
                    if(var_radio.get()=='s'):
                        usrNameTwo.config(state='disabled')
                    elif(var_radio.get()=='p'):
                        usrNameTwo.config(state='normal')

                var_radio=StringVar()
                r1=Radiobutton(Report,text='single',value='s',variable=var_radio,command=des)
                r1.place(x=85,y=200)
                r2=Radiobutton(Report,text='Pair',value='p',variable=var_radio,command=des)
                r2.place(x=140,y=200)
                var_radio.set('s')
                usrNameTwo.config(state='disabled')
                name=StringVar()
                name.set("")
                label2_page1=Label(Report,text="Title :")
                label2_page1.place(x=10,y=250)
                def dbfuntitle():
                    userID=usrName.get()
                    if(userID!=""):
                        dbtitle()
                    else:
                        messagebox.showerror("Required","Please fill the Student ID")
                def dbtitle():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    try:
                        cursor.execute("select * from student where studid1='%s'"%userID)
                        r=cursor.fetchall()
                        if r:
                            st="select * from title where userID='%s'";
                            cursor.execute(st%(userID))
                            r1=cursor.fetchall()
                            for i in r1:
                                x=str(i[2])
                            name.set(x)
                            conn.commit()
                        else :
                            cursor.execute("select * from student where studid2='%s'"%userID)
                            r=cursor.fetchall()
                            if r:
                                st="select * from title where userID2='%s'";
                                cursor.execute(st%(userID))
                                r1=cursor.fetchall()

                                for i in r1:
                                    x=str(i[2])
                                name.set(x)
                                conn.commit()
                            else:
                                messagebox.showerror("Failed",'Check the Student Id')
                    except:
                        messagebox.showerror("Failed",'Check the Student Id')
                btn_found=Button(Report,text="click",command=dbfuntitle)
                btn_found.place(x=250,y=200)

                title=Entry(Report,width=100,textvariable=name)
                title.place(x=60,y=250)
                label3_final=Label(Report,text="Report Submission:")
                label3_final.place(x=10,y=300)
                def db():
                    # Connect to the database
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cur = conn.cursor()
                    userID1=usrName.get()
                    userID2=usrNameTwo.get()
                    s=var_radio.get()
                    def upload_file():

                        # Open a file dialog to select a PDF file to upload
                        from tkinter.filedialog import askopenfilename
                        file_path = askopenfilename(filetypes=[('PDF Files', '*.pdf')])
                        if not file_path:
                            return
                        
                        # Extract the file name from the file path
                        import os
                        file_name = os.path.basename(file_path)

                        # Read the contents of the file
                        with open(file_path, 'rb') as file:
                            data = file.read()

                        # Insert the file into the database
                        try:
                            if(s=='s'):
                                cur.execute('INSERT INTO StudentReport (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                            else:
                                cur.execute('INSERT INTO StudentReport (userID,userID2,name, data) VALUES (%s,%s,%s, %s)', (userID1,userID2,file_name, data))
                                conn.commit()
                                message = f"The file '{file_name}' was uploaded successfully."
                                messagebox.showinfo("File Upload", message)
                        except:
                            messagebox.showerror("Fileupload","ERROR Aquired");

                    # Display a success message

                    upload_file()
                btn_upload=Button(Report,text='Upload here !',command=db)
                btn_upload.place(x=200,y=300)
            Report()

        #hide-indication of other button 
        def hide_indicate():
           
            home_indicate.config(bg="grey")
            student_Abstract_indicate.config(bg='grey')
            student_proposal_indicate.config(bg='grey')
            student_review1_indicate.config(bg='grey')
            student_review2_indicate.config(bg='grey')
            student_review3_indicate.config(bg='grey')
            student_final_indicate.config(bg='grey')
            student_mark_indicate.config(bg='grey')
            student_Report_indicate.config(bg='grey')

        #solve the problem of overlapping the text
        def delete_page():
            #winfo children is method that access the method current Object
            for frame in main_frame.winfo_children():
                frame.destroy()
        #show-indicstion of current button
        def indicate(self,page):
            hide_indicate()
            self.config(bg='blue')
            delete_page()
            page()

        

        option_frame=Frame(root,bg="grey")

        #button
        home_btn=Button(option_frame,text='HOME',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(home_indicate,home_page))
        home_btn.place(x=10,y=50)
        

        home_indicate=Label(option_frame,text='',bg='grey')
        home_indicate.place(x=3,y=50,width=5,height=40)

        student_Abstract=Button(option_frame,text='Abstract',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_Abstract_indicate,student_Abstract_page))
        student_Abstract.place(x=10,y=100)

        student_Abstract_indicate=Label(option_frame,text='',bg='grey')
        student_Abstract_indicate.place(x=3,y=100,width=5,height=40)

        student_proposal=Button(option_frame,text='Proposal',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_proposal_indicate,student_proposal_page))
        student_proposal.place(x=10,y=150)

        student_proposal_indicate=Label(option_frame,text='',bg='grey')
        student_proposal_indicate.place(x=3,y=150,width=5,height=40)

        student_review1=Button(option_frame,text='Review 1',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_review1_indicate,student_review1_page))
        student_review1.place(x=10,y=200)

        student_review1_indicate=Label(option_frame,text='',bg='grey')
        student_review1_indicate.place(x=3,y=200,width=5,height=40)



        student_review2=Button(option_frame,text='Review 2',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_review2_indicate,student_review2_page))
        student_review2.place(x=10,y=250)

        student_review2_indicate=Label(option_frame,text='',bg='grey')
        student_review2_indicate.place(x=3,y=250,width=5,height=40)

        student_review3=Button(option_frame,text='Review 3',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_review3_indicate,student_review3_page))
        student_review3.place(x=10,y=300)

        student_review3_indicate=Label(option_frame,text='',bg='grey')
        student_review3_indicate.place(x=3,y=300,width=5,height=40)

        student_final=Button(option_frame,text='Final Docs',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_final_indicate,student_final_page))
        student_final.place(x=10,y=350)

        student_final_indicate=Label(option_frame,text='',bg='grey')
        student_final_indicate.place(x=3,y=350,width=5,height=40)

        student_Mark=Button(option_frame,text='Mark',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_mark_indicate,Mark_View_page))
        student_Mark.place(x=10,y=400)

        student_mark_indicate=Label(option_frame,text='',bg='grey')
        student_mark_indicate.place(x=3,y=400,width=5,height=40)

        student_Report=Button(option_frame,text='Report',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_Report_indicate,student_Report_page))
        student_Report.place(x=10,y=450)

        student_Report_indicate=Label(option_frame,text='',bg='grey')
        student_Report_indicate.place(x=3,y=450,width=5,height=40)

        option_frame.pack(side=LEFT)
        option_frame.pack_propagate(False)
        option_frame.configure(width=120,height=500)


        main_frame=Frame(root,highlightbackground='black',highlightthickness=2)


        main_frame.pack()
        main_frame.pack_propagate(False)
        main_frame.configure(width=600,height=520)
    student_login_page()

#home page for all user !
def mentor_login(x):
    def mentor_Page():
        no.set(x)
        def logout():
            main_frame.destroy()
            option_frame.destroy()
            registeration_login()
        
        def home_page():
            home_frame=Frame(main_frame,width=500,height=500)
            home_frame.pack()

            logout_btn=Button(home_frame,text="LOGOUT",bd=0,fg='red',
                          command=logout)
            logout_btn.place(x=450,y=20)
            label_mark=Label(home_frame,text='Home',foreground="saddlebrown",font=('bold',15))
            label_mark.place(x=200,y=50)
            label_mark=Label(home_frame,text='Mentor Id')
            label_mark.place(x=10,y=80)
            
            usrName=Entry(home_frame,textvariable=no)
            usrName.place(x=120,y=80)

            deptm=StringVar()
            deptm.set("")
        
            dept=Label(home_frame,text='Course :')
            dept.place(x=10,y=110)
            depatment=Entry(home_frame,textvariable=deptm)
            depatment.place(x=120,y=110)

            strm=StringVar()
            strm.set("")
        
            studentstream=Label(home_frame,text='Stream :')
            studentstream.place(x=10,y=140)
            stream=Entry(home_frame,textvariable=strm)
            stream.place(x=120,y=140)

            guide=StringVar()
            guide.set("")
            label_mark=Label(home_frame,text='Total Guide :')
            label_mark.place(x=10,y=180)
            gu=Entry(home_frame,textvariable=guide)
            gu.place(x=120,y=180)
        
            student=StringVar()
            student.set("")
            label_mark=Label(home_frame,text='Total Student :')
            label_mark.place(x=10,y=220)
            st=Entry(home_frame,textvariable=student)
            st.place(x=120,y=220)
            
            girls=StringVar()
            girls.set("")
            label_mark=Label(home_frame,text='Total girls :')
            label_mark.place(x=10,y=250)
            g=Entry(home_frame,textvariable=girls)
            g.place(x=120,y=250)
            
            boys=StringVar()
            boys.set("")
            label_mark=Label(home_frame,text='Total Boys :')
            label_mark.place(x=10,y=280)
            b=Entry(home_frame,textvariable=boys)
            b.place(x=120,y=280)
                        
            single=StringVar()
            single.set("")
            label_mark=Label(home_frame,text='Total Single Project Students :')
            label_mark.place(x=10,y=310)
            sin=Entry(home_frame,textvariable=single)
            sin.place(x=180,y=310)


            pair=StringVar()
            pair.set("")
            label_mark=Label(home_frame,text='Total Pair Project Students :')
            label_mark.place(x=10,y=340)
            pa=Entry(home_frame,textvariable=pair)
            pa.place(x=180,y=340)

            def db():
                conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                cur = conn.cursor()
                userId=usrName.get()
                deptm.set("")
                strm.set("")
                guide.set("")
                student.set("")
                single.set("")
                pair.set("")
                girls.set("")
                boys.set("")
                if(userId!=""):
                    try:
                        cur.execute("select * from mentor where mid='%s'"%userId)
                        r=cur.fetchall()
                        if r:
                            for i in r:
                                x=str(i[0])
                                y=str(i[1])
                            
                            deptm.set(x)
                            strm.set(y)
                            try:
                                cur.execute("select count(*) from guide where depart='%s' and stream='%s'"%(x,y))
                                count=cur.fetchall()
                                for i in count:
                                    cou=str(i[0])
                                guide.set(cou)
                            except:
                                pass

                            try:
                                cur.execute("select count(*) from student where type='s' and gender='m' and dept='%s' and stream='%s'"%(x,y))
                                bsin=cur.fetchall()
                                for i in bsin:
                                    boyssinglecount=str(i[0])
                                cur.execute("select count(*) from student where type='p' and gender='m' and dept='%s' and stream='%s'"%(x,y))
                                bpair=cur.fetchall()
                                for i in bpair:
                                    boyspaircount=str(i[0])

                                c=int(boyssinglecount)+(int(boyspaircount)*2)
                                boys.set(c)
                            except:
                                pass

                            try:
                                cur.execute("select count(*) from student where type='s' and gender='f' and dept='%s' and stream='%s'"%(x,y))
                                gsin=cur.fetchall()
                                for i in gsin:
                                    girlssinglecount=str(i[0])
                                cur.execute("select count(*) from student where type='p' and gender='f' and dept='%s' and stream='%s'"%(x,y))
                                gpair=cur.fetchall()
                                for i in gpair:
                                    girlspaircount=str(i[0])
                                c=int(girlssinglecount)+(int(girlspaircount)*2)
                                girls.set(c)
                            except:
                                pass
                            
                            try:
                                cur.execute("select count(*) from student where type='s' and dept='%s' and stream='%s'"%(x,y))
                                count=cur.fetchall()
                                for i in count:
                                    singlecount=str(i[0])
                                single.set(singlecount)
                            except:
                                pass
                            try:
                                cur.execute("select count(*) from student where type='p' and dept='%s' and stream='%s'"%(x,y))
                                count=cur.fetchall()
                                for i in count:
                                    paircount=str(i[0])
                                pair.set(paircount)
                            except:
                                pass
                            try:
                                xc=int(singlecount)+(int(paircount)*2)
                                student.set(xc)
                            except:
                                pass 
                                
                        else:
                            messagebox.showerror("Failed","Please Varify your Mentor Id")
                    except:
                        messagebox.showerror("Failed","Mentor ID can not Defined")
                else:
                    messagebox.showerror("Failed","Please Fill the Entry")

            btn=Button(home_frame,text="Click",command=db)
            btn.place(x=300,y=95)   

        
        
    
            home_frame.pack()
        def Guide_Details_page():
        
            f=Frame(main_frame,width=600,height=520)
            f.pack()

            lb=Label(f,text='Guide Details',font=('bold',15))
            lb.place(x=155,y=10)
    
            stream=Label(f,text="Stream :")
            stream.place(x=10,y=50)
            streamCombobox=ttk.Combobox(f)
            streamCombobox.place(x=65,y=50)
            streamCombobox.config(values=('AIDED','SF'))
            streamCombobox.set('--- Select option ---')

            de=Label(f,text='Course :')
            de.place(x=250,y=50)
            staffcombo2=ttk.Combobox(f)
            staffcombo2.place(x=315,y=50)
            staffcombo2.config(values=('CS','IT','CA','DS','BBA','CGS','MATHS','PHY','CH','EN','TAMIL','PSY','B.com-BPS','B.com-CA','B.com-PA','B.com','B.com-HONOURS','BIOTECH','MICRO-BIOLOGY','ZOLOGY'))
            staffcombo2.set('---Select option ---')
            def fun():
                s1=streamCombobox.get()
                s2=staffcombo2.get()
                if(s1=="--- Select option ---" or s2=="--- Select option ---"  or s1=="" or s2=="" ):
                    messagebox.showerror("Failed","Please fill the Entry")
                else:
                    db(s2,s1)
        
            def db(s1,s2):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()

                st="select * from guide where depart='%s' AND stream='%s'"
                a=(s1,s2)
                try:
                    cursor.execute(st%a)
                except:
                    messagebox.showerror('Search Error',"Failed")
                tree.delete(*tree.get_children())
                for i in cursor:
                    tree.insert('',END,text='',values=(i[2],i[3],i[4]))
              
            tree =ttk.Treeview(f,show='headings',height=15)
            tree["columns"]=("Name","Idno","Gmail")
            tree.column("Name",width=150,anchor=CENTER)
            tree.column("Idno",width=50,anchor=CENTER)
            tree.column("Gmail",width=300,anchor=CENTER)
            tree.heading("Name",text="Name",anchor=CENTER)
            tree.heading("Idno",text="Idno",anchor=CENTER)
            tree.heading("Gmail",text="Gmail",anchor=CENTER)
            s=ttk.Style(root)
            s.theme_use("vista")
            s.configure(".",font=("Helvetica",11))
            s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,"bold"))
            tree.place(x=30,y=100) 
            hsb=ttk.Scrollbar(main_frame,orient="vertical")
            hsb.configure(command=tree.yview)
            tree.configure(yscrollcommand=hsb.set)
            hsb.pack(fill=Y,side=RIGHT)
            btn=Button(f,text="Submit",command=fun)
            btn.place(x=490,y=45)
      
        
        def Student_Details_page():
            Std=Frame(main_frame,width=600,height=520)
            Std.pack()
            lb=Label(Std,text='Student Details',font=('bold',15))
            lb.place(x=155,y=10)
            batch=Label(Std,text='Batch :')
            batch.place(x=10,y=50)
            stucombo1=ttk.Combobox(Std)
            stucombo1.place(x=55,y=50)
            stucombo1.config(values=('2019','2020','2021','2021','2022','2023'))
            stucombo1.set('---select option ---')


            stream=Label(Std,text="Stream :")
            stream.place(x=10,y=80)
            streamCombobox=ttk.Combobox(Std)
            streamCombobox.place(x=65,y=80)
            streamCombobox.config(values=('Aided','SF'))
            streamCombobox.set('--- Select option ---')

            de=Label(Std,text='Course :')
            de.place(x=250,y=50)
            stucombo2=ttk.Combobox(Std)
            stucombo2.place(x=315,y=50)
            stucombo2.config(values=('CS','IT','CA','DS','BBA','CGS','MATHS','PHY','CH','EN','TAMIL','PSY','B.com-BPS','B.com-CA','B.com-PA','B.com','B.com-HONOURS','BIOTECH','MICRO-BIOLOGY','ZOLOGY'))
            stucombo2.set('---Select option ---')
            def fun():
                s1=stucombo1.get()
                s2=streamCombobox.get()
                s3=stucombo2.get()
                if(s1=="--- Select option ---" or s2=="--- Select option ---" or s3=="--- Select option ---" or s1=="" or s2=="" or s3=="" ):
                    messagebox.showerror("Failed","Please fill the Entry")
                else:
                    db(s3,s1,s2)
            
            def db(s1,s2,s3):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
    
                st="select * from student where dept='%s'AND batch='%s' AND stream='%s'"
                a=(s1,s2,s3)
                cursor.execute(st%a)
                tree.delete(*tree.get_children())
                for i in cursor:
                    tree.insert('',END,text='',values=(i[2],i[3],i[10],i[11],i[5]))
          
            tree =ttk.Treeview(Std,show='headings',height=15)
            tree["columns"]=("Name","Idno","Name2","Idno2","Type")
            tree.column("Name",width=150,anchor=CENTER)
            tree.column("Idno",width=100,anchor=CENTER)
            tree.column("Name2",width=150,anchor=CENTER)
            tree.column("Idno2",width=100,anchor=CENTER)
            tree.column("Type",width=50,anchor=CENTER)
        
            tree.heading("Name",text="Name",anchor=CENTER)
            tree.heading("Idno",text="Idno",anchor=CENTER)
            tree.heading("Name2",text="Name2",anchor=CENTER)
            tree.heading("Idno2",text="Idno2",anchor=CENTER)
            tree.heading("Type",text="Type",anchor=CENTER)
        
            s=ttk.Style(root)
            s.theme_use("vista")
            s.configure(".",font=("Helvetica",11))
            s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,"bold"))
            tree.place(x=10,y=130) 
            hsb=ttk.Scrollbar(main_frame,orient="vertical")
            hsb.configure(command=tree.yview)
            tree.configure(yscrollcommand=hsb.set)
            hsb.pack(fill=Y,side=RIGHT)
            hsb2=ttk.Scrollbar(main_frame,orient="vertical")
            hsb2.configure(command=tree.xview)
            tree.configure(xscrollcommand=hsb2.set)
            hsb2.pack(fill=X,side=BOTTOM)
            btn=Button(Std,text="Submit",command=fun)
            btn.place(x=290,y=80)
    
 
        def Allocation_page():
            allocation=Frame(main_frame,width=500,height=400)
            allocation.pack()
            lb=Label(allocation,text='Allocating Boys To Guide',font=('bold',15))
            lb.place(x=155,y=30)
        
            batch=Label(allocation,text='Batch :')
            batch.place(x=10,y=80)
            stucombo1=ttk.Combobox(allocation)
            stucombo1.place(x=55,y=80)
            stucombo1.config(values=('2019','2020','2021','2022','2023','2024'))
            stucombo1.set('---select option ---')

            gend=StringVar()
            gend.set('m')
            gender=Label(allocation,text="Gender :")
            gender.place(x=250,y=120)
            gen=Entry(allocation,textvariable=gend)
            gen.place(x=315,y=120)

            stream=Label(allocation,text="Stream :")
            stream.place(x=10,y=120)
            streamCombobox=ttk.Combobox(allocation)
            streamCombobox.place(x=65,y=120)
            streamCombobox.config(values=('Aided','SF'))
            streamCombobox.set('--- Select option ---')

            de=Label(allocation,text='Course :')
            de.place(x=250,y=80)
            stucombo2=ttk.Combobox(allocation)
            stucombo2.place(x=315,y=80)
            stucombo2.config(values=('CS','IT','CA','DS','BBA','CGS','MATHS','PHY','CH','EN','TAMIL','PSY','B.com-BPS','B.com-CA','B.com-PA','B.com','B.com-HONOURS','BIOTECH','MICRO-BIOLOGY','ZOLOGY'))
            stucombo2.set('---Select option ---')

            def Allocate():

                batch=stucombo1.get()
                stream=streamCombobox.get()
                dept=stucombo2.get()
                gender=gen.get()
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                single=[]
                pair=[]
                teacher=[]
                singleallocate=[]
                singleConcat=[]
                pairallocate=[]
                pairConcat=[]
                def retrivesingle(dept,batch,stream,gender):
    
                    st="select * from student where type='s' and dept='%s' and batch='%s' and stream='%s' and gender='%s'"
                    a=(dept,batch,stream,gender)
                    cursor.execute(st%a)
                    rows=cursor.fetchall()
                    for i in rows:
                        x=str(i[3])
                        single.append(x)
                    ##print("SINGLE :",single)
                    con.commit()
                def retrivepair(dept,batch,stream,gender):
    
                    st="select * from student where type='p' and dept='%s' and batch='%s' and stream='%s' and gender='%s'"
                    a=(dept,batch,stream,gender)
                    cursor.execute(st%a)
                    rows=cursor.fetchall()
                    for i in rows:
                        x=str(i[3])
                        y=str(i[11])
                        pair.append([x,y])
                    ##print("PAIR :",pair)
                    con.commit()
                def retriveguide(dept,stream):
    
                    st="select * from guide where depart='%s' and stream='%s'"
                    a=(dept,stream)
                    cursor.execute(st%a)
                    rows=cursor.fetchall()
                    for i in rows:
                        x=str(i[2])
                        teacher.append(x)
                    ##print("Guide :",teacher)
                    con.commit()

                def grouping():
                    single.sort()
                    ##print(single)
                    teacher.sort()
                    random.shuffle(single)
                    ##print("Shuffle :",single)
                    avg=len(single)//len(teacher)
                    c=0
                    for i in range(avg):
                        for j in range(len(teacher)):
                            singleConcat=[teacher[j],single[c]]
                            singleallocate.append(singleConcat)
                            c+=1
                    m=0
                    for i in range(c+1,len(single)+1):
                        singleConcat=[teacher[m],single[c]]
                        singleallocate.append(singleConcat)
                        c+=1
                        m+=1
    
                    pair.sort()
                    teacher.sort(reverse=True)
                    random.shuffle(pair)
                    ##print("Shuffle :",pair)
                    avg=len(pair)//len(teacher)
                    c=0
                    for i in range(avg):
                        for j in range(len(teacher)):
                            pairConcat=[teacher[j],pair[c]]
                            pairallocate.append(pairConcat)
                            c+=1
                    m=0
                    for i in range(c+1,len(pair)+1):
                        pairConcat=[teacher[m],pair[c]]
                        pairallocate.append(pairConcat)
                        c+=1
                        m+=1

               #insert into database
                    ##print(singleallocate)
                    for item in singleallocate:
                        guide = item[0]
                        stud1 = item[1]
                        stud2 ="" 
                        cursor.execute("insert into allocation(batch,dept,stream,guide,student1,student2,gender) values ('%s','%s','%s','%s','%s','%s','%s')"%(batch,dept,stream,guide,stud1,stud2,gender))
                        con.commit()
                    ##print("ss")
                    ##print(pairallocate)
                    for item in pairallocate:
                        guide = item[0]
                        stud1 = item[1][0]
                        stud2 = item[1][1]
                        cursor.execute("insert into allocation(batch,dept,stream,guide,student1,student2,gender) values ('%s','%s','%s','%s','%s','%s','%s')"%(batch,dept,stream,guide,stud1,stud2,gender))
                        con.commit()
                    ##print("ps")
                if(batch=="--- Select option ---" or dept=="--- Select option ---" or stream=="--- Select option ---" or gender!="m"):
                    messagebox.showerror("Failed","please Fill the Entry")
                else:
                    retrivesingle(dept,batch,stream,gender)
                    retrivepair(dept,batch,stream,gender)
                    retriveguide(dept,stream)
                    grouping()
                
    

            def fun():
                s1=stucombo1.get()
                s2=streamCombobox.get()
                s3=stucombo2.get()
                s4=gen.get()
                Allocate()
                db(s3,s1,s2,s4)
                
            def db(s1,s2,s3,s4):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                if(s1=="--- Select option ---" or s2=="--- Select option ---" or s3=="--- Select option ---" or s4!='m'):
                    messagebox.showerror("Failed","Please fill the Entry")
                else:
                    try:
                        st="select * from allocation where dept='%s'AND batch='%s' AND stream='%s' and gender='%s'"
                        a=(s1,s2,s3,s4)
                        cursor.execute(st%a)
                    except:
                        messagebox.showerror("failed","Allcation fails")
                    tree.delete(*tree.get_children())
                    for i in cursor:
                        tree.insert('',END,text='',values=(i[3],i[4],i[5]))
                
            tree =ttk.Treeview(allocation,show='headings',height=8)
            tree["columns"]=("Guide IdNo","Student1 IdNo","Student2 IdNo")
            tree.column("Guide IdNo",width=150,anchor=CENTER)
            tree.column("Student1 IdNo",width=100,anchor=CENTER)
            tree.column("Student2 IdNo",width=150,anchor=CENTER)
        
            tree.heading("Guide IdNo",text="Guide IdNo",anchor=CENTER)
            tree.heading("Student1 IdNo",text="Student1 IdNo",anchor=CENTER)
            tree.heading("Student2 IdNo",text="Student2 IdNo",anchor=CENTER)

        
            s=ttk.Style(root)
            s.theme_use("vista")
            s.configure(".",font=("Helvetica",11))
            s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,"bold"))
            tree.place(x=10,y=200) 

            btn=Button(allocation,text="Submit & show",command=fun)
            btn.place(x=290,y=150)
            def fun2():
                s1=stucombo1.get()
                s2=streamCombobox.get()
                s3=stucombo2.get()
                s4=gen.get()
                db(s3,s1,s2,s4)
            btn=Button(allocation,text="Show",command=fun2)
            btn.place(x=420,y=370)




        def Allocation_girls_page():
            allocation=Frame(main_frame,width=500,height=400)
            allocation.pack()
            lb=Label(allocation,text='Allocating Girls To Guide',font=('bold',15))
            lb.place(x=155,y=30)
        
            batch=Label(allocation,text='Batch :')
            batch.place(x=10,y=80)
            stucombo1=ttk.Combobox(allocation)
            stucombo1.place(x=55,y=80)
            stucombo1.config(values=('2019','2020','2021','2021','2022','2023'))
            stucombo1.set('---select option ---')


            stream=Label(allocation,text="Stream :")
            stream.place(x=10,y=120)
            streamCombobox=ttk.Combobox(allocation)
            streamCombobox.place(x=65,y=120)
            streamCombobox.config(values=('Aided','SF'))
            streamCombobox.set('--- Select option ---')

            gend=StringVar()
            gend.set('f')
            gender=Label(allocation,text="Gender :")
            gender.place(x=250,y=120)
            gen=Entry(allocation,textvariable=gend)
            gen.place(x=315,y=120)

            de=Label(allocation,text='Course :')
            de.place(x=250,y=80)
            stucombo2=ttk.Combobox(allocation)
            stucombo2.place(x=315,y=80)
            stucombo2.config(values=('CS','IT','CA','DS','BBA','CGS','MATHS','PHY','CH','EN','TAMIL','PSY','B.com-BPS','B.com-CA','B.com-PA','B.com','B.com-HONOURS','BIOTECH','MICRO-BIOLOGY','ZOLOGY'))
            stucombo2.set('---Select option ---')

            def Allocate():

                batch=stucombo1.get()
                stream=streamCombobox.get()
                dept=stucombo2.get()
                gender=gen.get()
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                single=[]
                pair=[]
                teacher=[]
                singleallocate=[]
                singleConcat=[]
                pairallocate=[]
                pairConcat=[]
                def retrivesingle(dept,batch,stream,gender):
    
                    st="select * from student where type='s' and dept='%s' and batch='%s' and stream='%s' and gender='%s'"
                    a=(dept,batch,stream,gender)
                    cursor.execute(st%a)
                    rows=cursor.fetchall()
                    for i in rows:
                        x=str(i[3])
                        single.append(x)
                    #print("SINGLE :",single)
                    con.commit()
                def retrivepair(dept,batch,stream,gender):
    
                    st="select * from student where type='p' and dept='%s' and batch='%s' and stream='%s' and gender='%s'"
                    a=(dept,batch,stream,gender)
                    cursor.execute(st%a)
                    rows=cursor.fetchall()
                    for i in rows:
                        x=str(i[3])
                        y=str(i[11])
                        pair.append([x,y])
                    #print("PAIR :",pair)
                    con.commit()
                def retriveguide(dept,stream):
    
                    st="select * from guide where depart='%s' and stream='%s'"
                    a=(dept,stream)
                    cursor.execute(st%a)
                    rows=cursor.fetchall()
                    for i in rows:
                        x=str(i[2])
                        teacher.append(x)
                    #print("Guide :",teacher)
                    con.commit()

                def grouping():
                    single.sort()
                    ##print(single)
                    teacher.sort()
                    random.shuffle(single)
                    ##print("Shuffle :",single)
                    avg=len(single)//len(teacher)
                    c=0
                    for i in range(avg):
                        for j in range(len(teacher)):
                            singleConcat=[teacher[j],single[c]]
                            singleallocate.append(singleConcat)
                            c+=1
                    m=0
                    for i in range(c+1,len(single)+1):
                        singleConcat=[teacher[m],single[c]]
                        singleallocate.append(singleConcat)
                        c+=1
                        m+=1
    
                    pair.sort()
                    teacher.sort(reverse=True)
                    random.shuffle(pair)
                    ##print("Shuffle :",pair)
                    avg=len(pair)//len(teacher)
                    c=0
                    for i in range(avg):
                        for j in range(len(teacher)):
                            pairConcat=[teacher[j],pair[c]]
                            pairallocate.append(pairConcat)
                            c+=1
                    m=0
                    for i in range(c+1,len(pair)+1):
                        pairConcat=[teacher[m],pair[c]]
                        pairallocate.append(pairConcat)
                        c+=1
                        m+=1

               #insert into database
                    ##print(singleallocate)
                    for item in singleallocate:
                        guide = item[0]
                        stud1 = item[1]
                        stud2 ="" 
                        cursor.execute("insert into allocation(batch,dept,stream,guide,student1,student2,gender) values ('%s','%s','%s','%s','%s','%s','%s')"%(batch,dept,stream,guide,stud1,stud2,gender))
                        con.commit()
                    ##print("ss")
                    ##print(pairallocate)
                    for item in pairallocate:
                        guide = item[0]
                        stud1 = item[1][0]
                        stud2 = item[1][1]
                        cursor.execute("insert into allocation(batch,dept,stream,guide,student1,student2,gender) values ('%s','%s','%s','%s','%s','%s','%s')"%(batch,dept,stream,guide,stud1,stud2,gender))
                        con.commit()
                    ##print("ps")
                if(batch=="--- Select option ---" or dept=="--- Select option ---" or stream=="--- Select option ---" or gender!="f"):
                    messagebox.showerror("Failed","please Fill the Entry")
                else:
                    retrivesingle(dept,batch,stream,gender)
                    retrivepair(dept,batch,stream,gender)
                    retriveguide(dept,stream)
                    grouping()
                
    

            def fun():
                s1=stucombo1.get()
                s2=streamCombobox.get()
                s3=stucombo2.get()
                s4=gen.get()
                Allocate()
                db(s3,s1,s2,s4)


                
            
            def db(s1,s2,s3,s4):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                if(s1=="--- Select option ---" or s2=="--- Select option ---" or s3=="--- Select option ---" or s4!="f"):
                    messagebox.showerror("Failed","Please fill the Entry")
                else:
                    try:
                        st="select * from allocation where dept='%s'AND batch='%s' AND stream='%s' and gender='%s'"
                        a=(s1,s2,s3,s4)
                        cursor.execute(st%a)
                    except:
                        messagebox.showerror("failed","Allcation fails")
                    tree.delete(*tree.get_children())
                    for i in cursor:
                        tree.insert('',END,text='',values=(i[3],i[4],i[5]))
                
            tree =ttk.Treeview(allocation,show='headings',height=8)
            tree["columns"]=("Guide IdNo","Student1 IdNo","Student2 IdNo")
            tree.column("Guide IdNo",width=150,anchor=CENTER)
            tree.column("Student1 IdNo",width=100,anchor=CENTER)
            tree.column("Student2 IdNo",width=150,anchor=CENTER)
        
            tree.heading("Guide IdNo",text="Guide IdNo",anchor=CENTER)
            tree.heading("Student1 IdNo",text="Student1 IdNo",anchor=CENTER)
            tree.heading("Student2 IdNo",text="Student2 IdNo",anchor=CENTER)

        
            s=ttk.Style(root)
            s.theme_use("vista")
            s.configure(".",font=("Helvetica",11))
            s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,"bold"))
            tree.place(x=10,y=200) 

            btn=Button(allocation,text="Submit & show",command=fun)
            btn.place(x=290,y=150)
            def fun2():
                s1=stucombo1.get()
                s2=streamCombobox.get()
                s3=stucombo2.get()
                s4=gen.get()
                db(s3,s1,s2,s4)
            btn=Button(allocation,text="Show",command=fun2)
            btn.place(x=420,y=370)
                
        def mark_page():
            mark=Frame(main_frame,width=500,height=500)
            mark.pack()
            lb=Label(mark,text='Mark Details',font=('bold',15))
            lb.place(x=155,y=10)
            batch=Label(mark,text='Batch :')
            batch.place(x=10,y=50)
            stucombo1=ttk.Combobox(mark)
            stucombo1.place(x=55,y=50)
            stucombo1.config(values=('2019','2020','2021','2021','2022','2023'))
            stucombo1.set('---select option ---')


            stream=Label(mark,text="Stream :")
            stream.place(x=10,y=80)
            streamCombobox=ttk.Combobox(mark)
            streamCombobox.place(x=65,y=80)
            streamCombobox.config(values=('Aided','SF'))
            streamCombobox.set('--- Select option ---')

            de=Label(mark,text='Course :')
            de.place(x=250,y=50)
            stucombo2=ttk.Combobox(mark)
            stucombo2.place(x=315,y=50)
            stucombo2.config(values=('CS','IT','CA','DS','BBA','CGS','MATHS','PHY','CH','EN','TAMIL','PSY','B.com-BPS','B.com-CA','B.com-PA','B.com','B.com-HONOURS','BIOTECH','MICRO-BIOLOGY','ZOLOGY'))
            stucombo2.set('---Select option ---')

            def fun():
                s1=stucombo1.get()
                s2=streamCombobox.get()
                s3=stucombo2.get()
                if(s1=='---Select option ---' or s2=='---Select option ---' or s3=='---Select option ---' or s1=="" or s2=="" or s3==""):
                    messagebox.showerror("Require","please fill the Entry")
                else:
                   db(s1,s2,s3)
            
            def db(s1,s2,s3):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()

                st="select * from ReviewMark where batch='%s' and  stream='%s' AND dept='%s' "
                a=(s1,s2,s3)
                try:
                    cursor.execute(st%a)
                except:
                    messagebox.showerror('Search Error',"Failed")
                tree.delete(*tree.get_children())
                for i in cursor:
                    tree.insert('',END,text='',values=(i[0],i[4],i[5],i[6],i[7]))
          
            tree =ttk.Treeview(mark,show='headings',height=15)
            tree["columns"]=("Idno","Review1","Review2","Review3","Total")
            tree.column("Idno",width=95,anchor=CENTER)
            tree.column("Review1",width=75,anchor=CENTER)
            tree.column("Review2",width=75,anchor=CENTER)
            tree.column("Review3",width=75,anchor=CENTER)
            tree.column("Total",width=75,anchor=CENTER)
        
            tree.heading("Idno",text="Idno",anchor=CENTER)
            tree.heading("Review1",text="Review1",anchor=CENTER)
            tree.heading("Review2",text="Review2",anchor=CENTER)
            tree.heading("Review3",text="Review3",anchor=CENTER)
            tree.heading("Total",text="Total",anchor=CENTER)
            s=ttk.Style(root)
            s.theme_use("vista")
            s.configure(".",font=("Helvetica",11))
            s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,"bold"))
            tree.place(x=30,y=150) 
            btn=Button(mark,text="Submit",command=fun)
            btn.place(x=280,y=80)

        
        def Review_page():
            review=Frame(main_frame,width=500,height=500)
            review.pack()
            lb=Label(review,text='Review Schedule',font=('bold',15))
            lb.place(x=155,y=20)
        
            batch=Label(review,text='Batch :')
            batch.place(x=10,y=60)
            stucombo1=ttk.Combobox(review)
            stucombo1.place(x=55,y=60)
            stucombo1.config(values=('2019','2020','2021','2021','2022','2023'))
            stucombo1.set('---select option ---')

    
            stream=Label(review,text="Stream :")
            stream.place(x=10,y=90)
            streamCombobox=ttk.Combobox(review)
            streamCombobox.place(x=65,y=90)
            streamCombobox.config(values=('Aided','SF'))
            streamCombobox.set('--- Select option ---')

            de=Label(review,text='Course :')
            de.place(x=250,y=70)
            stucombo2=ttk.Combobox(review)
            stucombo2.place(x=315,y=70)
            stucombo2.config(values=('CS','IT','CA','DS','BBA','CGS','MATHS','PHY','CH','EN','TAMIL','PSY','B.com-BPS','B.com-CA','B.com-PA','B.com','B.com-HONOURS','BIOTECH','MICRO-BIOLOGY','ZOLOGY'))
            stucombo2.set('---Select option ---')
        
            label2_page1=Label(review,text="Abstract & Title Submission :")
            label2_page1.place(x=10,y=120)
            title=DateEntry(review,date_pattern='yyyy-mm-dd')
            title.place(x=175,y=120)

            label2_page1=Label(review,text="Proposal Submission :")
            label2_page1.place(x=10,y=150)
            proposal=DateEntry(review,date_pattern='yyyy-mm-dd')
            proposal.place(x=175,y=150)

            label2_page1=Label(review,text="Review 1 Submission :")
            label2_page1.place(x=10,y=180)
            reviewOne=DateEntry(review,date_pattern='yyyy-mm-dd')
            reviewOne.place(x=175,y=180)

            label2_page1=Label(review,text="Review 2 Submission :")
            label2_page1.place(x=10,y=210)
            reviewTwo=DateEntry(review,date_pattern='yyyy-mm-dd')
            reviewTwo.place(x=175,y=210)


            label2_page1=Label(review,text="Review 3 Submission :")
            label2_page1.place(x=10,y=240)
            reviewThree=DateEntry(review,date_pattern='yyyy-mm-dd')
            reviewThree.place(x=175,y=240)


            label2_page1=Label(review,text="Report Submission :")
            label2_page1.place(x=10,y=270)
            report=DateEntry(review,date_pattern='yyyy-mm-dd')
            report.place(x=175,y=270)

            label2_page1=Label(review,text="Final Submission :")
            label2_page1.place(x=10,y=300)
            final=DateEntry(review,date_pattern='yyyy-mm-dd')
            final.place(x=175,y=300)


        

        
        
            def fun():
                s1=stucombo1.get()
                s2=stucombo2.get()
                s3=streamCombobox.get()
                s4=title.get()
                s5=proposal.get()
                s6=reviewOne.get()
                s7=reviewTwo.get()
                s8=reviewThree.get()
                s9=report.get()
                s10=final.get()
                con=pymysql.connect(host="localhost",user="root",password="",database='tcarts')
                cursor=con.cursor()
            

                if(s1=="--- Select option ---" or s2=="--- Select option ---" or s3=="--- Select option ---" or s1=="" or s2=="" or s3=="" ):
                    messagebox.showerror("Failed","Please fill the Entry")
                else:
                    cursor.execute("insert into ReviewSchdule values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10))
                    con.commit()
                    messagebox.showinfo("Successfully","Successfully updated")
                


            def reset():
                stucombo2.set('--- Select option ---')
                streamCombobox.set('--- Select option ---')
                stucombo1.set('---select option ---')
                title.set_date(date.today())
                proposal.set_date(date.today())
                reviewOne.set_date(date.today())
                reviewTwo.set_date(date.today())
                reviewThree.set_date(date.today())
                report.set_date(date.today())
                final.set_date(date.today())
            
            btn=Button(review,text="Reset",command=reset)
            btn.place(x=150,y=350)
            btn=Button(review,text="Submit",command=fun)
            btn.place(x=280,y=350)

        def student_Report_page():
            def Report():
                Report=Frame(main_frame,width=500,height=400)
                Report.pack()
                label_final=Label(Report,text="REPORT")
                label_final.place(x=200,y=50)
                label2_final=Label(Report,text="Student Id :")
                label2_final.place(x=10,y=100)
                usrName=Entry(Report)
                usrName.place(x=100,y=100)
                def dbtitle():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    if(userID!=''):
                        
                        try:
                            cursor.execute("select * from student where studid1='%s'"%userID)
                            r=cursor.fetchall()
                            if r:
                                st="select * from title where userID='%s'";
                                cursor.execute(st%(userID))
                                r1=cursor.fetchall()
                                for i in r1:
                                    x=str(i[2])
                                name.set(x)
                                conn.commit()
                            else :
                                cursor.execute("select * from student where studid2='%s'"%userID)
                                r=cursor.fetchall()
                                if r:
                                    st="select * from title where userID2='%s'";
                                    cursor.execute(st%(userID))
                                    r1=cursor.fetchall()

                                    for i in r1:
                                        x=str(i[2])
                                    name.set(x)
                                    conn.commit()
                                else:
                                    messagebox.showerror("Failed",'Check the Student Id')
                        except:
                            messagebox.showerror("Failed",'Check the Student Id')
                    else:
                        messagebox.showerror("Required","Please Fill the Entry")
                     
                btn_found=Button(Report,text="click",command=dbtitle)
                btn_found.place(x=250,y=100)
                name=StringVar()
                name.set("")
                label2_final=Label(Report,text="Title :")
                label2_final.place(x=10,y=140)
                title=Entry(Report,width=100,textvariable=name)
                title.place(x=60,y=140)
                label3_final=Label(Report,text="Doumentation Download :")
                label3_final.place(x=10,y=180)
                def db():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()

                    def display_file(file_id):
                        # Retrieve the selected file from the database
                        cursor.execute('SELECT name, data FROM studentreport WHERE userID=%s', (file_id,))
                        row = cursor.fetchone()
                        if row is not None:
                            filename, data = row
                            with open("report.pdf", "wb") as file:
                                file.write(data)
                            import os
                            os.startfile("report.pdf")
                        else:
                            cursor.execute('SELECT name, data FROM studentreport WHERE userID2=%s', (file_id,))
                            row = cursor.fetchone()
                            if row is not None:
                                filename, data = row
                                with open("report.pdf", "wb") as file:
                                    file.write(data)
                                import os
                                os.startfile("report.pdf")
                            else:
                                messagebox.showerror("Error", f"userID {file_id} not found.")
                    def search_file():
                        file_id = usrName.get()
                        if(file_id !=''):
                            if file_id:
                                display_file(str(file_id))
                        else:
                            messagebox.showerror("Required","Please Fill the Entry")
                    search_file()
                btn_download=Button(Report,text='Download here !',command=db)
                btn_download.place(x=180,y=180)
            Report()
          



        #hide-indication of other button 
        def hide_indicate():
       
            home_indicate.config(bg="grey")
            Guide_Details_indicate.config(bg='grey')
            Student_Details_indicate.config(bg='grey')
            Allocation_indicate.config(bg='grey')
            Allocation2_indicate.config(bg='grey')
            ReviewShu_indicate.config(bg='grey')
            mark_indicate.config(bg='grey')
            report_indicate.config(bg='grey')

        #solve the problem of overlapping the text
        def delete_page():
            #winfo children is method that access the method current Object
            for frame in main_frame.winfo_children():
                frame.destroy()
        #show-indicstion of current button
        def indicate(self,page):
            hide_indicate()
            self.config(bg='blue')
            delete_page()
            page()

    
    
        option_frame=Frame(root,bg="grey")

        #button
        home_btn=Button(option_frame,text='HOME',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(home_indicate,home_page))
        home_btn.place(x=10,y=50)
    

        home_indicate=Label(option_frame,text='',bg='grey')
        home_indicate.place(x=3,y=50,width=5,height=40)

        Guide_Details=Button(option_frame,text='Guide',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(Guide_Details_indicate,Guide_Details_page))
        Guide_Details.place(x=10,y=100)

        Guide_Details_indicate=Label(option_frame,text='',bg='grey')
        Guide_Details_indicate.place(x=3,y=100,width=5,height=40)

        Student_Details=Button(option_frame,text='Student',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(Student_Details_indicate,Student_Details_page))
        Student_Details.place(x=10,y=150)

        Student_Details_indicate=Label(option_frame,text='',bg='grey')
        Student_Details_indicate.place(x=3,y=150,width=5,height=40)

        Allocation=Button(option_frame,text='Boys Allocate',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(Allocation_indicate,Allocation_page))
        Allocation.place(x=10,y=200)

        Allocation_indicate=Label(option_frame,text='',bg='grey')
        Allocation_indicate.place(x=3,y=200,width=5,height=40)

        Allocation2=Button(option_frame,text='Girls Allocate',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(Allocation2_indicate,Allocation_girls_page))
        Allocation2.place(x=10,y=250)

        Allocation2_indicate=Label(option_frame,text='',bg='grey')
        Allocation2_indicate.place(x=3,y=250,width=5,height=40)

        ReviewShu=Button(option_frame,text='Scheduling',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(ReviewShu_indicate,Review_page))
        ReviewShu.place(x=10,y=300)

        ReviewShu_indicate=Label(option_frame,text='',bg='grey')
        ReviewShu_indicate.place(x=3,y=300,width=5,height=40)

        mark=Button(option_frame,text='Mark',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(mark_indicate,mark_page))
        mark.place(x=10,y=350)

        mark_indicate=Label(option_frame,text='',bg='grey')
        mark_indicate.place(x=3,y=350,width=5,height=40)

        rep=Button(option_frame,text='Report',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(report_indicate,student_Report_page))
        rep.place(x=10,y=400)

        report_indicate=Label(option_frame,text='',bg='grey')
        report_indicate.place(x=3,y=400,width=5,height=40)
    
        option_frame.pack(side=LEFT)
        option_frame.pack_propagate(False)
        option_frame.configure(width=140,height=500)


        main_frame=Frame(root,highlightbackground='black',highlightthickness=2)


        main_frame.pack()
        main_frame.pack_propagate(False)
        main_frame.configure(width=600,height=520)
    mentor_Page()

def guide_login(x):
    def guide_login_page():
        no.set(x)
        def logout():
            main_frame.destroy()
            option_frame.destroy()
            registeration_login()
        
        def home_page():
            home_frame=Frame(main_frame,width=500,height=400)
            home_frame.pack()
            logout_btn=Button(home_frame,text="LOGOUT",bd=0,fg='red',command=logout)
            logout_btn.place(x=450,y=20)
            label_home=Label(home_frame,text='HOME')
            label_home.place(x=200,y=50)

            label_UserId=Label(home_frame,text='Staff Id :')
            label_UserId.place(x=10,y=100)
            usrName=Entry(home_frame,textvariable=no)
            usrName.place(x=100,y=100)

            name=""

            label2_page1=Label(home_frame,text="Schdule",font=("Helvetica",11))
            label2_page1.place(x=385,y=150)
            textTwo=Text(home_frame,width=21,height=11)
            textTwo.insert(END,name)
            textTwo.place(x=330,y=180)
            def fun():
                userId=usrName.get()
                textTwo.delete("1.0","end")
                if(userId==""):
                    messagebox.showerror("Failed","please fill the Entry")
                else:
                    dbfound(userId)
            
            
            def dbfound(userId):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                try:
                    cursor.execute("select * from guide where gid='%s'"%x)
                    r=cursor.fetchall()
                    ##print(r)
                    for i in r:
                        s1=str(i[0])
                        s2=str(i[1])
                        name=str(i[2])
                    #print(name)
                    db(s1,s2,name)
                    


                    cursor.execute("select * from reviewschdule where dept='%s' AND stream='%s'"%(s1,s2))
                    e=cursor.fetchall()
                    for i in e:
                        abstract=str(i[3])
                        proposal=str(i[4])
                        reviewOne=str(i[5])
                        reviewTwo=str(i[6])
                        reviewThree=str(i[7])
                        report=str(i[8])
                        final=str(i[9])
                    value="Abstract :"+abstract+"\nProposal :"+proposal+"\nReview1  :"+reviewOne+"\nReview2  :"+reviewTwo+"\nReview3  :"+reviewThree+"\nReport   :"+report+"\nFinal    :"+final
                    ##print(value)
                    textTwo.insert(END,value)
                except:
                    messagebox.showerror("failed","failed to fetch the data")                
                
           
        


            btn_found=Button(home_frame,text="click",command=fun)
            btn_found.place(x=250,y=100)

            label_UserId=Label(home_frame,text='Student Details',font=("Helvetica",11))
            label_UserId.place(x=55,y=150)
            tree =ttk.Treeview(home_frame,show='headings',height=8)
            tree["columns"]=("Idno","Idno2")
            tree.column("Idno",width=100,anchor=CENTER)
            tree.column("Idno2",width=100,anchor=CENTER)
            tree.heading("Idno",text="Idno",anchor=CENTER)
            tree.heading("Idno2",text="Idno2",anchor=CENTER)
            def db(s1,s2,userId):
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                st="select * from allocation where dept='%s' AND stream='%s' and guide='%s'"
                a=(s1,s2,userId)
                cursor.execute(st%a)
                tree.delete(*tree.get_children())
                for i in cursor:
                    tree.insert('',END,text='',values=(i[4],i[5]))
                    
            s=ttk.Style(root)
            s.theme_use("vista")
            s.configure(".",font=("Helvetica",11))
            s.configure("Treeview.Heading",foreground='red',font=("Helvetica",11,"bold"))
            tree.place(x=5,y=180)


        
        
 
    
        
        
        def Abstract_page():
            def Abstract():
                abstract=Frame(main_frame,width=500,height=400)
                abstract.pack()
                label_abstract=Label(abstract,text="PROJECT TITLE AND ABSTRACT ")
                label_abstract.place(x=155,y=50)
                label2_abstract=Label(abstract,text="Student Id :")
                label2_abstract.place(x=10,y=100)
                usrName=Entry(abstract)
                usrName.place(x=100,y=100)
                label3_abstract=Label(abstract,text="Title :")
                label3_abstract.place(x=10,y=140)
                name=StringVar()
                name.set("")
                title=Entry(abstract,width=100,textvariable=name)
                title.place(x=60,y=140)
                def funtitle():
                    userID=usrName.get()
                    if(userID!=''):
                        fun()
                    else:
                        messagebox.showerror("Error","Please Fill The Entry")
                def fun():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    cursor.execute("select * from guide where gid='%s'"%x)
                    r1=cursor.fetchall()
                    for i in r1:
                        name=str(i[2])
                    try:
                        cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,userID))
                        r2=cursor.fetchall()
                        for i in r2:
                            stud=str(i[4])
                            stud2=str(i[5])
                        cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                        r=cursor.fetchall()
                        #print(r)
                        dbtitle(stud)
                    except:
                        try:
                            cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,userID))
                            r2=cursor.fetchall()
                            #print(r2)
                            for i in r2:
                                stud=str(i[4])
                                stud2=str(i[5])
                            #print(stud,"",stud2)
                            cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                            r=cursor.fetchall()
                            #print(r)
                            dbtitle(stud)
                        except:
                            messagebox.showerror("Mismatched","Enter The Student Id of Yours")
                        
                def dbtitle(userID):
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    try:
                        
                        st="select * from title where userID='%s'";
                        cursor.execute(st%(userID))
                        r1=cursor.fetchall()
                        #print(r1)
                        for i in r1:
                            y=str(i[2])
                        name.set(y)
                        conn.commit()
                    except:
                        messagebox.showerror("Failed",'He/She does not post any thing')
                btn_found=Button(abstract,text="click",command=funtitle)
                btn_found.place(x=250,y=100)

                label4_abstract=Label(abstract,text="Abstract Download :")
                label4_abstract.place(x=10,y=180)
                def db():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    

                    def display_file(file_id):
                    # Retrieve the selected file from the database
                        cursor.execute('SELECT name, data FROM abstract WHERE userID=%s', (file_id,))
                        row = cursor.fetchone()
                        if row is not None:
                            filename, data = row
                            with open("abstract.pdf", "wb") as file:
                                file.write(data)
                            import os
                            os.startfile("abstract.pdf")
                        else:
                            messagebox.showerror("Error", f"userID {file_id} not found.")

                    def search_file():
                        file_id = usrName.get()
                        if(file_id!=''):
                            try:
                                cursor.execute("select * from guide where gid='%s'"%x)
                                g=cursor.fetchall()
                                for i in g:
                                    name=str(i[2])
                                cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,file_id))
                                a=cursor.fetchall()
                                for i in a:
                                    stud=str(i[4])
                                    stud2=str(i[5])
                                cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                                    
                                if stud:
                                    display_file(str(stud))
                            except:
                                try:
                                    cursor.execute("select * from guide where gid='%s'"%x)
                                    g=cursor.fetchall()
                                    for i in g:
                                        name=str(i[2])
                                    cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,file_id))
                                    a=cursor.fetchall()
                                    for i in a:
                                        stud=str(i[4])
                                        stud2=str(i[5])
                                    cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))   
                                    if stud:
                                        display_file(str(stud))
                                except:
                                    messagebox.showerror("Error","Enter The Student ID of Yours")
                        else:
                           messagebox.showerror("Required","Please fill the  Entry") 
                    search_file()
                btn_download=Button(abstract,text='Download here !',command=db)
                btn_download.place(x=180,y=180)
                label4_abstract=Label(abstract,text="Message :")
                label4_abstract.place(x=10,y=220)
                message=Entry(abstract,width=50)
                message.place(x=70,y=220)
                def check():
                    userID=usrName.get()
                    s=message.get()
                    if(userID!=''):
                        if(s!=''):
                            functo()
                        else:
                            messagebox.showerror("Required","Please notify the student")
                    else:
                        messagebox.showerror("Required","Please Enter The Student ID")

                def functo():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    cursor.execute("select * from guide where gid='%s'"%x)
                    r1=cursor.fetchall()
                    for i in r1:
                        name=str(i[2])
                    try:
                        cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,userID))
                        r2=cursor.fetchall()
                        for i in r2:
                            stud=str(i[4])
                            stud2=str(i[5])
                        cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                        r=cursor.fetchall()
                        #print(r)
                        db1(stud)
                    except:
                        try:
                            cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,userID))
                            r2=cursor.fetchall()
                            #print(r2)
                            for i in r2:
                                stud=str(i[4])
                                stud2=str(i[5])
                            #print(stud,"",stud2)
                            cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                            r=cursor.fetchall()
                            #print(r)
                            db1(stud)
                        except:
                            messagebox.showerror("Mismatched","Enter The Student Id of Yours")

                def db1(userID):
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()

                    s=message.get()
                    userID2=""
                    try:
                        cursor.execute("select * from student where studid1='%s'"%userID)
                        r=cursor.fetchall()
                        for i in r:
                            x=str(i[5])
                        
                        ##print(x)
                        if x=='s': 
                            cursor.execute("UPDATE `abstractmessage` SET `message`='%s' WHERE `userID`='%s' and`userID2`='%s'"%(s,userID,userID2));
                            conn.commit()
                            messagebox.showinfo("Successfull","Message Send")
                        elif x=='p':
                            cursor.execute("select * from student where studid1='%s'"%userID)
                            r=cursor.fetchall()
                            ##print("pair")
                            for i in r:
                                y=str(i[3])
                                z=str(i[11])
                            cursor.execute("UPDATE `abstractmessage` SET `message`='%s' WHERE `userID`='%s' and `userID2`='%s'"%(s,y,z));
                            conn.commit()
                            messagebox.showinfo("Successfull","Message Send")                            

                    except:
                        try:
                            cursor.execute("select * from student where studid2='%s'"%userID)
                            r=cursor.fetchall()
                            ##print("pair")
                            for i in r:
                                y=str(i[3])
                                z=str(i[11])
                            cursor.execute("UPDATE `abstractmessage` SET `message`='%s' WHERE `userID`='%s' and `userID2`='%s'"%(s,y,z));
                            conn.commit()
                            messagebox.showinfo("Successfull","Message Send")                            
                        except:
                            messagebox.showerror("Failed","student ID not Found")

                def accept():
                    check()
                btn_acceptance=Button(abstract,text="Accept",command=accept)
                btn_acceptance.place(x=10,y=260)
                def reject():
                
                    def db2():
                        conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                        cursor = conn.cursor()
                        userID=usrName.get()
                        s=message.get()
                        userID2=""
                        try:
                            cursor.execute("select * from student where studid1='%s'"%userID)
                            r=cursor.fetchall()
                            for i in r:
                                x=str(i[5])
                            if x=='s':
                                cursor.execute("DELETE from abstract where userID='%s'"%userID);

                                cursor.execute("DELETE from title where userID='%s'"%userID);
                                conn.commit()
                            elif x=='p':
                                cursor.execute("select * from student where studid1='%s'"%userID)
                                r=cursor.fetchall()
                                for i in r:
                                    y=str(i[3])
                                    z=str(i[11])
                                cursor.execute("DELETE from abstract where userID='%s'"%userID);

                                cursor.execute("DELETE from title WHERE userID='%s'"%userID);
                                conn.commit()
                        except:
                            try:
                                cursor.execute("select * from student where studid2='%s'"%userID)
                                r=cursor.fetchall()
                                for i in r:
                                    y=str(i[3])
                                    z=str(i[11])
                                cursor.execute("DELETE from abstract where userID='%s'"%userID);

                                cursor.execute("DELETE from title WHERE userID2='%s'"%userID);
                                conn.commit()
                            except:
                                messagebox.showerror("Failed","student ID not Found")
                    try:
                        check()
                        db2()
                    except:
                        pass
                btn_Reject=Button(abstract,text="Reject",command=reject)
                btn_Reject.place(x=90,y=260)
 
            Abstract()
        
        def proposal_page():
            def proposal():
                proposal=Frame(main_frame,width=500,height=400)
                proposal.pack()
                label_proposal=Label(proposal,text="PROJECT PROPOSAL")
                label_proposal.place(x=200,y=50)
                label2_proposal=Label(proposal,text="Student Id :")
                label2_proposal.place(x=10,y=100)
                usrName=Entry(proposal)
                usrName.place(x=100,y=100)
                def dbfuntitle():
                    userID=usrName.get()
                    if(userID!=""):
                        funtitle()
                    else:
                        messagebox.showerror("Required","Please fill the Student ID")
                def funtitle():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    cursor.execute("select * from guide where gid='%s'"%x)
                    r1=cursor.fetchall()
                    for i in r1:
                        name=str(i[2])
                    try:
                        cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,userID))
                        r2=cursor.fetchall()
                        for i in r2:
                            stud=str(i[4])
                            stud2=str(i[5])
                        cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                        r=cursor.fetchall()
                        #print(r)
                        dbtitle(stud)
                    except:
                        try:
                            cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,userID))
                            r2=cursor.fetchall()
                            #print(r2)
                            for i in r2:
                                stud=str(i[4])
                                stud2=str(i[5])
                            #print(stud,"",stud2)
                            cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                            r=cursor.fetchall()
                            #print(r)
                            dbtitle(stud)
                        except:
                            messagebox.showerror("Mismatched","Enter The Student Id of Yours")
                        
                def dbtitle(userID):
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    try:
                        
                        st="select * from title where userID='%s'";
                        cursor.execute(st%(userID))
                        r1=cursor.fetchall()
                        #print(r1)
                        for i in r1:
                            y=str(i[2])
                        name.set(y)
                        conn.commit()
                    except:
                        messagebox.showerror("Failed",'He/She does not post any thing')
                
                btn_found=Button(proposal,text="click",command=dbfuntitle)
                btn_found.place(x=250,y=100)
                name=StringVar()
                name.set("")
                label2_proposal=Label(proposal,text="Title :")
                label2_proposal.place(x=10,y=140)
                title=Entry(proposal,width=100,textvariable=name)
                title.place(x=60,y=140)
                label3_proposal=Label(proposal,text="Proposal Download :")
                label3_proposal.place(x=10,y=180)
                def db():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    

                    def display_file(file_id):
                    # Retrieve the selected file from the database
                        cursor.execute('SELECT name, data FROM proposal WHERE userID=%s', (file_id,))
                        row = cursor.fetchone()
                        if row is not None:
                            filename, data = row
                            with open("proposal.pdf", "wb") as file:
                                file.write(data)
                            import os
                            os.startfile("proposal.pdf")
                        else:
                            messagebox.showerror("Error", f"userID {file_id} not found.")

                    def search_file():
                        file_id = usrName.get()
                        if(file_id!=''):
                            try:
                                cursor.execute("select * from guide where gid='%s'"%x)
                                g=cursor.fetchall()
                                for i in g:
                                    name=str(i[2])
                                cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,file_id))
                                a=cursor.fetchall()
                                for i in a:
                                    stud=str(i[4])
                                    stud2=str(i[5])
                                cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                                    
                                if stud:
                                    display_file(str(stud))
                            except:
                                try:
                                    cursor.execute("select * from guide where gid='%s'"%x)
                                    g=cursor.fetchall()
                                    for i in g:
                                        name=str(i[2])
                                    cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,file_id))
                                    a=cursor.fetchall()
                                    for i in a:
                                        stud=str(i[4])
                                        stud2=str(i[5])
                                    cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))   
                                    if stud:
                                        display_file(str(stud))
                                except:
                                    messagebox.showerror("Error","Enter The Student ID of Yours")
                        else:
                            messagebox.showerror("Required","Please fill the Entry")
                    search_file()
                btn_download=Button(proposal,text='Download here !',command=db)
                btn_download.place(x=180,y=180)
                label3_proposal=Label(proposal,text="Message :")
                label3_proposal.place(x=10,y=220)
                message=Entry(proposal,width=50)
                message.place(x=70,y=220)

                def check():
                    userID=usrName.get()
                    s=message.get()

                    if(userID!=''):
                        if(s==''):
                            messagebox.showerror("Required","Please Notify the Students")
                        else:
                            functo()
 
                    else:
                        messagebox.showerror("Required","Please Enter The Student ID")

                def functo():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    cursor.execute("select * from guide where gid='%s'"%x)
                    r1=cursor.fetchall()
                    for i in r1:
                        name=str(i[2])
                    try:
                        cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,userID))
                        r2=cursor.fetchall()
                        for i in r2:
                            stud=str(i[4])
                            stud2=str(i[5])
                        cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                        r=cursor.fetchall()
                        #print(r)
                        db1(stud)
                    except:
                        try:
                            cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,userID))
                            r2=cursor.fetchall()
                            #print(r2)
                            for i in r2:
                                stud=str(i[4])
                                stud2=str(i[5])
                            #print(stud,"",stud2)
                            cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                            r=cursor.fetchall()
                            #print(r)
                            db1(stud)
                        except:
                            messagebox.showerror("Mismatched","Enter The Student Id of Yours")
                def db1(userID):
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    s=message.get()
                    userID2=""
                    try:
                        cursor.execute("select * from student where studid1='%s'"%userID)
                        r=cursor.fetchall()
                        for i in r:
                            x=str(i[5])     
                        if x=='s': 
                            cursor.execute("UPDATE `abstractmessage` SET `message`='%s' WHERE `userID`='%s' and`userID2`='%s'"%(s,userID,userID2));
                            conn.commit()
                            messagebox.showinfo("Successfull","Message Send")
                        elif x=='p':
                            cursor.execute("select * from student where studid1='%s'"%userID)
                            r=cursor.fetchall()
                            for i in r:
                                y=str(i[3])
                                z=str(i[11])
                            cursor.execute("UPDATE `abstractmessage` SET `message`='%s' WHERE `userID`='%s' and `userID2`='%s'"%(s,y,z));
                            conn.commit()
                            messagebox.showinfo("Successfull","Message Send")                            

                    except:
                        try:
                            cursor.execute("select * from student where studid2='%s'"%userID)
                            r=cursor.fetchall()
                            for i in r:
                                y=str(i[3])
                                z=str(i[11])
                            cursor.execute("UPDATE `abstractmessage` SET `message`='%s' WHERE `userID`='%s' and `userID2`='%s'"%(s,y,z));
                            conn.commit()
                            messagebox.showinfo("Successfull","Message Send")                            
                        except:
                            messagebox.showerror("Failed","student ID not Found")

                def accept():
                    check()

                btn_acceptance=Button(proposal,text="Accept",command=accept)
                btn_acceptance.place(x=10,y=260)
                def reject():
                    s=message.get()

                        
                    def db2():
                        conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                        cursor = conn.cursor()
                        userID=usrName.get()
                        s=message.get()
                        userID2=""
                        try:
                            cursor.execute("select * from student where studid1='%s'"%userID)
                            r=cursor.fetchall()
                            for i in r:
                                x=str(i[5])
                            if x=='s': 
                                cursor.execute("DELETE from proposal where userID='%s'"%userID);
                                conn.commit()
                            elif x=='p':
                                cursor.execute("select * from student where studid1='%s'"%userID)
                                r=cursor.fetchall()
                                for i in r:
                                    y=str(i[3])
                                    z=str(i[11])
                                cursor.execute("DELETE from proposal WHERE userID='%s'"%userID);
                                conn.commit()
                        except:
                            try:
                               cursor.execute("select * from student where studid2='%s'"%userID)
                               r=cursor.fetchall()
                               for i in r:
                                   y=str(i[3])
                                   z=str(i[11])
                               cursor.execute("DELETE from proposal WHERE userID2='%s'"%userID);
                               conn.commit()
                            except:
                                messagebox.showerror("Failed","student ID not Found")
                    try:
                        check()
                        if(s!=''):
                            db2()
                    except:
                        pass
                btn_Reject=Button(proposal,text="Reject",command=reject)
                btn_Reject.place(x=90,y=260)

            proposal()
        def student_review_page():
            def page1go(): 
                page1=Frame(main_frame,width=500,height=400)
                page1.pack()
                label_page1=Label(page1,text="REVIEW 1")
                label_page1.place(x=200,y=50)
                label2_page1=Label(page1,text="Student Id :")
                label2_page1.place(x=10,y=100)
                usrName=Entry(page1)
                usrName.place(x=100,y=100)
                def dbfuntitle():
                    userID=usrName.get()
                    if(userID!=""):
                        fun()
                    else:
                        messagebox.showerror("Required","Please fill the Student ID")
                
                def fun():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    cursor.execute("select * from guide where gid='%s'"%x)
                    r1=cursor.fetchall()
                    for i in r1:
                        name=str(i[2])
                    try:
                        cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,userID))
                        r2=cursor.fetchall()
                        for i in r2:
                            stud=str(i[4])
                            stud2=str(i[5])
                        cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                        r=cursor.fetchall()
                        #print(r)
                        dbtitle(stud)
                    except:
                        try:
                            cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,userID))
                            r2=cursor.fetchall()
                            #print(r2)
                            for i in r2:
                                stud=str(i[4])
                                stud2=str(i[5])
                            #print(stud,"",stud2)
                            cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                            r=cursor.fetchall()
                            #print(r)
                            dbtitle(stud)
                        except:
                            messagebox.showerror("Mismatched","Enter The Student Id of Yours")
                        
                def dbtitle(userID):
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    try:
                        
                        st="select * from title where userID='%s'";
                        cursor.execute(st%(userID))
                        r1=cursor.fetchall()
                        #print(r1)
                        for i in r1:
                            y=str(i[2])
                        name.set(y)
                        conn.commit()
                    except:
                        messagebox.showerror("Failed",'He/She does not post any thing')
                 
                
                btn_found=Button(page1,text="click",command=dbfuntitle)
                btn_found.place(x=250,y=100)
                name=StringVar()
                name.set("")
                label2_page1=Label(page1,text="Title :")
                label2_page1.place(x=10,y=140)
                title=Entry(page1,width=100,textvariable=name)
                title.place(x=60,y=140)
                label3_page1=Label(page1,text="First Review Download :")
                label3_page1.place(x=10,y=180)

                def db():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    

                    def display_file(file_id):
                    # Retrieve the selected file from the database
                        cursor.execute('SELECT name, data FROM reviewOne WHERE userID=%s', (file_id,))
                        row = cursor.fetchone()
                        if row is not None:
                            filename, data = row
                            with open("reviewone.ppt", "wb") as file:
                                file.write(data)
                            import os
                            os.startfile("reviewone.ppt")
                        else:
                            messagebox.showerror("Error", f"userID {file_id} not found.")

                    def search_file():
                        file_id = usrName.get()
                        if(file_id !=''):
                            
                            try:
                                cursor.execute("select * from guide where gid='%s'"%x)
                                g=cursor.fetchall()
                                for i in g:
                                    name=str(i[2])
                                cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,file_id))
                                a=cursor.fetchall()
                                for i in a:
                                    stud=str(i[4])
                                    stud2=str(i[5])
                                cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                                    
                                if stud:
                                    display_file(str(stud))
                            except:
                                try:
                                    cursor.execute("select * from guide where gid='%s'"%x)
                                    g=cursor.fetchall()
                                    for i in g:
                                        name=str(i[2])
                                    cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,file_id))
                                    a=cursor.fetchall()
                                    for i in a:
                                        stud=str(i[4])
                                        stud2=str(i[5])
                                    cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))   
                                    if stud:
                                        display_file(str(stud))
                                except:
                                    messagebox.showerror("Error","Enter The Student ID of Yours")
                        else:
                            messagebox.showerror("Required","please fill the Entry")
                    search_file()
                btn_upload=Button(page1,text='Download here !',command=db)
                btn_upload.place(x=180,y=180)
                def des2():
                    page1.destroy()
                    page2go()
                def des3():
                    page1.destroy()
                    page3go()
                btn1=Button(page1,text="Review 2",command=des2)
                btn1.place(x=100,y=350)
                btn2=Button(page1,text="Review 3",command=des3)
                btn2.place(x=250,y=350)
                def page2go():
                    page2=Frame(main_frame,width=500,height=400)
                    page2.pack()
                    label_page2=Label(page2,text="REVIEW 2")
                    label_page2.place(x=200,y=50)
                    label2_page2=Label(page2,text="Student Id :")
                    label2_page2.place(x=10,y=100)
                    usrName=Entry(page2)
                    usrName.place(x=100,y=100)
                    def dbfuntitle():
                        userID=usrName.get()
                        if(userID!=""):
                            fun()
                        else:
                            messagebox.showerror("Required","Please fill the Student ID")
                    def fun():
                        conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                        cursor = conn.cursor()
                        userID=usrName.get()
                        cursor.execute("select * from guide where gid='%s'"%x)
                        r1=cursor.fetchall()
                        for i in r1:
                            name=str(i[2])
                        try:
                            cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,userID))
                            r2=cursor.fetchall()
                            for i in r2:
                                stud=str(i[4])
                                stud2=str(i[5])
                            cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                            r=cursor.fetchall()
                            #print(r)
                            dbtitle(stud)
                        except:
                            try:
                                cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,userID))
                                r2=cursor.fetchall()
                                #print(r2)
                                for i in r2:
                                    stud=str(i[4])
                                    stud2=str(i[5])
                                #print(stud,"",stud2)
                                cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                                r=cursor.fetchall()
                                #print(r)
                                dbtitle(stud)
                            except:
                                messagebox.showerror("Mismatched","Enter The Student Id of Yours")
                            
                    def dbtitle(userID):
                        conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                        cursor = conn.cursor()
                        try:
                            
                            st="select * from title where userID='%s'";
                            cursor.execute(st%(userID))
                            r1=cursor.fetchall()
                            #print(r1)
                            for i in r1:
                                y=str(i[2])
                            name.set(y)
                            conn.commit()
                        except:
                            messagebox.showerror("Failed",'He/She does not post any thing')
                    btn_found=Button(page2,text="click",command=dbfuntitle)
                    btn_found.place(x=250,y=100)
                    name=StringVar()
                    name.set("")
                    label2_page2=Label(page2,text="Title :")
                    label2_page2.place(x=10,y=140)
                    title=Entry(page2,width=100,textvariable=name)
                    title.place(x=60,y=140)

                    label3_page2=Label(page2,text="Second Review Download :")
                    label3_page2.place(x=10,y=180)
                    def db():
                        conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                        cursor = conn.cursor()
                        

                        def display_file(file_id):
                        # Retrieve the selected file from the database
                            cursor.execute('SELECT name, data FROM reviewTwo WHERE userID=%s', (file_id,))
                            row = cursor.fetchone()
                            if row is not None:
                                filename, data = row
                                with open("reviewtwo.ppt", "wb") as file:
                                    file.write(data)
                                import os
                                os.startfile("reviewtwo.ppt")
                            else:
                                messagebox.showerror("Error", f"userID {file_id} not found.")

                        def search_file():
                            file_id = usrName.get()
                            if(file_id !=''):
                                try:
                                    cursor.execute("select * from guide where gid='%s'"%x)
                                    g=cursor.fetchall()
                                    for i in g:
                                        name=str(i[2])
                                    cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,file_id))
                                    a=cursor.fetchall()
                                    for i in a:
                                        stud=str(i[4])
                                        stud2=str(i[5])
                                    cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                                        
                                    if stud:
                                        display_file(str(stud))
                                except:
                                    try:
                                        cursor.execute("select * from guide where gid='%s'"%x)
                                        g=cursor.fetchall()
                                        for i in g:
                                            name=str(i[2])
                                        cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,file_id))
                                        a=cursor.fetchall()
                                        for i in a:
                                            stud=str(i[4])
                                            stud2=str(i[5])
                                        cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))   
                                        if stud:
                                            display_file(str(stud))
                                    except:
                                        messagebox.showerror("Error","Enter The Student ID of Yours")
                            else:
                                messagebox.showerror("Required","Please Fill the Entry")
                        search_file()
                    btn_upload=Button(page2,text='Download here !',command=db)
                    btn_upload.place(x=180,y=180)
                    def des1():
                        page2.destroy()
                        page1go()
                    def des3():
                        page2.destroy()
                        page3go()
                    btn1=Button(page2,text="Review 1",command=des1)
                    btn2=Button(page2,text="Review 3",command=des3)
                    btn1.place(x=100,y=350)
                    btn2.place(x=250,y=350)
                def page3go():
                    page3=Frame(main_frame,width=500,height=400)
                    page3.pack()
                    label_page3=Label(page3,text="REVIEW 3")
                    label_page3.place(x=200,y=50)
                    label2_page3=Label(page3,text="Student Id :")
                    label2_page3.place(x=10,y=100)
                    usrName=Entry(page3)
                    usrName.place(x=100,y=100)
                    def dbfuntitle():
                        userID=usrName.get()
                        if(userID!=""):
                            fun()
                        else:
                            messagebox.showerror("Required","Please fill the Student ID")
                    def fun():
                        conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                        cursor = conn.cursor()
                        userID=usrName.get()
                        cursor.execute("select * from guide where gid='%s'"%x)
                        r1=cursor.fetchall()
                        for i in r1:
                            name=str(i[2])
                        try:
                            cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,userID))
                            r2=cursor.fetchall()
                            for i in r2:
                                stud=str(i[4])
                                stud2=str(i[5])
                            cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                            r=cursor.fetchall()
                            #print(r)
                            dbtitle(stud)
                        except:
                            try:
                                cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,userID))
                                r2=cursor.fetchall()
                                #print(r2)
                                for i in r2:
                                    stud=str(i[4])
                                    stud2=str(i[5])
                                #print(stud,"",stud2)
                                cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                                r=cursor.fetchall()
                                #print(r)
                                dbtitle(stud)
                            except:
                                messagebox.showerror("Mismatched","Enter The Student Id of Yours")
                            
                    def dbtitle(userID):
                        conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                        cursor = conn.cursor()
                        try:
                            
                            st="select * from title where userID='%s'";
                            cursor.execute(st%(userID))
                            r1=cursor.fetchall()
                            #print(r1)
                            for i in r1:
                                y=str(i[2])
                            name.set(y)
                            conn.commit()
                        except:
                            messagebox.showerror("Failed",'He/She does not post any thing')
                 
                    btn_found=Button(page3,text="click",command=dbfuntitle)
                    btn_found.place(x=250,y=100)
                    name=StringVar()
                    name.set("")
                    label2_page3=Label(page3,text="Title :")
                    label2_page3.place(x=10,y=140)
                    title=Entry(page3,width=100,textvariable=name)
                    title.place(x=60,y=140)

                    def db():
                        conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                        cursor = conn.cursor()
                        

                        def display_file(file_id):
                        # Retrieve the selected file from the database
                            cursor.execute('SELECT name, data FROM reviewThree WHERE userID=%s', (file_id,))
                            row = cursor.fetchone()
                            if row is not None:
                                filename, data = row
                                with open("reviewthree.ppt", "wb") as file:
                                    file.write(data)
                                import os
                                os.startfile("reviewthree.ppt")
                            else:
                                messagebox.showerror("Error", f"userID {file_id} not found.")

                        def search_file():
                            file_id = usrName.get()
                            if(file_id !=''):
                                try:
                                    cursor.execute("select * from guide where gid='%s'"%x)
                                    g=cursor.fetchall()
                                    for i in g:
                                        name=str(i[2])
                                    cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,file_id))
                                    a=cursor.fetchall()
                                    for i in a:
                                        stud=str(i[4])
                                        stud2=str(i[5])
                                    cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                                        
                                    if stud:
                                        display_file(str(stud))
                                except:
                                    try:
                                        cursor.execute("select * from guide where gid='%s'"%x)
                                        g=cursor.fetchall()
                                        for i in g:
                                            name=str(i[2])
                                        cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,file_id))
                                        a=cursor.fetchall()
                                        for i in a:
                                            stud=str(i[4])
                                            stud2=str(i[5])
                                        cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))   
                                        if stud:
                                            display_file(str(stud))
                                    except:
                                        messagebox.showerror("Error","Enter The Student ID of Yours")
                            else:
                                messagebox.showerror("Required","Please Fill The Entry")
                        search_file()
                    label3_page3=Label(page3,text="Third Review Download :")
                    label3_page3.place(x=10,y=180)
                    btn_upload=Button(page3,text='Download here !',command=db)
                    btn_upload.place(x=180,y=180)
                    def des1():
                        page3.destroy()
                        page1go()
                    def des2():
                        page3.destroy()
                        page2go()
                    btn1=Button(page3,text="Review 1",command=des1)
                    btn2=Button(page3,text="Review 2",command=des2)
                    btn1.place(x=100,y=350)
                    btn2.place(x=250,y=350)
    


            page1go()
        
        def student_final_page():
            def final():
                final=Frame(main_frame,width=500,height=400)
                final.pack()
                label_final=Label(final,text="FINAL DOCUMENTATION")
                label_final.place(x=200,y=50)
                label2_final=Label(final,text="Student Id :")
                label2_final.place(x=10,y=100)
                usrName=Entry(final)
                usrName.place(x=100,y=100)
                def dbfuntitle():
                    userID=usrName.get()
                    if(userID!=""):
                        fun()
                    else:
                        messagebox.showerror("Required","Please fill the Student ID")
                def fun():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    cursor.execute("select * from guide where gid='%s'"%x)
                    r1=cursor.fetchall()
                    for i in r1:
                        name=str(i[2])
                    try:
                        cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,userID))
                        r2=cursor.fetchall()
                        for i in r2:
                            stud=str(i[4])
                            stud2=str(i[5])
                        cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                        r=cursor.fetchall()
                        #print(r)
                        dbtitle(stud)
                    except:
                        try:
                            cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,userID))
                            r2=cursor.fetchall()
                            #print(r2)
                            for i in r2:
                                stud=str(i[4])
                                stud2=str(i[5])
                            #print(stud,"",stud2)
                            cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                            r=cursor.fetchall()
                            #print(r)
                            dbtitle(stud)
                        except:
                            messagebox.showerror("Mismatched","Enter The Student Id of Yours")
                        
                def dbtitle(userID):
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    try:
                        
                        st="select * from title where userID='%s'";
                        cursor.execute(st%(userID))
                        r1=cursor.fetchall()
                        #print(r1)
                        for i in r1:
                            y=str(i[2])
                        name.set(y)
                        conn.commit()
                    except:
                        messagebox.showerror("Failed",'He/She does not post any thing')
                 
                btn_found=Button(final,text="click",command=dbfuntitle)
                btn_found.place(x=250,y=100)
                name=StringVar()
                name.set("")
                label2_final=Label(final,text="Title :")
                label2_final.place(x=10,y=140)
                title=Entry(final,width=100,textvariable=name)
                title.place(x=60,y=140)
                label3_final=Label(final,text="Doumentation Download :")
                label3_final.place(x=10,y=180)
                def db():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    

                    def display_file(file_id):
                    # Retrieve the selected file from the database
                        cursor.execute('SELECT name, data FROM final WHERE userID=%s', (file_id,))
                        row = cursor.fetchone()
                        if row is not None:
                            filename, data = row
                            with open("final.pdf", "wb") as file:
                                file.write(data)
                            import os
                            os.startfile("final.pdf")
                        else:
                            messagebox.showerror("Error", f"userID {file_id} not found.")

                    def search_file():
                        file_id = usrName.get()
                        if(file_id !=''):
                            try:
                                cursor.execute("select * from guide where gid='%s'"%x)
                                g=cursor.fetchall()
                                for i in g:
                                    name=str(i[2])
                                cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,file_id))
                                a=cursor.fetchall()
                                for i in a:
                                    stud=str(i[4])
                                    stud2=str(i[5])
                                cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                                    
                                if stud:
                                    display_file(str(stud))
                            except:
                                try:
                                    cursor.execute("select * from guide where gid='%s'"%x)
                                    g=cursor.fetchall()
                                    for i in g:
                                        name=str(i[2])
                                    cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,file_id))
                                    a=cursor.fetchall()
                                    for i in a:
                                        stud=str(i[4])
                                        stud2=str(i[5])
                                    cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))   
                                    if stud:
                                        display_file(str(stud))
                                except:
                                    messagebox.showerror("Error","Enter The Student ID of Yours")
                        else:
                            messagebox.showerror("Required","Please Fill The Entry")
                    search_file()
                btn_download=Button(final,text='Download here !',command=db)
                btn_download.place(x=180,y=180)
            final()

        def student_Report_page():
            def Report():
                Report=Frame(main_frame,width=500,height=400)
                Report.pack()
                label_final=Label(Report,text="REPORT")
                label_final.place(x=200,y=50)
                label2_final=Label(Report,text="Student Id :")
                label2_final.place(x=10,y=100)
                usrName=Entry(Report)
                usrName.place(x=100,y=100)
                def dbfuntitle():
                    userID=usrName.get()
                    if(userID!=""):
                        fun()
                    else:
                        messagebox.showerror("Required","Please fill the Student ID")
                def fun():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    userID=usrName.get()
                    cursor.execute("select * from guide where gid='%s'"%x)
                    r1=cursor.fetchall()
                    for i in r1:
                        name=str(i[2])
                    try:
                        cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,userID))
                        r2=cursor.fetchall()
                        for i in r2:
                            stud=str(i[4])
                            stud2=str(i[5])
                        cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                        r=cursor.fetchall()
                        #print(r)
                        dbtitle(stud)
                    except:
                        try:
                            cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,userID))
                            r2=cursor.fetchall()
                            #print(r2)
                            for i in r2:
                                stud=str(i[4])
                                stud2=str(i[5])
                            #print(stud,"",stud2)
                            cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                            r=cursor.fetchall()
                            #print(r)
                            dbtitle(stud)
                        except:
                            messagebox.showerror("Mismatched","Enter The Student Id of Yours")
                        
                def dbtitle(userID):
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    try:
                        
                        st="select * from title where userID='%s'";
                        cursor.execute(st%(userID))
                        r1=cursor.fetchall()
                        #print(r1)
                        for i in r1:
                            y=str(i[2])
                        name.set(y)
                        conn.commit()
                    except:
                        messagebox.showerror("Failed",'He/She does not post any thing')
                 
                btn_found=Button(Report,text="click",command=dbfuntitle)
                btn_found.place(x=250,y=100)
                name=StringVar()
                name.set("")
                label2_final=Label(Report,text="Title :")
                label2_final.place(x=10,y=140)
                title=Entry(Report,width=100,textvariable=name)
                title.place(x=60,y=140)
                label3_final=Label(Report,text="Doumentation Download :")
                label3_final.place(x=10,y=180)    
                def db():
                    conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                    cursor = conn.cursor()
                    

                    def display_file(file_id):
                    # Retrieve the selected file from the database
                        cursor.execute('SELECT name, data FROM studentreport WHERE userID=%s', (file_id,))
                        row = cursor.fetchone()
                        if row is not None:
                            filename, data = row
                            with open("report.pdf", "wb") as file:
                                file.write(data)
                            import os
                            os.startfile("report.pdf")
                        else:
                            messagebox.showerror("Error", f"userID {file_id} not found.")

                    def search_file():
                        file_id = usrName.get()
                        if(file_id!=''):
                            try:
                                cursor.execute("select * from guide where gid='%s'"%x)
                                g=cursor.fetchall()
                                for i in g:
                                    name=str(i[2])
                                cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,file_id))
                                a=cursor.fetchall()
                                for i in a:
                                    stud=str(i[4])
                                    stud2=str(i[5])
                                cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                                    
                                if stud:
                                    display_file(str(stud))
                            except:
                                try:
                                    cursor.execute("select * from guide where gid='%s'"%x)
                                    g=cursor.fetchall()
                                    for i in g:
                                        name=str(i[2])
                                    cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,file_id))
                                    a=cursor.fetchall()
                                    for i in a:
                                        stud=str(i[4])
                                        stud2=str(i[5])
                                    cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))   
                                    if stud:
                                        display_file(str(stud))
                                except:
                                    messagebox.showerror("Error","Enter The Student ID of Yours")
                        else:
                            messagebox.showerror("Required","Please Fill The Entry")
                    search_file()
                btn_download=Button(Report,text='Download here !',command=db)
                btn_download.place(x=180,y=180)
            Report()
        def Review_mark_page():
            mark_frame=Frame(main_frame,width=500,height=500)
            mark_frame.pack()
            label_mark=Label(mark_frame,text='Mark Update')
            label_mark.place(x=200,y=50)
            label_mark=Label(mark_frame,text='Student Id')
            label_mark.place(x=10,y=100)
            usrName=Entry(mark_frame)
            usrName.place(x=120,y=100)
        
            dept=Label(mark_frame,text='Department :')
            dept.place(x=10,y=140)
            stucombo2=ttk.Combobox(mark_frame)
            stucombo2.place(x=120,y=140)
            stucombo2.config(values=('CS','IT','CA','DS','BBA','CGS','MATHS','PHY','CH','EN','TAMIL','PSY','B.com-BPS','B.com-CA','B.com-PA','B.com','B.com-HONOURS','BIOTECH','MICRO-BIOLOGY','ZOLOGY'))
            stucombo2.set('--- select option ---')

            studentstream=Label(mark_frame,text='Stream :')
            studentstream.place(x=10,y=170)
            stucombo3=ttk.Combobox(mark_frame)
            stucombo3.place(x=120,y=170)
            stucombo3.config(values=('Aided','SF'))
            stucombo3.set('--- select option ---')

            batch=Label(mark_frame,text='Batch :')
            batch.place(x=10,y=210)
            stucombo1=ttk.Combobox(mark_frame)
            stucombo1.place(x=120,y=210)
            stucombo1.config(values=('2019','2020','2021','2021','2022','2023'))
            stucombo1.set('--- select option ---')
        
            label_mark=Label(mark_frame,text='Review one Mark :')
            label_mark.place(x=10,y=240)
            ReviewOne=Spinbox(mark_frame,from_=0,to=5)
            ReviewOne.place(x=120,y=240)
            label_mark=Label(mark_frame,text='Review two mark :')
            label_mark.place(x=10,y=270)
            ReviewTwo=Spinbox(mark_frame,from_=0,to=5)
            ReviewTwo.place(x=120,y=270)
            label_mark=Label(mark_frame,text='Review three mark :')
            label_mark.place(x=10,y=310)
            ReviewThree=Spinbox(mark_frame,from_=0,to=5)
            ReviewThree.place(x=120,y=310)
            totalMark=StringVar()
            totalMark.set("")
            def fun():
                s=usrName.get()
                conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                cursor = conn.cursor()
                try:
                    cursor.execute("select * from guide where gid='%s'"%x)
                    g=cursor.fetchall()
                    for i in g:
                        name=str(i[2])
                    cursor.execute("select * from allocation where guide='%s' and student1='%s'"%(name,s))
                    a=cursor.fetchall()
                    #print(a)
                    for i in a:
                        stud=str(i[4])
                        stud2=str(i[5])
                    cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                    db(stud)
                                
                except:
                    try:
                        cursor.execute("select * from guide where gid='%s'"%x)
                        g=cursor.fetchall()
                        for i in g:
                            name=str(i[2])
                        cursor.execute("select * from allocation where guide='%s' and student2='%s'"%(name,s))
                        a=cursor.fetchall()
                        #print(a)
                        for i in a:
                            stud=str(i[4])
                            stud2=str(i[5])
                        cursor.execute("select * from student where studid1='%s' and studid2='%s'"%(stud,stud2))
                        db(stud2)
                    except:
                        messagebox.showerror("Failed","Enter the Student Id of Yours")

                
                
            def db(s):
                #print(s)
                s1=ReviewOne.get()
                s2=ReviewTwo.get()
                s3=ReviewThree.get()
                s4=stucombo2.get()
                s5=stucombo3.get()
                s6=stucombo1.get()
                
                conn = pymysql.connect(host='localhost', user='root', password='', db='tcarts')
                cursor = conn.cursor()
            
                
                def refresh():
                    usrName.delete(0,'end')
                    ReviewOne.delete(0,'end')
                    ReviewTwo.delete(0,'end')
                    ReviewThree.delete(0,'end')
                    stucombo2.set('--- select option ---')
                    stucombo3.set('--- select option ---')
                    stucombo1.set('--- select option ---')
                if(s1!="" or s2!="" or s3!="" or s4!="--- select option ---" or s5!="--- select option ---" or s6!="--- select option ---"):
                    total=str(int(s1)+int(s2)+int(s3))
                    try:
                        cursor.execute("select * from student where studid1='%s' and dept='%s' and stream='%s' and batch='%s'"%(s,s4,s5,s6))
                        r=cursor.fetchone()
                        if r:
                            cursor.execute("insert into ReviewMark(userId,dept,stream,batch,reviewOne,reviewTwo,reviewThree,total) values ('%s','%s','%s','%s','%s','%s','%s','%s')"%(s,s4,s5,s6,s1,s2,s3,total))
                            conn.commit()
                            refresh()
                            messagebox.showinfo("Update","Successfull")
                        else:
    
                            cursor.execute("select * from student where studid2='%s' and dept='%s' and stream='%s' and batch='%s'"%(s,s4,s5,s6))
                            r=cursor.fetchone()
                            if r:
                                cursor.execute("insert into ReviewMark(userId,dept,stream,batch,reviewOne,reviewTwo,reviewThree,total) values ('%s','%s','%s','%s','%s','%s','%s','%s')"%(s,s4,s5,s6,s1,s2,s3,total))
                                conn.commit()
                                refresh()
                                messagebox.showinfo("Update","Successfull")
                            else:
                                messagebox.showerror("Failed","Student Id not Found")

                    except:
                            messagebox.showerror("update","Failed")
                else:
                    messagebox.showerror("Required","Please Fill the Entry")
            

            btn=Button(mark_frame,text="Update",command=fun)
            btn.place(x=120,y=350)
        
        #hide-indication of other button 
        def hide_indicate():
       
            home_indicate.config(bg="grey")
            Abstract_indicate.config(bg='grey')
            proposal_indicate.config(bg='grey')
            student_review_indicate.config(bg='grey')
            student_final_indicate.config(bg='grey')
            Review_mark_indicate.config(bg='grey')
            student_Report_indicate.config(bg='grey')

        #solve the problem of overlapping the text
        def delete_page():
            #winfo children is method that access the method current Object
            for frame in main_frame.winfo_children():
                frame.destroy()
        #show-indicstion of current button
        def indicate(self,page):
            hide_indicate()
            self.config(bg='blue')
            delete_page()
            page()

    

        option_frame=Frame(root,bg="grey")

        #button
        home_btn=Button(option_frame,text='HOME',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(home_indicate,home_page))
        home_btn.place(x=10,y=50)
    

        home_indicate=Label(option_frame,text='',bg='grey')
        home_indicate.place(x=3,y=50,width=5,height=40)

        Abstract=Button(option_frame,text='Abstract',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(Abstract_indicate,Abstract_page))
        Abstract.place(x=10,y=100)

        Abstract_indicate=Label(option_frame,text='',bg='grey')
        Abstract_indicate.place(x=3,y=100,width=5,height=40)

        proposal=Button(option_frame,text='Proposal',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(proposal_indicate,proposal_page))
        proposal.place(x=10,y=150)

        proposal_indicate=Label(option_frame,text='',bg='grey')
        proposal_indicate.place(x=3,y=150,width=5,height=40)

        student_review=Button(option_frame,text='Review',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_review_indicate,student_review_page))
        student_review.place(x=10,y=200)

        student_review_indicate=Label(option_frame,text='',bg='grey')
        student_review_indicate.place(x=3,y=200,width=5,height=40)

        student_final=Button(option_frame,text='Final Docs',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_final_indicate,student_final_page))
        student_final.place(x=10,y=250)

        student_final_indicate=Label(option_frame,text='',bg='grey')
        student_final_indicate.place(x=3,y=250,width=5,height=40)

        Review_Mark=Button(option_frame,text='Mark',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(Review_mark_indicate,Review_mark_page))
        Review_Mark.place(x=10,y=300)

        Review_mark_indicate=Label(option_frame,text='',bg='grey')
        Review_mark_indicate.place(x=3,y=300,width=5,height=40)

        student_Report=Button(option_frame,text='Report',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_Report_indicate,student_Report_page))
        student_Report.place(x=10,y=350)

        student_Report_indicate=Label(option_frame,text='',bg='grey')
        student_Report_indicate.place(x=3,y=350,width=5,height=40)

        option_frame.pack(side=LEFT)
        option_frame.pack_propagate(False)
        option_frame.configure(width=120,height=500)


        main_frame=Frame(root,highlightbackground='black',highlightthickness=2)


        main_frame.pack()
        main_frame.pack_propagate(False)
        main_frame.configure(width=600,height=520)
    guide_login_page()

def registeration_login():
            
    def student_registeration_page():

        def stu_regis():
            s1=stucombo1.get()
            s2=stucombo2.get()
            s3=stuname.get()
            s4=stuid.get()
            s5=stuemail.get()
            s6=var_radio.get()
            s7=stucombo3.get()
            s8=stusernameEntry.get()
            s9=stpassEntry.get()
            s10=strepass.get()
            pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,6}+\.[a-z]{1,2}$"
            s11=pairEntryname.get()
            s12=pairstidEntry.get()
            s13=pairemailEntry.get()
            s14=stucombo4.get()

    
            
            if(s14 =='--- select option ---'or s1 =='--- select option ---' or s3 =='' or s2 =='--- select option ---' or s4 =='' or s5 =='' or s6 =='' or s7 =='--- select option ---' or s8=='' or s9=='' or s10==''):    
                messagebox.showerror('Error','Field cannot be empty !\n Please full all the feild ')
            elif (s1=='--- select option ---' or s2=='--- select option ---' or s7=='--- select option ---'):
                messagebox.showerror('Error','Field cannot be empty !\n Please full all the feild ')
            elif (s9 != s10):
                messagebox.showerror('Password Error','Recheck the Password')
            elif(s3.isdigit() or len(s3)<5):
                messagebox.showerror('Error','Please Enter the Valid Name !')
            elif(s5 !=''):
                pass
                    
            elif(s6=='p'):
                if(s11.isdigit() or len(s11)<5):
                    messagebox.showerror('Error','Please Enter the Valid Name !')
            elif(s6=='p'):
                if(s13 !=''):
                    if re.match(pat,s13):
                        pass

                    else:
                        messagebox.showerror('Email Id Error','Enter the correct email')
            def db():
                con=pymysql.connect(host='localhost',user='root',password='',database='tcarts')
                cursor=con.cursor()
                st="INSERT INTO `student`(`batch`, `dept`, `name1`, `studid1`, `email1`, `type`, `stream`, `username`, `password`, `confirmpassword`, `name2`, `studid2`, `email2`,`gender`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                a=(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14)
                m=""
                try:
                    cursor.execute(st%a)
                    cursor.execute('insert into abstractmessage(userID,userID2,message) values(%s,%s,%s)',(s4,s12,m))

                    messagebox.showinfo('SUCCESSFULL','Register Successfully !')
                except :
                    messagebox.showerror('FAILED','Registeration Failed !')
                finally:
                    con.commit()
                    cursor.close()
                    con.close()
            if(s1!='' and s3 !='' and s2 !='' and s4 !='' and s5 !='' and s6!='' and s7!='' and s8!='' and s14!='' and s9==s10):
                if(s14=='--- select option ---'or s1 =='--- select option ---' or s2=='--- select option ---' or s7=='--- select option ---'):
                    messagebox.showerror('Error','Field cannot be empty !\n Please full all the feild ')
                else :
                    if re.match(pat,s5):
                        db()
                    else:
                        messagebox.showerror('Email Id Error','Enter the correct email')

        def stu_reset():
            stucombo1.delete(0,'end')
            stucombo1.set('--- select option ---')
            stucombo2.delete(0,'end')
            stucombo2.set('--- select option ---')
            stuname.delete(0,'end')
            stuid.delete(0,'end')
            stuemail.delete(0,'end')
            stucombo3.delete(0,'end')
            stucombo3.set('--- select option ---')
            stucombo4.set('--- select option ---')
            stusernameEntry.delete(0,'end')
            stpassEntry.delete(0,'end')
            strepass.delete(0,'end')
            pairEntryname.delete(0,'end')
            pairstidEntry.delete(0,'end')
            pairemailEntry.delete(0,'end')
            pairEntryname.delete(0,'end')
            pairstidEntry.delete(0,'end')
            pairemailEntry.delete(0,'end')
            
        frame=Frame(main_frame,width=500,height=400)
        frame.pack()
        
        l=Label(frame,text="STUDENT REGISTRATION")
        l.place(x=155,y=20)

        batch=Label(frame,text='Batch :')
        batch.place(x=40,y=50)
        stucombo1=ttk.Combobox(frame)
        stucombo1.place(x=90,y=50)
        stucombo1.config(values=('2019','2020','2021','2022','2023','2024'))
        stucombo1.set('--- select option ---')
        
        dept=Label(frame,text='Course :')
        dept.place(x=240,y=50)
        stucombo2=ttk.Combobox(frame)
        stucombo2.place(x=320,y=50)
        stucombo2.config(values=('CS','IT','CA','DS','BBA','CGS','MATHS','PHY','CH','EN','TAMIL','PSY','B.com-BPS','B.com-CA','B.com-PA','B.com','B.com-HONOURS','BIOTECH','MICRO-BIOLOGY','ZOLOGY'))
        stucombo2.set('--- select option ---')
        
        l1=Label(frame,text='Name :')
        l1.place(x=40,y=80)
        stuname=Entry(frame)
        stuname.place(x=90,y=80)
    
        l2=Label(frame,text='Id no :')
        l2.place(x=40,y=110)
        stuid=Entry(frame)
        stuid.place(x=90,y=110)

        l3=Label(frame,text='Email :')
        l3.place(x=40,y=140)
        stuemail=Entry(frame)
        stuemail.place(x=90,y=140)
# pair name,id and email
        pairn1=Label(frame,text='Name :')
        pairn1.place(x=250,y=80)
        pairEntryname=Entry(frame)
        pairEntryname.place(x=320,y=80)
    
        paire1=Label(frame,text='Id no :')
        paire1.place(x=250,y=110)
        pairstidEntry=Entry(frame)
        pairstidEntry.place(x=320,y=110)

        paire2=Label(frame,text='Email :')
        paire2.place(x=250,y=140)
        pairemailEntry=Entry(frame)
        pairemailEntry.place(x=320,y=140)

        var_radio=StringVar()   
        def des():
            if(var_radio.get()=='s'):
                pairEntryname.config(state='disabled')
                pairstidEntry.config(state='disabled')
                pairemailEntry.config(state='disabled')
            elif(var_radio.get()=='p'):
                pairEntryname.config(state='normal')
                pairstidEntry.config(state='normal')
                pairemailEntry.config(state='normal')
            
                

        l4=Label(frame,text='Type :')
        l4.place(x=40,y=170)
        
        r1=Radiobutton(frame,text='single',value='s',variable=var_radio,command=des)
        r1.place(x=85,y=170)
        r2=Radiobutton(frame,text='Pair',value='p',variable=var_radio,command=des)
        r2.place(x=140,y=170)
        var_radio.set('s')
        pairEntryname.config(state='disabled')
        pairstidEntry.config(state='disabled')
        pairemailEntry.config(state='disabled')
    
        studentstream=Label(frame,text='Stream :')
        studentstream.place(x=250,y=170)
        stucombo3=ttk.Combobox(frame)
        stucombo3.place(x=320,y=170)
        stucombo3.config(values=('Aided','SF'))
        stucombo3.set('--- select option ---')
        
        l5=Label(frame,text='User Name :')
        l5.place(x=40,y=200)
        stusernameEntry=Entry(frame)
        stusernameEntry.place(x=120,y=200)


        studentgender=Label(frame,text='Gender :')
        studentgender.place(x=250,y=200)
        stucombo4=ttk.Combobox(frame)
        stucombo4.place(x=320,y=200)
        stucombo4.config(values=('m','f'))
        stucombo4.set('--- select option ---')

        
        l6=Label(frame,text='Password :')
        l6.place(x=40,y=230)
        stpassEntry=Entry(frame,show='*')
        stpassEntry.place(x=120,y=230)

        l7=Label(frame,text='Confirm Password :')
        l7.place(x=250,y=230)
        strepass=Entry(frame,show='*')
        strepass.place(x=370,y=230)
        
        guide_btn=Button(frame,text="Submit",command=stu_regis)
        guide_btn.place(x=150,y=300)

        guide_btn2=Button(frame,text="Reset",command=stu_reset)
        guide_btn2.place(x=250,y=300)

    
        
#staff registeration page
    def staff_registeration_page():
        def guide_regis():
            
        
            s1=staffcombo.get()
            s2=gnameEntry.get()
            s3=gidEntry.get()
            s4=gemailEntry.get()
            s5=gusernameEntry.get()
            s6=gpassEntry.get()
            s7=grepass.get()
            s8=staffcombo2.get()
            pat = "^[a-zA-Z0-9-_]+@+tcarts+\.in$"

        # valided for empty field !
            if(s1 =='--- select option ---' or s3 =='' or s2 =='' or s4 =='' or s5 =='' or s6 =='' or s7 =='' or s8=='--- select option ---'):
                messagebox.showerror('Error','Field cannot be empty !\n Please full all the feild ')
            elif (s1=='---select option ---' or s8=='---select option ---'):
                messagebox.showerror('Error','Field cannot be empty !\n Please full all the feild ')       
            
            elif(s2.isdigit() or len(s2)<5):
                messagebox.showerror('Error','Please Enter the Valid Name !')
            elif(s4 !=''):
                pass
            elif(len(s3)<6):
                messagebox.showerror('Error','check the Id number!')
#checking the both password feild has same String
            if(s6 != s7):
                messagebox.showerror('Password Error','Recheck the Password')
            
            def db():
                con=pymysql.connect(host="localhost",user="root",password="",database="tcarts")
                cursor=con.cursor()
                st="INSERT INTO `guide`(`depart`, `stream`, `name`, `gid`, `email`, `username`, `password`, `confirmpassword`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"
                a=(s1,s8,s2,s3,s4,s5,s6,s7)
                try:
                    cursor.execute(st%a)
                    messagebox.showinfo('SUCCESSFULL','Registered Successfully !')
                except :
                    messagebox.showerror('FAILED','Registeration Failed !')
                finally:
                    con.commit()
                    cursor.close()
                    con.close()
                    
            
            #if all the field is not empty.database connecting
            if(s1!='' and s3 !='' and s2 !='' and s4 !='' and s5 !='' and s6==s7 and s8 !=''):
                if(s1=='--- select option ---' or s8=='--- select option ---'):
                    messagebox.showerror('Error','Field cannot be empty !\n Please full all the feild ')
                else :
                    if re.match(pat,s4):
                        db()
                    else:
                        messagebox.showerror('Email Id Error','Enter the correct email')
            
                
        def mentor_regis():
            s1=staffcombo.get()
            s2=gnameEntry.get()
            s3=gidEntry.get()
            s4=gemailEntry.get()
            s5=gusernameEntry.get()
            s6=gpassEntry.get()
            s7=grepass.get()
            s8=staffcombo2.get()
            pat = "^[a-zA-Z0-9-_]+@+tcarts+\.in$"

        # valided for empty field !
            if(s1 =='--- select option ---' or s3 =='' or s2 =='' or s4 =='' or s5 =='' or s6 =='' or s7 =='' or s8=='--- select option ---'):
                messagebox.showerror('Error','Field cannot be empty !\n Please full all the feild ')
            elif (s1=='---select option ---' or s8=='---select option ---'):
                messagebox.showerror('Error','Field cannot be empty !\n Please full all the feild ')       
            
            elif(s2.isdigit() or len(s2)<5):
                messagebox.showerror('Error','Please Enter the Valid Name !')
            elif(s4 !=''):
                pass
            elif(len(s3)<6):
                messagebox.showerror('Error','check the Id number!')
#checking the both password feild has same String
            if(s6 != s7):
                messagebox.showerror('Password Error','Recheck the Password')
            def db2():
                con=pymysql.connect(host="localhost",user="root",password="",database="tcarts")
                cursor=con.cursor()
                sts="INSERT INTO `mentor`(`depart`, `stream`, `name`, `mid`, `email`, `username`, `password`, `confirmpassword`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"
                a1=(s1,s8,s2,s3,s4,s5,s6,s7)
                try:
                    cursor.execute(sts%a1)
                    messagebox.showinfo('SUCCESSFULL','Registered Successfully !')
                except :
                    messagebox.showerror('FAILED','Registeration Failed !')
                finally:
                    con.commit()
                    cursor.close()
                    con.close()
            if(s1!='' and s3 !='' and s2 !='' and s4 !='' and s5 !='' and s6==s7 and s8 !=''):
                if(s1=='--- select option ---' or s8=='--- select option ---'):
                   messagebox.showerror('Error','Field cannot be empty !\n Please full all the feild ')
                else :
                    if re.match(pat,s4):
                        db2()
                    else:
                        messagebox.showerror('Email Id Error','Enter the correct email')
       
# on click Button to reset in guide field
        def guide_reset():
            staffcombo.delete(0,'end')
            staffcombo.set('--- select option ---')
            gnameEntry.delete(0,'end')
            gidEntry.delete(0,'end')
            gemailEntry.delete(0,'end')
            staffcombo2.delete(0,'end')
            staffcombo2.set('--- select option ---')
            gusernameEntry.delete(0,'end')
            gpassEntry.delete(0,'end')
            grepass.delete(0,'end')
            
        frame=Frame(main_frame,width=500,height=400)
        frame.pack()
        
        l=Label(frame,text="STAFF REGISTRATION",fg='red')
        l.place(x=155,y=20)

       

        dept=Label(frame,text='Course :')
        dept.place(x=40,y=50)
        staffcombo=ttk.Combobox(frame)
        staffcombo.place(x=160,y=50)
        staffcombo.config(values=('CS','IT','CA','DS','BBA','CGS','MATHS','PHY','CH','EN','TAMIL','PSY','B.com-BPS','B.com-CA','B.com-PA','B.com','B.com-HONOURS','BIOTECH','MICRO-BIOLOGY','ZOLOGY'))
        staffcombo.set('--- select option ---')
        
        l1=Label(frame,text='Name :')
        l1.place(x=40,y=80)
        gnameEntry=Entry(frame)
        gnameEntry.place(x=160,y=80)
    
        l2=Label(frame,text='ID No:')
        l2.place(x=40,y=110)
        gidEntry=Entry(frame)
        gidEntry.place(x=160,y=110)

        l3=Label(frame,text='Email :')
        l3.place(x=40,y=140)
        gemailEntry=Entry(frame)
        gemailEntry.place(x=160,y=140)

        stream=Label(frame,text='Stream :')
        stream.place(x=40,y=170)
        staffcombo2=ttk.Combobox(frame)
        staffcombo2.place(x=160,y=170)
        staffcombo2.config(values=('Aided','SF'))
        staffcombo2.set('--- select option ---')
        
        l4=Label(frame,text='User Name :')
        l4.place(x=40,y=200)
        gusernameEntry=Entry(frame)
        gusernameEntry.place(x=160,y=200)

        l5=Label(frame,text='Password :')
        l5.place(x=40,y=230)
        gpassEntry=Entry(frame,show='*')
        gpassEntry.place(x=160,y=230)

        l6=Label(frame,text='Confirm Password :')
        l6.place(x=40,y=260)
        grepass=Entry(frame,show='*')
        grepass.place(x=160,y=260)


        guide_btn=Button(frame,text="Submit",command=guide_regis)
        guide_btn.place(x=100,y=300)

        guide_btn2=Button(frame,text="Reset",command=guide_reset)
        guide_btn2.place(x=170,y=300)

        guide_btn3=Button(frame,text="Mentor",command=mentor_regis)
        guide_btn3.place(x=240,y=300)
    
    def login_page():
        
        show_face='hide'
        hide_face='show'
        def show_hide_password():
            if logpassEntry['show']=='*':
                logpassEntry.configure(show='')
                sho_btn.configure(text=show_face)
            else :
                logpassEntry.configure(show='*')
                sho_btn.configure(text=hide_face)
        def loginas():
            s1=logcombobox.get()
            s2=logusernameEntry.get()
            s3=logpassEntry.get()
            if (s2=='' or s3=='' or s1=="--- select option--"):
                messagebox.showerror('Login Error','please fill the Require Fields !')
            if(s1=='Student'):
                if(s2 !='' and s3 !=''):
                    con=pymysql.connect(host='localhost',user='root',password='',db='tcarts')
                    cursor=con.cursor()
                    st="select * from student where username=%s and password=%s"
                    cursor.execute(st,[(s2),(s3)])
                    r=cursor.fetchall()
                    if r:
                        for i in r:
                            x=str(i[3])
                            y=str(i[11])
                        main_frame.destroy()
                        option_frame.destroy()
                        student_login(x,y)
                    else:
                        messagebox.showerror('Login Error','No data Found')

            elif(s1=='Guide'):
                if(s2 !='' and s3 !=''):
                    con=pymysql.connect(host='localhost',user='root',password='',db='tcarts')
                    cursor=con.cursor()
                    st="select * from guide where username=%s and password=%s"
                    cursor.execute(st,[(s2),(s3)])
                    r=cursor.fetchall()
                    if r:
                        for i in r:
                            x=str(i[3])
                        main_frame.destroy()
                        option_frame.destroy()
                        guide_login(x)
                    else:
                        messagebox.showerror('Login Error','No data Found')
                    
            elif(s1=='Mentor'):
                if(s2 !='' and s3 !=''):
                    con=pymysql.connect(host='localhost',user='root',password='',db='tcarts')
                    cursor=con.cursor()
                    st="select * from mentor where username=%s and password=%s"
                    cursor.execute(st,[(s2),(s3)])
                    r=cursor.fetchall()
                    if r:
                        for i in r:
                            x=str(i[3])
                        main_frame.destroy()
                        option_frame.destroy()
                        mentor_login(x)
                    else:
                        messagebox.showerror('Login Error','No data Found')
                    

        
            

                    
    #forget password
        
        def forget():
            Login_frame.destroy()
            frame1=Frame(main_frame,width=500,height=400)
            frame1.pack()

            forl1=Label(frame1,text='FORGET PASSWORD',fg='green')
            forl1.place(x=155,y=20)
            
            forl2=Label(frame1,text='Select :')
            forl2.place(x=60,y=50)
            fors=ttk.Combobox(frame1)
            fors.place(x=160,y=50)
            fors.config(values=('Student','Guide','Mentor'))
            fors.set("--- select option ---")

            forl3=Label(frame1,text='Id :')
            forl3.place(x=60,y=80)
            fore1=Entry(frame1)
            fore1.place(x=160,y=80)
            
            forl4=Label(frame1,text='User Name :')
            forl4.place(x=60,y=110)
            fore2=Entry(frame1)
            fore2.place(x=160,y=110)

            forl5=Label(frame1,text='New Password :')
            forl5.place(x=60,y=140)
            fore3=Entry(frame1,show='*')
            fore3.place(x=160,y=140)

            forl5=Label(frame1,text='Confirm Password :')
            forl5.place(x=50,y=170)
            fore4=Entry(frame1,show='*')
            fore4.place(x=160,y=170)

            def login_forward():
                frame1.destroy()
                login_page()
            
            def update_Details():
                s1=fors.get()
                s2=fore1.get()
                s3=fore2.get()
                s4=fore3.get()
                s5=fore4.get()
                if(s4==s5):
                    if(s1=="--- select option ---"or s2=='' or s3=='' or s4=='' or s5==''):
                        messagebox.showerror('Login Error','please fill the Require Fields !')
                    elif(s2 !='' and s3 !='' and s4 !="" and s5 !=""):
                        if(s1=='Student'):
                            con=pymysql.connect(host='localhost',user='root',password='',db='tcarts')
                            cursor=con.cursor()
                            try:
                                cursor.execute("select * from student where username='%s' and studid1='%s'"%(s3,s2))
                                r=cursor.fetchall()
                                if r:
                                    cursor.execute("update student set confirmpassword='%s',password='%s' where studid1='%s' and username='%s'"%(s5,s4,s2,s3))
                                    con.commit()
                                    messagebox.showinfo('Success','Update SuccessFull !')
                                else:
                                    messagebox.showerror('FAILED','Student Updation Failed')
                            except:
                                try:
                                    cursor.execute("select * from student where username='%s' and studid2='%s'"%(s3,s2))
                                    r=cursor.fetchall()
                                    if r:
                                        cursor.execute("update student set confirmpassword='%s',password='%s' where studid2='%s' and username='%s'"%(s5,s4,s2,s3))
                                        con.commit()
                                        messagebox.showinfo('Success','Update SuccessFull !')
                                    else:
                                        messagebox.showerror('FAILED','Student Updation Failed')
                                except:
                                    messagebox.showerror('FAILED','Student Updation Failed')
                            finally:
                                con.close()
                                cursor.close()
                        elif(s1=='Guide'):
                            con=pymysql.connect(host='localhost',user='root',password='',db='tcarts')
                            cursor=con.cursor()
                            try:
                                cursor.execute("select * from guide where username='%s' and gid='%s'"%(s3,s2))
                                r=cursor.fetchall()
                                if r:
                                    cursor.execute("update guide set confirmpassword='%s',password='%s' where gid='%s' and username='%s'"%(s5,s4,s2,s3))
                                    con.commit()
                                    messagebox.showinfo('Success','Update SuccessFull !')
                                else :
                                    messagebox.showerror('FAILED','guide Updation Failed')
                            except:
                                messagebox.showerror('FAILED','guide Updation Failed')
                            finally:
                                con.close()
                                cursor.close()
                        elif(s1=='Mentor'):
                            con=pymysql.connect(host='localhost',user='root',password='',db='tcarts')
                            cursor=con.cursor()
                            try:
                                cursor.execute("select * from mentor where username='%s' and mid='%s'"%(s3,s2))
                                r=cursor.fetchall()
                                #print(r)
                                if r:
                                    cursor.execute("update mentor set confirmpassword='%s',password='%s' where mid='%s' and username='%s'"%(s5,s4,s2,s3))
                                    con.commit()
                                    messagebox.showinfo('Success','Update SuccessFull !')
                                else :
                                    messagebox.showerror('FAILED','guide Updation Failed')
                            except:
                                messagebox.showerror('FAILED','Mentor Updation Failed')
                            finally:
                                con.close()
                                cursor.close()
                        else:
                            messagebox.showerror('Failed','Updation Failed')
                    else:
                        messagebox.showerror('Login Error','please fill the Require Fields !')
               


                else:
                    messagebox.showerror('Login Error','password and Confirm password are mismatched!')

            forbtn=Button(frame1,text='Update',command=update_Details)
            forbtn.place(x=120,y=210)
            forbtn2=Button(frame1,text='Login',command=login_forward)
            forbtn2.place(x=190,y=210)
            

    #reset in login Entry box and Combobox    
        def loginreset():
            logusernameEntry.delete(0,END)
            logpassEntry.delete(0,END)
            logcombobox.delete(0,'end')
            logcombobox.set("--- select option ---")
            
        Login_frame=Frame(main_frame,width=500,height=400)
        Login_frame.pack()    
        
        
        l=Label(Login_frame,text="LOGIN",fg='red')
        l.place(x=155,y=20)
        
        logl1=Label(Login_frame,text='Select :')
        logl1.place(x=60,y=50)
        logcombobox=ttk.Combobox(Login_frame)
        logcombobox.place(x=160,y=50)
        logcombobox.config(values=('Student','Guide','Mentor'))
        logcombobox.set("--- select option ---")
        
        logl2=Label(Login_frame,text='Username :')
        logl2.place(x=60,y=80)
        logusernameEntry=Entry(Login_frame)
        logusernameEntry.place(x=160,y=80)

        logl3=Label(Login_frame,text='Password :')
        logl3.place(x=60,y=110)
        logpassEntry=Entry(Login_frame,show='*')
        logpassEntry.place(x=160,y=110)
        sho_btn=Button(Login_frame,text=hide_face,command=show_hide_password,fg='blue',bd=0)
        sho_btn.place(x=300,y=110)

        logbtn=Button(Login_frame,text='Sign in',command=loginas)
        logbtn.place(x=120,y=160)

        logbtn2=Button(Login_frame,text='Reset',command=loginreset)
        logbtn2.place(x=220,y=160)

        logbtn3=Button(Login_frame,text='forget Password ?',command=forget,fg='red',bd=0)
        logbtn3.place(x=120,y=200)
       
    #hide-indication of other button 
    def hide_indicate():
        
        #home_indicate.config(bg="grey")
        student_registeration_indicate.config(bg='grey')
        staff_registeration_indicate.config(bg='grey')
        login_indicate.config(bg='grey')
    #solve the problem of overlapping the text
    def delete_page():
        #winfo children is method that access the method current Object
        for frame in main_frame.winfo_children():
            frame.destroy()
    #show-indicstion of current button
    def indicate(self,page):
        hide_indicate()
        self.config(bg='blue')
        delete_page()
        page()

    

    option_frame=Frame(root,bg="grey")

    #home page button
    

    student_registeration=Button(option_frame,text='STUDENT',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(student_registeration_indicate,student_registeration_page))
    student_registeration.place(x=10,y=50)

    student_registeration_indicate=Label(option_frame,text='',bg='grey')
    student_registeration_indicate.place(x=3,y=50,width=5,height=40)

    staff_registeration=Button(option_frame,text='STAFF',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(staff_registeration_indicate,staff_registeration_page))
    staff_registeration.place(x=10,y=100)

    staff_registeration_indicate=Label(option_frame,text='',bg='grey')
    staff_registeration_indicate.place(x=3,y=100,width=5,height=40)

    login=Button(option_frame,text='LOGIN',font=('bold',15),fg='blue',bd=0,bg='grey',command=lambda:indicate(login_indicate,login_page))
    login.place(x=10,y=150)

    login_indicate=Label(option_frame,text='',bg='grey')
    login_indicate.place(x=3,y=150,width=5,height=40)

    option_frame.pack(side=LEFT)
    option_frame.pack_propagate(False)
    option_frame.configure(width=120,height=500)

    
    main_frame=Frame(root,highlightbackground='black',highlightthickness=2)


    main_frame.pack()
    main_frame.pack_propagate(False)
    main_frame.configure(width=600,height=520)

    
registeration_login()

root.mainloop()


