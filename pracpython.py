from PIL import Image, ImageTk
import pickle
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import PhotoImage

file_name=input("Enter the file name you want to use : ")

root=tk.Tk()

image=Image.open("C:\\Users\\shama\\OneDrive\\Pictures\\website-hosting-concept-with-circuits11.jpg")
bg_image=ImageTk.PhotoImage(image)

bg_label=tk.Label(root,image=bg_image)
bg_label.place(relwidth=1,relheight=1)

root.title("Data Management")
root.geometry("950x500")
data_area=tk.Text(root,width=57,height=17)
data_area.place(x=460,y=53)

d={}

UPDATE_COUNT_RECORD=1

# CREATING A SECOND WINDOW FOR WRITING DATA ONTO THE FILE 
def write_window():

    global inc
    inc=0

    global new_window
    new_window=tk.Toplevel(root)
    new_window.title("WRITING DATA")
    new_window.geometry("500x300")

    new_image=Image.open("C:\\Users\\shama\\OneDrive\\Pictures\\website-hosting-concept-with-circuits11.jpg")
    new_bg_image=ImageTk.PhotoImage(new_image)

    new_image_label=tk.Label(new_window,image=new_bg_image)
    new_image_label.place(relwidth=1,relheight=1)

    name_label=tk.Label(new_window,text="1) ENTER THE NAME OF THE STUDENT : ",bg="black",fg="white").place(x=0,y=40)
    class_label=tk.Label(new_window,text="2) ENTER THE STUDENTS SECTION : ",bg="black",fg="white").place(x=0,y=80)
    rno_label=tk.Label(new_window,text="3) ENTER THE SUDENT'S ROLL NUMBER : ",bg="black",fg="white").place(x=0,y=120)
    marks_label=tk.Label(new_window,text="4)ENTER THE STUDENT'S MARKS : ",bg="black",fg="white").place(x=0,y=160)
    submit_label=tk.Label(new_window,text=" TO ENTER DATA, CLICK ON  --->",bg="black",fg="white").place(x=0,y=200)
    cont_writing_label=tk.Label(new_window,text="DO YOU WANT TO CONTINUE WRITING?",bg="black",fg="white").place(x=0,y=240)
    
    button_yes=tk.Button(new_window,text="YES",width=15,command=continue_writing_yes,bg="black",fg="white").place(x=1,y=270)
    button_no=tk.Button(new_window,text="NO",width=15,command=continue_writing_no,bg="black",fg="white").place(x=136,y=270)

    global name_area
    name_area=tk.Text(new_window,width=15,height=1)
    name_area.place(x=240,y=40)

    global class_area
    class_area=tk.Text(new_window,width=15,height=1)
    class_area.place(x=240,y=80)

    global rno_area
    rno_area=tk.Text(new_window,width=15,height=1)
    rno_area.place(x=240,y=120)

    global marks_area
    marks_area=tk.Text(new_window,width=15,height=1)
    marks_area.place(x=240,y=160)

    global info_area
    info_area=tk.Text(new_window,width=38,height=1)
    info_area.place(x=0,y=0)


    submit_button=tk.Button(new_window,text="WRITE DATA",width=17,height=1,activeforeground="white",activebackground="green",command=combined_writing,bg="black",fg="white").place(x=240,y=200)

    new_window.mainloop()


def continue_writing_yes():

    name_area.delete("1.0",tk.END)
    rno_area.delete("1.0",tk.END)
    class_area.delete("1.0",tk.END)
    marks_area.delete("1.0",tk.END)


def continue_writing_no():

    new_window.destroy()



# START OF DATA ADDITION

def write_name():

    global name
    try:
        name=name_area.get("1.0","end-1c")
        if len(name)>50:
            messagebox.showerror("NAME ERROR","NAME ENTERED IS TOO LONG [MAX OF 50 CHARACTERs]")
            name=''

    except tk.TclError:
        messagebox.showerror("VALUE ERROR","INVALID VALUE WAS ENTERED IN THE NAME WIDGET")

#------------------------------------------------------------------------------------------------------------------------------

def write_class():

    global stu_class
    try:
        stu_class=class_area.get("1.0","end-1c")
        if stu_class.isdigit():
            messagebox.showwarning("NUMBER/SPECIAL SYMBOL FOUND","NO NUMBERS OR SPECIAL SYMBOLS ALLOWED FOR 'SECTION'")
            
    except tk.TclError:
        messagebox.showwarning("VALUE ERROR", "INVALID VALUE IN THE SECTION WIDGET")

