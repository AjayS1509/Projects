from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql


class connectorDB:

    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(102*titlespace + "Mysql Connector")
        self.root.geometry("776x700+300+0")
        self.root.resizable(width = False, height = False)

        MainFrame = Frame(self.root,bd = 10,width = 770,height = 700,relief = RIDGE,bg = 'cadetblue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,bd = 7,width = 770,height = 100,relief = RIDGE)
        TitleFrame.grid(row = 0,column = 0)
        TopFrame3 = Frame(MainFrame,bd = 5,width = 770,height = 500,relief = RIDGE)
        TopFrame3.grid(row = 1,column = 0)

        LeftFrame = Frame(TopFrame3,bd = 5,width = 770,height = 400,padx = 2,bg = 'cadetblue',relief = RIDGE)
        LeftFrame.pack(side = LEFT)
        LeftFrame1 = Frame(LeftFrame,bd = 5,width = 600,height = 180,padx = 12,pady = 9,relief = RIDGE)
        LeftFrame1.pack(side = TOP)

        RightFrame = Frame(TopFrame3,bd = 5,width = 100,height = 400,padx = 2,bg = 'cadetblue',relief = RIDGE)
        RightFrame.pack(side = RIGHT)
        RightFrame1 = Frame(RightFrame,bd = 5,width = 90,height = 300,padx = 2,pady = 2,relief = RIDGE)
        RightFrame1.pack(side = TOP)
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        StudentID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Gender = StringVar()
        Mobile = StringVar()

        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        def iExit():
            iExit = tkinter.messagebox.askyesno("Mysql Connection","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.EnterStudentId.delete(0,END)
            self.EnterFirstName.delete(0,END)
            self.EnterLastName.delete(0,END)
            self.EnterAddress.delete(0,END)
            Gender.set("")
            self.EnterMobile.delete(0,END)

        def addData():
            if StudentID.get() == "" or Firstname.get() == "" or Surname.get() == "":
                tkinter.messagebox.showerror("Mysql Connection","Enter correct Details !")
            else:
                sqlCon = pymysql.connect(host = "localhost",user = "root",password = "Ajay@15",database = "student_data")
                cur = sqlCon.cursor()
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s)",(
                StudentID.get(),
                Firstname.get(),
                Surname.get(),
                Address.get(),
                Gender.get(),
                Mobile.get(),
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Mysql Connection","Record Entered Successfully")

        def DisplayData():
            sqlCon = pymysql.connect(host = "localhost",user = "root",password = "Ajay@15",database = "student_data")
            cur = sqlCon.cursor()
            cur.execute("select * from student ")
            result = cur.fetchall()
            if len(result) != 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('',END,values = row)
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Entered Sucessfully")




        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.lblTitle = Label(TitleFrame,font = ('arial',40,'bold'),text = "Mysql Connection",bd = 7)
        self.lblTitle.grid(row = 0,column = 0,padx = 132)

        self.lblStudentID = Label(LeftFrame1,font =('arial',12,'bold'),text = "Student ID",bd = 7)
        self.lblStudentID.grid(row = 1,column = 0,sticky = W,padx = 5)
        self.EnterStudentId = Entry(LeftFrame1,font = ('arial',12,'bold'),bd = 5,width = 44,justify = 'left',textvariable = StudentID)
        self.EnterStudentId.grid(row = 1,column = 1,sticky = W,padx = 5)
        self.lblFirstName = Label(LeftFrame1,font =('arial',12,'bold'),text = "First Name",bd = 7)
        self.lblFirstName.grid(row = 2,column = 0,sticky = W,padx = 5)
        self.EnterFirstName = Entry(LeftFrame1,font = ('arial',12,'bold'),bd = 5,width = 44,justify = 'left',textvariable = Firstname)
        self.EnterFirstName.grid(row = 2,column = 1,sticky = W,padx = 5)
        self.lblLastName = Label(LeftFrame1,font =('arial',12,'bold'),text = "Last Name",bd = 7)
        self.lblLastName.grid(row = 3,column = 0,sticky = W,padx = 5)
        self.EnterLastName = Entry(LeftFrame1,font = ('arial',12,'bold'),bd = 5,width = 44,justify = 'left',textvariable = Surname)
        self.EnterLastName.grid(row = 3,column = 1,sticky = W,padx = 5)
        self.lblAddress = Label(LeftFrame1,font =('arial',12,'bold'),text = "Address",bd = 7)
        self.lblAddress.grid(row = 4,column = 0,sticky = W,padx = 5)
        self.EnterAddress = Entry(LeftFrame1,font = ('arial',12,'bold'),bd = 5,width = 44,justify = 'left',textvariable = Address)
        self.EnterAddress.grid(row = 4,column = 1,sticky = W,padx = 5)
        self.lblGender = Label(LeftFrame1,font =('arial',12,'bold'),text = "Gender",bd = 7)
        self.lblGender.grid(row = 5,column = 0,sticky = W,padx = 5)
        self.cboGender = ttk.Combobox(LeftFrame1,font = ('arial',12,'bold'),width = 42,state = 'readonly',textvariable = Gender)
        self.cboGender['values'] = (' ','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row = 5,column = 1)
        self.lblMobile = Label(LeftFrame1,font =('arial',12,'bold'),text = "Mobile ",bd = 7)
        self.lblMobile.grid(row = 6,column = 0,sticky = W,padx = 5)
        self.EnterMobile = Entry(LeftFrame1,font = ('arial',12,'bold'),bd = 5,width = 44,justify = 'left',textvariable = Mobile)
        self.EnterMobile.grid(row = 6,column = 1,sticky = W,padx = 5)


        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        scroll_y = Scrollbar(LeftFrame,orient = VERTICAL)

        self.student_records = ttk.Treeview(LeftFrame,height = 14,columns = ('stdid','firstname','surname','address','gender','mobile'),yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)

        self.student_records.heading('stdid',text = 'StudentID')
        self.student_records.heading('firstname',text = 'Firstname')
        self.student_records.heading('surname',text = 'Surname')
        self.student_records.heading('address',text = 'Address')
        self.student_records.heading('gender',text = 'Gender')
        self.student_records.heading('mobile',text = 'Mobile')

        self.student_records['show'] = 'headings'

        self.student_records.column('stdid',width = 70)
        self.student_records.column('firstname',width = 100)
        self.student_records.column('surname',width = 100)
        self.student_records.column('address',width = 100)
        self.student_records.column('gender',width = 70)
        self.student_records.column('mobile',width = 70)

        self.student_records.pack(fill = BOTH,expand = 1)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.btnAddNew = Button(RightFrame1,font = ('arial',16,'bold'),text = 'Add New',bd = 4,pady = 1,padx = 24,width = 8,height = 2,command = addData).grid(row = 0,column = 0,padx = 1)
        self.btnDisplay = Button(RightFrame1,font = ('arial',16,'bold'),text = 'Display',bd = 4,pady = 1,padx = 24,width = 8,height = 2,command = DisplayData).grid(row = 1,column = 0,padx = 1)
        self.btnUpdate = Button(RightFrame1,font = ('arial',16,'bold'),text = 'Update',bd = 4,pady = 1,padx = 24,width = 8,height = 2).grid(row = 2,column = 0,padx = 1)
        self.btnDelete = Button(RightFrame1,font = ('arial',16,'bold'),text = 'Delete',bd = 4,pady = 1,padx = 24,width = 8,height = 2).grid(row = 3,column = 0,padx = 1)
        self.btnSearch = Button(RightFrame1,font = ('arial',16,'bold'),text = 'Search',bd = 4,pady = 1,padx = 24,width = 8,height = 2).grid(row = 4,column = 0,padx = 1)
        self.btnReset = Button(RightFrame1,font = ('arial',16,'bold'),text = 'Reset',bd = 4,pady = 1,padx = 24,width = 8,height = 2,command = Reset).grid(row = 5,column = 0,padx = 1)
        self.btnExit = Button(RightFrame1,font = ('arial',16,'bold'),text = 'Exit',bd = 4,pady = 1,padx = 24,width = 8,height = 2,command = iExit).grid(row = 6,column = 0,padx = 1)





if __name__ == '__main__':
    root = Tk()
    application = connectorDB(root)
    root.mainloop()
