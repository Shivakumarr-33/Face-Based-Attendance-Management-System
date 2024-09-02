from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    _instance = None

    def __new__(cls, root):
        if cls._instance is None:
            cls._instance = super(Attendance, cls).__new__(cls)
            cls._instance._initialize(root)
        return cls._instance

    def _initialize(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # *********variables*********
        self.var_atten_Id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten__attendance = StringVar()

        # first image
        img = Image.open(r"College_Images\smart-attendance.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # 2nd image
        img2 = Image.open(r"College_Images\iStock-182059956_18390_t12.jpg")
        img2 = img2.resize((800, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=800, height=200)

        title_lbl = Label(text="ATTENDENCE MANAGEMENT SYSTEM", font=("comicsansns", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=200, width=1530, height=45)

        main_frame = Frame(bd=2, bg="white")
        main_frame.place(x=0, y=250, width=1530, height=600)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendence Details", font=("comicsansns", 12, "bold"))
        left_frame.place(x=10, y=10, width=760, height=580)

        img_left = Image.open(r"College_Images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((750, 150), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=150)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=155, width=720, height=370)

        # label entry
        # attendence id
        attendence_Id_label = Label(left_inside_frame, text="AttendenceId:", font="comicsansns 12 bold", bg="white")
        attendence_Id_label.grid(row=0, column=0, padx=5, pady=5)

        attendence_Id_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_Id, font="comicsansns 12 bold")
        attendence_Id_entry.grid(row=0, column=1, padx=5, pady=5)

        # student name
        studentname_label = Label(left_inside_frame, text="Name:", font=("comicsansns", 12, "bold"), bg="white")
        studentname_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        studentname_entry = ttk.Entry(left_inside_frame, width=25, textvariable=self.var_atten_name, font=("comicsansns", 12, "bold"))
        studentname_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # time
        time_label = Label(left_inside_frame, text="Time:", font=("comicsansns", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("comicsansns", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # roll no
        roll_no_label = Label(left_inside_frame, text="Roll No:", font=("comicsansns", 12, "bold"), bg="white")
        roll_no_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll, font=("comicsansns", 12, "bold"))
        roll_no_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # dep
        dep_label = Label(left_inside_frame, text="Department:", font=("comicsansns", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        dep_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("comicsansns", 12, "bold"))
        dep_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # date
        date_label = Label(left_inside_frame, text="Date:", font=("comicsansns", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("comicsansns", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # attendence
        attendence_label = Label(left_inside_frame, text="Attendence Status:", font=("comicsansns", 12, "bold"), bg="white")
        attendence_label.grid(row=3, column=0, padx=10, pady=5)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten__attendance, font=("comicsansns", 12, "bold"), width=17, state="read only")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, pady=10, sticky=W)
        self.atten_status.bind('<Key>', lambda e: 'break')

        # button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=280, width=745, height=70)

        save_btn = Button(btn_frame, text="ImportCsv", width=18, command=self.importCsv, font=("comicsansns", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        delete_btn = Button(btn_frame, text="ExportCsv", command=self.exportCsv, width=18, font=("comicsansns", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=18, font=("comicsansns", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=15, font=("comicsansns", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendence Details", font=("comicsansns", 12, "bold"))
        Right_frame.place(x=780, y=10, width=650, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=642, height=460)

        # *************scroll bar*********
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendenceReportTable = ttk.Treeview(table_frame, column=("id", "RollNo", "Name", "Department", "Time", "Date", "Status"),
        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id", text="Attendence ID")
        self.AttendenceReportTable.heading("RollNo", text="RollNo")
        self.AttendenceReportTable.heading("Name", text="Name")
        self.AttendenceReportTable.heading("Department", text="Department")
        self.AttendenceReportTable.heading("Time", text="Time")
        self.AttendenceReportTable.heading("Status", text="Status")
        self.AttendenceReportTable.heading("Date", text="Date")

        self.AttendenceReportTable["show"] = "headings"
        self.AttendenceReportTable.column("id", width=100)
        self.AttendenceReportTable.column("Name", width=100)
        self.AttendenceReportTable.column("Time", width=100)
        self.AttendenceReportTable.column("Status", width=100)
        self.AttendenceReportTable.column("RollNo", width=100)
        self.AttendenceReportTable.column("Department", width=100)
        self.AttendenceReportTable.column("Date", width=100)

        self.AttendenceReportTable.pack(fill=BOTH, expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ****************fetch data***********
    def fetchData(self, rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("", END, values=i)

    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()

        try:
            if self.root is None or not self.root.winfo_exists():
                raise RuntimeError("Main window is not available.")

            fln = filedialog.askopenfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )

            if fln:
                with open(fln) as myfile:
                    csvread = csv.reader(myfile, delimiter=",")
                    for i in csvread:
                        mydata.append(i)
                self.fetchData(mydata)
            else:
                messagebox.showwarning("No File Selected", "Please select a CSV file.", parent=self.root)
        except Exception as e:
            if self.root is not None and self.root.winfo_exists():
                messagebox.showerror("Error", f"Failed to import CSV file: {e}", parent=self.root)

    def exportCsv(self):
        try:
            if self.root is None or not self.root.winfo_exists():
                raise RuntimeError("Main window is not available.")

            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )

            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    csvwrite = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        csvwrite.writerow(i)
                messagebox.showinfo("Success", "Data exported successfully", parent=self.root)
        except Exception as es:
            if self.root is not None and self.root.winfo_exists():
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event):
        cursor_row = self.AttendenceReportTable.focus()
        content = self.AttendenceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_Id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten__attendance.set(rows[6])

    # ****reset function*****
    def reset_data(self):
        self.var_atten_Id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten__attendance.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
