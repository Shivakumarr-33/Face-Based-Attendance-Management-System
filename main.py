from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox
import os
from time import strftime
from datetime import datetime
from student import student
from train import Train
from face_recognition import Face_Recognition
from attedence import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"College_Images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #2nd image
        img2=Image.open(r"College_Images\facialrecognition.png")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
    

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)



        #3rd image
        img3=Image.open(r"College_Images\images.jpg")
        img3=img3.resize((500,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
    

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        #bg image
        img4=Image.open(r"College_Images\sphn.jpg")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
    

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #**************time******************
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)


        lbl=Label(title_lbl,font=("times new roman",12,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=100,height=50)
        time()

        #student button
        img5=Image.open(r"College_Images\student.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=80,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=100,y=300,width=220,height=40)
   

         #Detector button
        img6=Image.open(r"College_Images\Detector.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=80,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=400,y=300,width=220,height=40)
   

        #Attdence button
        img7=Image.open(r"College_Images\report.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendence_data)
        b1.place(x=700,y=80,width=220,height=220)
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=700,y=300,width=220,height=40)



         #help button
        img8=Image.open(r"College_Images\help desk.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=80,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1000,y=300,width=220,height=40)



        #train button
        img9=Image.open(r"College_Images\train.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=100,y=600,width=220,height=40)



        #photos button
        img10=Image.open(r"College_Images\opencv_face_reco_more_data.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=400,y=600,width=220,height=40)

        #Developer button
        img11=Image.open(r"College_Images\Bill_Gates.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=700,y=600,width=220,height=40)

         #Exit button
        img12=Image.open(r"College_Images\exit.jpg")
        img12=img12.resize((220,220),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.IExit)
        b1.place(x=1000,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.IExit,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1000,y=600,width=220,height=40)

    def open_img(self):
        os.startfile("Data")

    def IExit(self):
        self.IExit=messagebox.askyesno("Face Recognition","Are You Want To Exit")
        if self.IExit >0:
            self.root.destroy()
        else:
            return

#*****************functions button****************

    def student_details(self):
        self.new_window = Toplevel(self.root)  
        self.app = student(self.new_window)  

    def train_data(self):
        self.new_window = Toplevel(self.root)  
        self.app = Train(self.new_window)  

    def face_data(self):
        self.new_window = Toplevel(self.root)  
        self.app = Face_Recognition(self.new_window)  

    def attendence_data(self):
        self.new_window = Toplevel(self.root)  
        self.app = Attendance(self.new_window)  

    def developer_data(self):
        self.new_window = Toplevel(self.root)  
        self.app = Developer(self.new_window)  

    def help_data(self):
        self.new_window = Toplevel(self.root)  
        self.app = Help(self.new_window)
    

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()