#------------------------------------------------------------------------------------------------------------------------------------

def write_rno():
            
    global rollno
    try:
        rollno=int(rno_area.get("1.0","end-1c"))
        if rollno<=0:
            messagebox.showwarning("NEGATIVE NUMBER","A NEGATIVE NUMBER WAS ENTERED")
            rollno=None
            
    except tk.TclError:
        messagebox.showwarning("VALUE ERROR", "INVALID VALUE IN THE ROLL NUMBER WIDGET")
                
 #--------------------------------------------------------------------------------------------------------
                            
def write_marks():

    global marks
    try:
        marks=int(marks_area.get("1.0","end-1c"))
        if marks<0:
            messagebox.showwarning("NEGATIVE MARKS","NO NEGATIVE MARKS ARE ALLOWED")
            marks=0

    except tk.TclError:
        messagebox.showwarning("VALUE ERROR", "INVALID VALUE IN THE MARKS WIDGET")

#----------------------------------------------------------------------------------------------
def form_dict(name,stu_class,rollno,marks):

    if os.path.isfile(file_name):
        with open(file_name,"ab") as f:
            d['Name']=name
            d['Section']=stu_class
            d['RollNo']=rollno
            d['Marks']=marks
            pickle.dump(d,f)
    else:
        with open(file_name,"wb") as f:
            d['Name']=name
            d['Section']=stu_class
            d['RollNo']=rollno
            d['Marks']=marks
            pickle.dump(d,f)

#---------------------------------------------------------------

def combined_writing():

    global inc
    inc+=1
    info_area.tag_configure("no_of_stu",font=text_widg_font)
    info_area.delete("1.0",tk.END)
    info_area.insert("1.0",f"SUCCESSFULLY WROTE {inc} RECORD","no_of_stu")
    write_name()
    write_class()
    write_rno()
    write_marks()
    form_dict(name,stu_class,rollno,marks)

#END OF DATA ADDITION 


def read_file():
    data_area.delete("1.0",tk.END)
    data_area.tag_configure("text_tag",font=text_widg_font)
    data_area.insert("1.0","THE RECORDS OF THE FILE ARE : \n","text_tag")
    data_area.insert("2.0","\n")

    count_rec=0
    d={}
    if os.path.isfile(file_name):
        f=open(file_name,"rb")
    else:
        messagebox.showerror("NON EXISTANT FILE","THE FILE NAME YOU HAVE GIVEN DOES NOT EXIST")

    try:
        while True:
            try:
                d=pickle.load(f)
                count_rec+=1
                data_area.insert(tk.END,str(count_rec)+')'+ ' ' + str(d)+'\n',"text_tag")
   
            except EOFError:
                f.close()
                break
    except FileNotFoundError:
        print("The Data File Does Not Exist")


# THE SEARCH FUNCTIONALITY STARTS HERE
def search_window():

    search_win=tk.Toplevel(root)
    search_win.title("SEARCH RECORDS")
    search_win.geometry("500x300")

    search_title_label=tk.Label(search_win,text="CURRENTLY SEARCHING FOR A SPECIFIC STUDENT",font=search_custom_font).place(x=0,y=0)

    search_name_label=tk.Label(search_win,text="ENTER THE NAME OF THE STUDENT YOU WANT TO FIND",font=search_label_font).place(x=0,y=50)
    search_sec_label=tk.Label(search_win,text="ENTER THE CLASS OF THE STUDENT YOU WANT TO FIND",font=search_label_font).place(x=0,y=100)
    search_rno_label=tk.Label(search_win,text="ENTER THE ROLL NUMBER OF THE STUDENT YOU WANT TO FIND",font=search_label_font).place(x=0,y=150)

    global search_name_area
    search_name_area=tk.Entry(search_win,width=18)
    search_name_area.place(x=360,y=50)

    global search_sec_area
    search_sec_area=tk.Entry(search_win,width=18)
    search_sec_area.place(x=360,y=100)

    global search_rno_area
    search_rno_area=tk.Entry(search_win,width=18)
    search_rno_area.place(x=360,y=150)

    clear_button=tk.Button(search_win,text="CLEAR ALL",width=15,command=search_clear).place(x=358,y=240)

    submit_search_button=tk.Button(search_win,text="SUBMIT DETAILS",width=15,activebackground="green",activeforeground="black",command=search_file).place(x=358,y=190)

    search_win.mainloop()


def search_clear():

    search_name_area.delete(0,tk.END)
    search_rno_area.delete(0,tk.END)
    search_sec_area.delete(0,tk.END)


