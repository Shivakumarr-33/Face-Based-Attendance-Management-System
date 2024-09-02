from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        #***********variables**********
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_dep=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_photo=StringVar()



        #first image
        img=Image.open(r"C:\Users\shiva\OneDrive\Pictures\College_Images\face-recognition.png")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #2nd image
        img2=Image.open(r"C:\Users\shiva\OneDrive\Pictures\College_Images\imgref3_orig.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
    

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)



        #3rd image
        img3=Image.open(r"C:\Users\shiva\OneDrive\Pictures\College_Images\smart-attendance.jpg")
        img3=img3.resize((500,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
    

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)


         #bg image
        img4=Image.open(r"C:\Users\shiva\OneDrive\Pictures\College_Images\sphn.jpg")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
    

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1510,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=580)
        
          #left first image
        img_left=Image.open(r"C:\Users\shiva\OneDrive\Pictures\College_Images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((750,150),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=150)


        #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=130,width=750,height=160)
        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state='read only')
        dep_combo["values"]=('Select Department',"Aiml","Cse","Csc","Csd","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        dep_combo.bind('<Key>', lambda e: 'break')
    

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","JAVA","ATCD","AI","DM","DBMS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        course_combo.bind('<Key>', lambda e: 'break')
        

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        year_combo.bind('<Key>', lambda e: 'break')



        #Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="read only")
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        sem_combo.bind('<Key>', lambda e: 'break')



        #Class Student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=750,height=280)
        #student id
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10)
        

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=30,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)


        #student name
        studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=25,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        

        class_div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="read only")
        class_div_combo["values"]=("Select Division","A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        class_div_combo.bind('<Key>', lambda e: 'break')



        #Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=25,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="read only")
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)
        gender_combo.bind('<Key>', lambda e: 'break')
        

        #dob
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=25,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=25,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=25,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Radio button

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0)

       
        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=5,column=1)


        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=190,width=745,height=50)


        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=21,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=21,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=21,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #btn frame 1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=220,width=750,height=30)


        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)


        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)

         #Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=650,height=580)

        img_right=Image.open(r"C:\Users\shiva\OneDrive\Pictures\College_Images\facial-recognition_0.jpg")
        img_right=img_right.resize((750,150),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=640,height=150)


        #*****Search System*****
        search_label_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_label_frame.place(x=5,y=155,width=640,height=70)

        search_label=Label(search_label_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(search_label_frame,font=("times new roman",12,"bold"),width=13,state="read only")
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        search_combo.bind('<Key>', lambda e: 'break')


        search_entry=ttk.Entry(search_label_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        
        search_btn=Button(search_label_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        show_all_btn=Button(search_label_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=6)


       # *******Table Frame******
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=220,width=640,height=340)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","div","name","roll","dob","email","phone","gender","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Rollno")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("photo",width=100)
       
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


        # ********function declaration******



    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:

                    try:
                        conn = mysql.connector.connect(host="localhost", username="root", password="Shivakumar@10", database="face_recoginzer")
                        my_cursor = conn.cursor()
                        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_id.get(),
                            self.var_div.get(),
                            self.var_name.get(),
                            self.var_roll.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_gender.get(),
                            self.var_photo.get()
                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Succes","Student Detaills hs been added Succesfully",parent=self.root)
                    except Exception as es:
                         messagebox.showerror("Error",f"Due To :{ str(es)}",parent=self.root)
# Fetch data method and get cursor method should be at the class level, not nested inside another method

# *************** fetch Data************

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Shivakumar@10", database="face_recoginzer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ************get cursor*************
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_div.set(data[5])
        self.var_name.set(data[6])
        self.var_roll.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_gender.set(data[11])
        self.var_photo.set(data[12])

        #*********** Update function ***********

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                if update:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Shivakumar@10",
                        database="face_recoginzer"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student 
                        SET Dep = %s, course = %s, Year = %s, Semester = %s, Division = %s, 
                            Name = %s, Roll = %s, Gender = %s, Dob = %s, Phone = %s, 
                            Photosample = %s 
                        WHERE Student_id = %s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_div.get(),
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_phone.get(),
                        self.var_photo.get(),
                        self.var_id.get()
                    ))

                else:
                     if not update:
                          return
                messagebox.showinfo("succces","student details updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                 messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            
    #*************delete function **********
    def delete_data(self):
         if self.var_id.get()=="":
            messagebox.showerror("Error","student id must required",parent=self.root)
         else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete the student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Shivakumar@10", database="face_recoginzer")
                    my_cursor = conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","succesfully deleted student details",parent=self.root)
            except Exception as es:
                 messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    #*************Reset function***************
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_div.set("Select Division")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_photo.set("")
        self.var_dob.set("")



#********************Genrate data set or take photosample*************
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try: 
                conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Shivakumar@10",
                database="face_recoginzer"
                    )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("""
                        UPDATE student 
                        SET Dep = %s, course = %s, Year = %s, Semester = %s, Division = %s, 
                            Name = %s, Roll = %s, Gender = %s, Dob = %s, Phone = %s, 
                            Photosample = %s 
                        WHERE Student_id = %s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_div.get(),
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_phone.get(),
                        self.var_photo.get(),
                        self.var_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()



                #================load predefined data on face frontals from opencv==========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #mimimum neighbour=5
                    for(x,y,w,h)in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Genrating data sets completed!!!")
            except Exception as es:
                 messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()