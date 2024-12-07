from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from main import Face_Recognition_System


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()