def search_file():

    search_dict={}
    found=False
    if os.path.isfile(file_name):
        f=open(file_name,"rb")
    else:
        messagebox.showerror("FILE ERROR","GIVEN FILE NAME DOES NOT EXIST")
    
    try:
        searched_name=search_name_area.get()
        if len(searched_name)>50:
            messagebox.showwarning("LENGTH WANRING","NAME ENTERED HAS EXCEEDED 50 CHARACTERS")

    except tk.TclError:
        messagebox.showwarning("VALUE ERROR","INVALID VALUE WAS ENTERED IN THE NAME WIDGET")

    try:
        searched_rno=int(search_rno_area.get())
        if int(searched_rno)<=0:
            messagebox.showwarning("NEGATIVE ROLLNO","NEGATIVE ROLL NUMBER FOUND")
            rno=None
        
    except tk.TclError:
        messagebox.showwarning("VALUE ERROR","INVALID VALUE WAS ENTERED IN THE ROLLNO WIDGET")
    
    try:
        searched_sec=search_sec_area.get()
        if searched_sec.isdigit():
            messagebox.showwarning("NUMBER FOUND","A NUMBER WAS ENTERED IN THE SEC WIDGET")
    except tk.TclError:
        messagebox.showwarning("VALUE ERROR","INVALID VALUE WAS ENTERED IN THE SEC WIDGET")

    try:
        while True:
            search_dict=pickle.load(f)
            if searched_rno==search_dict['RollNo'] and searched_sec==search_dict['Section'] and searched_name==search_dict['Name']:
                found=True
                if found==True:
                    messagebox.showinfo("SEARCH SUCCESSFUL","THE RECORD WILL BE DISPLAYED IN THE MAIN WINDOW")
                    data_area.delete("1.0",tk.END)
                    data_area.tag_configure("search_text_tag",font=search_display_font)
                    data_area.tag_configure("search_heading_tag",font=text_widg_font)
                    data_area.insert("1.0","THE RECORDS OF THE FILE ARE : \n","search_heading_tag")
                    data_area.insert("2.0","\n")
                    data_area.insert(tk.END,str(search_dict),"search_text_tag")
                
    except FileNotFoundError:
        print("The Data File Does Not Exist.")
    except EOFError :
        if found==False:
            messagebox.showinfo("RECORD NOT FOUND","THE RECROD YOU ARE LOOKING FOR DOES NOT EXIST")
        else:
            f.close()
            print()
#THE SEARCH FUNCTIONALITY ENDS HERE


# THE UPDATE FUNCTIONALITY STARTS HERE
def update_window():

    global updt_win
    updt_win=tk.Toplevel(root)
    updt_win.title("UPDATE RECORDS")
    updt_win.geometry("550x500")

    updt_bg_image=Image.open("C:\\Users\\shama\\OneDrive\\Pictures\\website-hosting-concept-with-circuits11.jpg")
    backscreen=ImageTk.PhotoImage(updt_bg_image)

    updt_bg_label=tk.Label(updt_win,image=backscreen)
    updt_bg_label.place(relwidth=1,relheight=1)

    updt_custom_font=font.Font(family="verdana",size=13,weight="bold")
    updt_label_font=font.Font(family="verdana",size=7,weight="bold")
    updt_record_heading_font=font.Font(family="verdana",size=11,weight="bold")

    global display_updated_area
    display_updated_area=tk.Text(updt_win,width=69,height=8)
    display_updated_area.place(x=0,y=298)
    display_updated_area.tag_configure("update_tag",font=updt_record_heading_font)
    display_updated_area.tag_configure("updt_write_tag",font=updt_label_font)
    display_updated_area.insert("1.0","THE UPDATED RECORD WILL BE DISPLAYED HERE  :\n","update_tag")
    display_updated_area.insert("2.0","\n")


    updt_title_label=tk.Label(updt_win,text="CURRENTLY UPDATING RECORD OF A SPECIFIC STUDENT",font=updt_custom_font,bg="black",fg="white").place(x=0,y=0)

    updt_name_label=tk.Label(updt_win,text="ENTER THE NAME OF THE STUDENT YOU WANT TO UPDATE",font=updt_label_font,bg="black",fg="white").place(x=0,y=50)
    updt_sec_label=tk.Label(updt_win,text="ENTER THE CLASS OF THE STUDENT YOU WANT TO UPDATE",font=updt_label_font,bg="black",fg="white").place(x=0,y=100)
    updt_rno_label=tk.Label(updt_win,text="ENTER THE ROLL NUMBER OF THE STUDENT YOU WANT TO UPDATE",font=updt_label_font,bg="black",fg="white").place(x=0,y=150)
    updt_marks_label=tk.Label(updt_win,text="ENTER THE AMOUNT OF MARKS TO BE INCREASED",font=updt_label_font,bg="black",fg="white").place(x=0,y=200)
    confirm_label=tk.Label(updt_win,text="DO YOU WANT TO UPDATE MORE RECORDS?",font=updt_label_font,bg="black",fg="white").place(x=0,y=457)

    confirm_button_yes=tk.Button(updt_win,text="YES",width=15,command=continue_updating_yes,bg="black",fg="white").place(x=250,y=452)
    confirm_button_no=tk.Button(updt_win,text="NO",width=15,command=continue_updating_no,bg="black",fg="white").place(x=400,y=452)

    global updt_name_area
    updt_name_area=tk.Entry(updt_win,width=18)
    updt_name_area.place(x=360,y=50)

    global updt_sec_area
    updt_sec_area=tk.Entry(updt_win,width=18)
    updt_sec_area.place(x=360,y=100)

    global updt_rno_area
    updt_rno_area=tk.Entry(updt_win,width=18)
    updt_rno_area.place(x=360,y=150)

    global updt_marks_area
    updt_marks_area=tk.Entry(updt_win,width=18)
    updt_marks_area.place(x=360,y=200)

    submit_update_button=tk.Button(updt_win,text="SUBMIT DETAILS",width=15,activebackground="green",activeforeground="black",command=update_file,bg="black",fg="white").place(x=358,y=245)


    updt_win.mainloop()


