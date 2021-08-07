from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr
import pymysql

class Complaint:
    def __init__(self,root):
        self.root = root
        self.root.title('Complaint Management System')
        self.root.geometry('1160x820+0+0')
        #self.root.pack(fill = 'both',expand = True)
        notebook = ttk.Notebook(self.root)
        self.TabControl1 = ttk.Frame(notebook)
        self.TabControl2 = ttk.Frame(notebook)
        self.TabControl3 = ttk.Frame(notebook)
        notebook.add(self.TabControl1,text = 'Entry Form')
        notebook.add(self.TabControl2,text = 'Complaint Data')

        notebook.grid()

        #++++++++++++++++++++++++++++++++++++++++++++++++++Variables Declaration++++++++++++++++++++++++++++++++++
        Name = StringVar()
        Gender = StringVar()
        pincode = StringVar()
        Address = StringVar()
        City = StringVar()
        District = StringVar()
        commentbox = StringVar()

        #++++++++++++++++++++++++++++++++++++++++++++++++CheckBox delcalraion+++++++++++++++++++++++++++++++++++++
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()

        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()

        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()

        #++++++++++++++++++++++++++++++++++++++++++++++++++add data into databasel+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        def addData():
            datacheck = check()
            if Name.get() == '' or Address.get() == '' or City.get() == "" or len(datacheck) == 0:
                tkinter.messagebox.showerror("Enter correct member details !")
            else:
                sqlCon = pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'test1')
                cur = sqlCon.cursor()
                cur.execute("insert into test values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                Name.get(),
                Gender.get(),
                pincode.get(),
                Address.get(),
                City.get(),
                District.get(),
                datacheck,
                commentbox.get("1.0",END),
                ))
                sqlCon.commit()
                DisplayData()
                sqlCon.close()
                tkinter.messagebox.showinfo('Data Entry From','Record Entered Successfully!')


        def DisplayData():
            sqlCon = pymysql.connect(host = "localhost",user = 'root',password = '',database = "test1")
            cur = sqlCon.cursor()
            cur.execute("Select * from test")
            result = cur.fetchall()
            if len(result) != 0:
                self.complaintdatarecords.delete(*self.complaintdatarecords.get_children())
                for row in result:
                    self.complaintdatarecords.insert('',END,values = row)
                sqlCon.commit()
            sqlCon.close()

        def Reset():
            Name.set('')
            Gender.set('')
            pincode.set('')
            Address.set('')
            City.set('')
            District.set('')
            commentbox.set('')


        def Submit(ev):
            viewdata = self.complaintdatarecords.focus()
            learnData = self.complaintdatarecords.item(viewdata)
            row = learnData['values']

            Name.set(row[0])
            Gender.set(row[1])
            pincode.set(row[2])
            Address.set(row[3])
            City.set(row[4])
            District.set(row[5])
            #commentbox.set(row[6])
            addData()


        def check():
            l = []
            if var1.get() == 1:
                l.append('Tansport')
            if var2.get() == 1:
                l.append('Water')
            if var3.get() == 1:
                l.append('Electricity')
            if var4.get() == 1:
                l.append('Road')
            if var5.get() == 1:
                l.append('Service')
            if var6.get() == 1:
                l.append('Hospitals')
            if var7.get() == 1:
                l.append('Tax')
            if var8.get() == 1:
                l.append('Communication')
            if var9.get() == 1:
                l.append('Education')
            if var10.get() == 1:
                l.append('Drainage')
            if var11.get() == 1:
                l.append('Gas issue')
            if var12.get() == 1:
                l.append('Other')
            length = len(l)
            s = ''
            for i in range(0,len(l)):
                if(i == length-1):
                    s += l[i]
                else:
                    s += l[i]
                    s += ','

            l = []
            l.append(s)
            return l



        #=================================================Frame================================================================================

        MainFrame = Frame(self.TabControl1,bd =10,width = 1230,height = 800,relief = RIDGE)
        MainFrame.grid()
        Tab2Frame = Frame(self.TabControl2,bd =10,width = 1230,height = 800,relief = RIDGE)
        Tab2Frame.grid()
        Tab3Frame = Frame(self.TabControl3,bd =10,width = 1230,height = 700,relief = RIDGE)
        Tab3Frame.grid()

        TopFrame1 = Frame(MainFrame,bd = 10,height = 100,relief = RIDGE)
        TopFrame1.grid()
        TopFrame2 = Frame(MainFrame,bd = 10,width = 1220,height = 100,relief = RIDGE)
        TopFrame2.grid()
        TopFrame3 = Frame(MainFrame,bd = 10,width = 1220,height = 100,relief = RIDGE)
        TopFrame3.grid()

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        UpperFrame = Frame(TopFrame2,bd = 5, width = 1210,height = 400,padx = 2,bg = 'cadetblue',relief = RIDGE)
        UpperFrame.grid()
        LowerFrame = Frame(TopFrame2,bd = 5,width = 1210,height = 800,padx = 2,relief = RIDGE)
        LowerFrame.grid()
        left_box = Frame(LowerFrame,bd = 5,width = 400,height = 200,padx = 2,bg = 'cadetblue',relief = RIDGE)
        left_box.pack(side = LEFT)
        right_box = Frame(LowerFrame,bd = 5,width = 960,height = 200,padx = 2,bg = 'cadetblue',relief = RIDGE)
        right_box.pack(side = RIGHT)
        lower_chat_box = Frame(TopFrame3,bd = 5,width =1200,height = 330,padx = 2,relief = RIDGE,bg = 'red')
        lower_chat_box.pack()





        #++++++++++++++++++++++++++++++++++++++++++Title Name+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.lb1Title = Label(TopFrame1,font = ('arial',10,'bold'),text = 'Complaint Management System',justify = CENTER)
        self.lb1Title.grid(padx = 450)

        self.lb1UserName = Label(UpperFrame,font = ('arial',12,'bold'),text = 'User Name ',bd = 10,width = 10)
        self.lb1UserName.grid(row = 0,column = 0,sticky = W)
        self.txtUserName = Entry(UpperFrame,font = ('arial',12,'bold'),bd = 5,width = 50 ,textvariable = Name)
        self.txtUserName.grid(row = 0,column = 1)
        self.lb1Gender = Label(UpperFrame,font = ('arial',12,'bold'),text = 'Gender ',bd = 10)
        self.lb1Gender.grid(row =0,column = 2,sticky = W)
        self.cboGender = ttk.Combobox(UpperFrame,textvariable = Gender,state = 'readonly',font = ('arial',14,'bold'),width = 15)
        self.cboGender['value'] = ('','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row =0,column = 3)
        self.pincodena = Label(UpperFrame,font = ('arial',12,'bold'),text = 'Pincode',bd = 10,width = 6)
        self.pincodena.grid(row = 0,column = 4,sticky = W)
        self.pincodetext = Entry(UpperFrame,font = ('arial',12,'bold'),bd = 5,width = 15,textvariable = pincode)
        self.pincodetext.grid(row = 0,column = 5)
        self.Address_user = Label(UpperFrame,font = ('arial',12,'bold'),text = 'Address ',width = 10,bd = 10)
        self.Address_user.grid(row = 1,column = 0,sticky = W)
        self.Address_us = Entry(UpperFrame,font = ('arial',12,'bold'),bd = 5,width = 50,textvariable = Address)
        self.Address_us.grid(row = 1,column = 1)
        self.getCity = Label(UpperFrame,font = ('arial',12,'bold'),bd = 10,text = 'City',width = 6)
        self.getCity.grid(row = 1,column = 2)
        self.txtCity = Entry(UpperFrame,font = ('arial',12,'bold'),bd = 5,textvariable = City,width = 20)
        self.txtCity.grid(row = 1,column = 3)
        self.getDistrict = Label(UpperFrame,font = ('arial',12,'bold'),bd = 10,text = 'District',width = 6)
        self.getDistrict.grid(row = 1,column = 4)
        self.txtDistrict = Entry(UpperFrame,font = ('arial',12,'bold'),bd = 5,textvariable = District,width = 15)
        self.txtDistrict.grid(row = 1,column = 5)


        #+++++++++++++++++++++++++++++++++++++++++CheckBox Frame++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        self.Complain_msg = Label(left_box,font = ('arial',15,'bold'),bd = 10,text = ' \n\nWhich Juvenile Justice Service\n were you using at the\n time of complaint?\n\n')
        self.Complain_msg.pack()

        #Checkbox Label
        self.checkinfo = Label(right_box,font = ('arial',10,'bold'),text = '(Tick appropiate boxes following of them).',bg = 'cadetblue')
        self.checkinfo.grid(row = 0,column = 0,sticky = W)

        #row1
        self.ckTransport = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0,width = 23, variable = var1 ,text = 'Transport')
        self.ckTransport.grid(row = 1,column = 0,padx = 10,pady = 10)
        self.ckWater = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0, variable = var2 ,text = 'Water')
        self.ckWater.grid(row = 1,column = 1)
        self.ckElectricity = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0, variable = var3 ,text = 'Electricity')
        self.ckElectricity.grid(row = 1,column = 2)
        self.ckRoad = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0, variable = var4 ,text = 'Road')
        self.ckRoad.grid(row = 1,column = 3)

        #row2
        self.ckservice = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0, variable = var5 ,text = 'Service')
        self.ckservice.grid(row = 2,column = 0,padx = 10,pady = 10)
        self.ckHospitals = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0, variable = var6 ,text = 'Hospitals')
        self.ckHospitals.grid(row = 2,column = 1)
        self.ckTax = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0, variable = var7 ,text = 'Tax')
        self.ckTax.grid(row = 2,column = 2)
        self.ckcommu = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0, variable = var8 ,text = 'Communication')
        self.ckcommu.grid(row = 2,column = 3)

        #row3
        self.ckEducation = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue' ,padx = 0,pady = 0, variable = var9 ,text = 'Education')
        self.ckEducation.grid(row = 3,column = 0,padx = 10,pady = 10)
        self.ckDrainage = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0, variable = var10 ,text = 'Drainage')
        self.ckDrainage.grid(row = 3,column = 1)
        self.ckgas = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0, variable = var11 ,text = 'Gas issue')
        self.ckgas.grid(row = 3,column = 2)
        self.ckOther = Checkbutton(right_box,font = ('arial',15,'bold'),bg = 'cadetblue',padx = 0,pady = 0, variable = var12 ,text = 'Other')
        self.ckOther.grid(row = 3,column = 3)




        #+++++++++++++++++++++++++++++++++++++++++chat Box++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.chatcomment = Label(lower_chat_box,bd = 10,font =  ('arial',15,'bold'),text = 'Note/Comment/Suggestion :-\t\t\t\t\t\t\t',justify = LEFT,bg = 'red')
        self.chatcomment.grid(row = 0,column = 0)
        self.lb1Note = Text(lower_chat_box,bd = 10,font = ('arial',12,'bold'),width = 120,height = 14,relief = RIDGE)
        self.lb1Note.grid(row=1,
               column=0)
        commentbox = self.lb1Note

        #my_label = Label(lower_chat_box,textvariable = commentbox)
        """self.txtchat = Text(chatframe,width = 100,font = ('arial',12,'bold'))
        self.txtchat.grid()"""
        #self.j = Label(lower_chat_box,bd = 2,font = ('arial',15,'bold'),width = 1)
        #self.j.grid(row =2,column = 0)
        self.Submit = Button(lower_chat_box,bd = 2,font =('arial',15,'bold'),text = 'Submit',width = 10,command = addData).grid(row = 2,column = 0)




        #**************************************complaint data records***********************************************************************
        TopFrame11 = Frame(Tab2Frame,bd = 10,width = 1200,height = 100,relief = RIDGE)
        TopFrame11.grid(row = 0,column = 0)
        TopFrame12 = Frame(Tab2Frame,bd = 10,width = 1220,height = 650,relief = RIDGE)
        TopFrame12.grid(row = 1,column = 0)

        self.lblTitle = Label(TopFrame11,font=('arial',40,'bold'),text = 'Complaint Management System',bd = 10,justify = CENTER)
        self.lblTitle.grid(padx = 72)
        Scroll_x = Scrollbar(TopFrame12,orient = HORIZONTAL)
        Scroll_y = Scrollbar(TopFrame12,orient = VERTICAL)
        self.complaintdatarecords = ttk.Treeview(TopFrame12, height = 22,columns = ('Name','Gender','pincode','Address','City','District','Complaint_type','commentbox'),xscrollcommand = Scroll_x.set,yscrollcommand = Scroll_y.set)

        Scroll_x.pack(side = BOTTOM,fill = X)
        Scroll_y.pack(side = RIGHT,fill = Y)

        self.complaintdatarecords.heading('Name',text = 'Name')
        self.complaintdatarecords.heading('Gender',text = 'Gender')
        self.complaintdatarecords.heading('pincode',text = 'pincode')
        self.complaintdatarecords.heading('Address',text = 'Address')
        self.complaintdatarecords.heading('City',text = 'City')
        self.complaintdatarecords.heading('District',text = 'District')
        self.complaintdatarecords.heading('Complaint_type',text ='Complaint type')
        self.complaintdatarecords.heading('commentbox',text = 'commentbox')

        self.complaintdatarecords['show'] = 'headings'
        self.complaintdatarecords.column('Name',width = 100)
        self.complaintdatarecords.column('Gender',width = 100)
        self.complaintdatarecords.column('pincode',width = 100)
        self.complaintdatarecords.column('Address',width = 100)
        self.complaintdatarecords.column('City',width = 100)
        self.complaintdatarecords.column('District',width = 100)
        self.complaintdatarecords.column('Complaint_type',width = 150)
        self.complaintdatarecords.column('commentbox',width = 450)

        self.complaintdatarecords.pack(fill = BOTH,expand = 1)
        self.complaintdatarecords.bind('<ButtonRelease-1>',Submit)
        DisplayData()









if __name__ == '__main__':
    root = Tk()
    application = Complaint(root)
    root.mainloop()
