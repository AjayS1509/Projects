from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.resizable(width = False,height = False)
root.geometry("400x492+460+40")

MainFrame = Frame(root,pady = 2,relief = RIDGE)
MainFrame.grid()
calFrame = Frame(MainFrame,bd = 20,pady = 2,relief = RIDGE)
calFrame.grid()

#************************************************************************************************************************************************************************************
class Calc():
    def __init__(self):
        self.total = 0
        self.current  = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def Enternumber(self, num):
        self.result = False
        firstnum = textResult.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.Display(self.current)
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.validFunction()
        else:
            self.total = float(textResult.get())

    def Display(self,value):
        textResult.delete(0,END)
        textResult.insert(0,value)

    def validFunction(self):
        if self.op == 'add':
            self.total += self.current
        if self.op == 'sub':
            self.total -= self.current
        if self.op == 'mult':
            self.total *= self.current
        if self.op == 'divide':
            self.total /= self.current
        if self.op == 'mod':
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.Display(self.total)

    def operation(self,op):
        self.current = float(self.current)
        if(self.check_sum):
            self.validFunction()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum  = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = '0'
        self.Display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry
        self.total = 0

    def mathsPM(self):
        self.result = False
        self.current = -(float(textResult.get()))
        self.Display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(textResult.get())))
        self.Display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(flaot(textResult.get())))
        self.Display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(textResult.get())))
        self.Display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(textResult.get())))
        self.Display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(textResult.get())))
        self.Display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(textResult.get())))
        self.Display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(math.radians(float(textResult.get())))
        self.Display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(math.radians(float(textResult.get())))
        self.Display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.Display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.Display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.Display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(textResult.get()))
        self.Display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(textResult.get()))
        self.Display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(textResult.get()))
        self.Display(self.current)

    def lagmma(self):
        self.result = False
        self.current = math.lagmma(float(textResult.get()))
        self.Display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degress(float(textResult.get()))
        self.Display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(textResult.get()))
        self.Display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(textResult.get()))
        self.Display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(textResult.get()))
        self.Display(self.current)

    def backspace(self):
        numLen = len(textResult.get())
        textResult.delete(numLen -1,'end')
        if numLen == 1:
            textResult.insert(0,"0")


#************************************************************************************************************************************************************************************

added_values = Calc()

textResult = Entry(calFrame,font = ('arial',16,'bold'),bg = 'cadetblue',bd = 30,width = 26,justify = RIGHT)
textResult.grid(row = 0,column = 0,columnspan = 4,pady = 1)
textResult.insert(0,"0")
#************************************************************************************************************************************************************************************
numericButton = '789456123'
i = 0
btn = []
for j in range(2,5):
    for q in range(3):
        btn.append(Button(calFrame,width = 6,height =2,font = ('arial',16,'bold'),bd = 4,text = numericButton[i]))
        btn[i].grid(row = j,column = q,pady = 1)
        btn[i]['command'] = lambda x = numericButton [i]: added_values.Enternumber(x)
        i+=1
#************************************************************************************************************************************************************************************
btn0 = Button(calFrame,text = '0',width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = lambda:added_values.Enternumber(0)).grid(row = 5,column = 0,pady = 1)
btnDiv = Button(calFrame,text = chr(247),width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = lambda: added_values.operation('divide')).grid(row = 5,column = 3,pady = 1)
btnMult = Button(calFrame,text = chr(42),width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = lambda: added_values.operation('mult')).grid(row = 4,column = 3,pady = 1)
btnSub = Button(calFrame,text = chr(45),width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = lambda: added_values.operation('sub')).grid(row = 3,column = 3,pady = 1)
btnDot = Button(calFrame,text = chr(183),width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = lambda: added_values.Enternumber('.')).grid(row = 5,column = 1,pady = 1)
btnAdd = Button(calFrame,text = chr(43),width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = lambda: added_values.operation('add')).grid(row = 2,column = 3,pady = 1)
btnPM = Button(calFrame,text = chr(177),width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.mathsPM).grid(row = 1,column = 3,pady = 1)
btnBackSpace = Button(calFrame,width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,text = '←',bg = 'cadetblue',command = added_values.backspace).grid(row = 1,column = 0,pady = 1)
btnClearEntry = Button(calFrame,text = chr(67)+chr(69),width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.Clear_Entry).grid(row = 1,column = 1,pady = 1)
btnClear = Button(calFrame,text = chr(67),width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.all_Clear_Entry).grid(row = 1,column = 2,pady = 1)
btnequals = Button(calFrame,text = chr(61),width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.sum_of_total).grid(row = 5,column = 2,pady = 1)