def update_file():

    updt_d={}
    found=False
    global UPDATE_COUNT_RECORD
    if os.path.isfile(file_name):
        f=open(file_name,"rb+")
    else:
        messagebox.showerror("FILE ERROR","GIVEN FILE NAME DOES NOT EXIST")
                
    try:
        update_amt=int(updt_marks_area.get())
        if update_amt<0:
            messagebox.showwarning("NEGATICE NUMBER","A NEGATIVE NUMBER HAS BEEN ENTERED IN MARKS WIDGET")

    except ValueError:
        messagebox.showerror("VALUE ERROR","INVALID VALUE HAS BEEN ENTERED IN THE MARKS WIDGET")

        
    try:
        while True:
            pos=f.tell()
            updt_d=pickle.load(f)
            if updt_d['Name']==updt_name_area.get() and updt_d['Section']==updt_sec_area.get() and updt_d['RollNo']==int(updt_rno_area.get()):
                updt_d['Marks']+=update_amt
                f.seek(pos)
                pickle.dump(updt_d,f)
                display_updated_area.insert(tk.END,str(UPDATE_COUNT_RECORD)+')'+str(updt_d)+'\n',"updt_write_tag")
                UPDATE_COUNT_RECORD+=1
                found=True

    except NameError:
        messagebox.showwarning("VALUE ERROR","THE UPDATE AMOUNT HAS NOT BEEN ASSIGNED")

    except FileNotFoundError:
        print("The Data File Does Not Exist.")

    except EOFError:
        if found==False:
            messagebox.showinfo("UPDATION MESSAGE","REQUIRED RECORD WAS NOT FOUND")
            f.close()
        else:
            if UPDATE_COUNT_RECORD==2:
                messagebox.showinfo("UPDATION NOTICE",f"SUCCESSFULLY UPDATED {UPDATE_COUNT_RECORD-1} RECORD IN TOTAL")
            else:
                messagebox.showinfo("UPDATION NOTICE",f"SUCCESSFULLY UPDATED {UPDATE_COUNT_RECORD-1} RECORDS IN TOTAL")

    f.close()
    

def continue_updating_yes():

    updt_name_area.delete(0,tk.END)
    updt_rno_area.delete(0,tk.END)
    updt_sec_area.delete(0,tk.END)
    updt_marks_area.delete(0,tk.END)


def continue_updating_no():

    updt_win.destroy()
# THE UPDATE FUNCTIONALITY ENDS HERE


# DATA DELETION FUNCTIONALITY BEGINS HERE
def delete_last_record():

    with open(file_name,"rb") as f_check:

        read_all=f_check.readlines()
        if not read_all:
            messagebox.showinfo("DATA MESSAGE","THE OPENED FILE IS EMPTY")

        else:
            del_q=messagebox.askquestion("DELETE RECORD","ARE YOU SURE YOU WANT TO DELETE THE LAST RECORD?")
            if del_q=="yes":

                temp_lst=[]
                data_area.delete("1.0",tk.END)
                with open(file_name,"rb") as f:
                    while True:
                        try:
                            while True:
                                ch=pickle.load(f)
                                temp_lst.append(ch)
                        except EOFError:
                            break

                temp_lst.pop()

                with open(file_name,"wb") as f:
                    for i in temp_lst:
                        pickle.dump(i,f)

                read_file()
            
            else:
                pass


def delete_data():
    
    ch=messagebox.askquestion("DELETION QUESTION","DO YOU WANT TO TRUNCATE EVERYTHING?")
    if ch=='yes':
        data_area.delete("1.0",tk.END)
        if os.path.isfile(file_name):
            with open(file_name,"wb") as f_delete:
                deleted_data()
 
        else:
            messagebox.showinfo("IMPORTANT MESSAGE","The file does not exist (or) The path of the file does not exist.")

    else:
        pass


def deleted_data():
    messagebox.showinfo("Message","ALL THE DATA HAS BEEN DELETED!")



def quit_file():
    root.destroy()
# DATA DELETEION FUCNTIONALITY ENDS HERE


# CUSTOM FONT FOR HEADING
custom_font=font.Font(family="verdana",size=14,weight="bold")

# CUSTOM FONT FOR DISPLAYING DATA IN THE TEXT WIDGET
text_widg_font=font.Font(family="verdana",size=10,weight="bold")

# CUSTOM FONT FOR SEARCH WINDOW
search_custom_font=font.Font(family="verdana",size=13,weight="bold")
search_label_font=font.Font(family="verdana",size=7,weight="bold")
search_display_font=font.Font(family="verdana",size=10,weight="bold")

#HEADING
func_label=tk.Label(root,text="FUNCTIONS OF PROGRAM",font=custom_font,bg="black",fg="white").place(x=10,y=0)
above_data_area_label=tk.Label(root,text="THE RECORD DETAILS WILL BE DISPLAYED HERE",font=custom_font,bg="black",fg="white").place(x=414,y=0)

#LABEL FONTS
label_font=font.Font(family="verdana",size=7,weight="bold")

# DISPLAYS TEXT GIVING THE FUNCTIONS OF EACH BUTTON
write_label=tk.Label(root,text="1) WRITE DATA ONTO FILE IN BINARY FORM",bg="black",fg="white",font=label_font).place(x=10,y=60)
read_label=tk.Label(root,text="2) READ DATA FROM THE GIEVN FILE",bg="black",fg="white",font=label_font).place(x=10,y=110)
search_label=tk.Label(root,text="3) SEARCH FOR A SPECIFIC RECORD",bg="black",fg="white",font=label_font).place(x=10,y=160)
update_label=tk.Label(root,text="4) UPDATE A SPECIFIC RECORD OF THE FILE",bg="black",fg="white",font=label_font).place(x=10,y=210)
delete_label=tk.Label(root,text="5) DELETE ALL THE DATA FROM THE FILE",bg="black",fg="white",font=label_font).place(x=10,y=260)
del_last_label=tk.Label(root,text="6) DELETE ONLY THE LAST/PREVIOUS RECORD",bg="black",fg="white",font=label_font).place(x=10,y=310)
quit_label=tk.Label(root,text="7) QUIT THE PROGRAM",bg="black",fg="white",font=label_font).place(x=10,y=360)

# THE BUTTONS OF ALL THE FUNCTIONS
w_button=tk.Button(root,text="WRITE DATA",width=11,command=write_window,bg="black",fg="white").place(x=300,y=57)
r_button=tk.Button(root,text="READ DATA",width=11, command=read_file,bg="black",fg="white").place(x=300,y=107)
srch_button=tk.Button(root,text="SEARCH DATA",width=11, command=search_window,bg="black",fg="white").place(x=300,y=157)
updt_button=tk.Button(root,text="UPDATE DATA",width=11,command=update_window,bg="black",fg="white").place(x=300,y=207)
del_button=tk.Button(root, text="CLEAR DATA",width=11,activeforeground="black",activebackground="red",command=delete_data,bg="black",fg="white").place(x=300,y=257)
del_last_button=tk.Button(root,text="DEL PREV",width=11,bg="black",fg="white",command=delete_last_record).place(x=300,y=307)
quit_button=tk.Button(root,text="QUIT",width=11,command=quit_file,bg="black",fg="white").place(x=300,y=357)


root.mainloop()