#************************************************************************************************************************************************************************************
btnsin = Button(calFrame,text = "sin",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.sin).grid(row = 1,column = 4,padx = 5,pady = 1)
btntan = Button(calFrame,text = "tan",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.tan).grid(row = 1,column = 5,padx = 5,pady = 1)
btncos = Button(calFrame,text = "cos",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.cos).grid(row = 1,column = 6,padx = 5,pady = 1)
btnpi = Button(calFrame,text = "π",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.pi).grid(row = 1,column = 7, padx = 5,pady = 1)

#************************************************************************************************************************************************************************************
btnsinh = Button(calFrame,text = "sinh",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,command = added_values.sinh).grid(row = 2,column = 4,padx = 5,pady = 1)
btntanh = Button(calFrame,text = "tanh",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,command = added_values.tanh).grid(row = 2,column = 5,padx = 5,pady = 1)
btncosh = Button(calFrame,text = "cosh",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,command = added_values.cosh).grid(row = 2,column = 6,padx = 5,pady = 1)
btn2pi = Button(calFrame,text = "2π",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.tau).grid(row = 2,column = 7,padx = 5,pady = 1)

#************************************************************************************************************************************************************************************
btnE = Button(calFrame,text = "e",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,command = added_values.e).grid(row = 3,column = 4,padx = 5,pady = 1)
btnMod = Button(calFrame,text = "mod",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,command = lambda: added_values.operation('mod')).grid(row = 3,column = 5,padx = 5,pady = 1)
btnExp = Button(calFrame,text = "exp",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,command = added_values.exp).grid(row = 3,column = 6,padx = 5,pady = 1)
btnlog = Button(calFrame,text = "log",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.log).grid(row = 3,column = 7,padx = 5,pady = 1)

#************************************************************************************************************************************************************************************
btnasinh = Button(calFrame,text = "asinh",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,command = added_values.asinh).grid(row = 4,column = 4,padx = 5,pady = 1)
btnacosh = Button(calFrame,text = "acosh",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,command = added_values.acosh).grid(row = 4,column = 5,padx = 5,pady = 1)
btndeg = Button(calFrame,text = "deg",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,command = added_values.degrees).grid(row = 4,column = 6,padx = 5,pady = 1)
btnlog2 = Button(calFrame,text = "log2",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,command = added_values.log2).grid(row = 4,column = 7,padx = 5,pady = 1)

#************************************************************************************************************************************************************************************
btnlgamma = Button(calFrame,text = "mod",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.lagmma).grid(row = 5,column = 4,pady = 1)
btnexp1 = Button(calFrame,text = "expm1",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.expm1).grid(row = 5,column = 5,pady = 1)
btnlog1p = Button(calFrame,text = "log1p",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.log1p).grid(row = 5,column = 6,pady = 1)
btnlog10 = Button(calFrame,text = "log10",width = 6,height = 2,font = ('arial',16,'bold'),bd = 4,bg = 'cadetblue',command = added_values.log10).grid(row = 5,column = 7,pady = 1)

#************************************************************************************************************************************************************************************

def iExit():
    iExit = tkinter.messagebox.askyesno("scintific Calculator","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return
def Scientific():
    root.geometry("800x492+260+40")
    root.resizable(width = False,height = False)
    textResult.delete(0,END)
    textResult.delete(0,"0")
    #lblDisplay = Label(calFrame,text = 'Dynamic Hunter',font = ('C39HrP24DhTt',60),padx = 9,fg = 'cadetblue',justify = CENTER)
    lblDisplay = Label(calFrame,text = "Scientific",font = ('forte',25,'bold'),bg = 'red')
    lblDisplay.grid(row = 0,column = 4,columnspan = 4)
    #lblDisplay.grid(row = 0,column = 4,columnspan = 4)

def Standard():
    root.geometry("400x492+460+40")
    root.resizable(width = False,height = False)
    textResult.delete(0,END)
    textResult.delete(0,"0")


menubar = Menu(calFrame)

filemenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'File',menu = filemenu)
filemenu.add_command(label = "Standard",command = Standard)
filemenu.add_separator()
filemenu.add_command(label = "Scientific",command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit",command = iExit)


root.config(menu = menubar)
root.mainloop()
