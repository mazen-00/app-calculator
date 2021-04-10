from tkinter import * # Import a library (tkinter)
'--------------------------------'

window = Tk() # Create an object for window
window.title('Calculator') # window title
window.geometry('400x424+450+100') # edit the window scale
window.config(bg='#000000') # change the window color to black
window.resizable(False,False) # Disable window maximization

var = StringVar() # Create a Stringvar object
ent = Entry(window,bg='#000000',fg='#FFFFFF',state='normal',justify='right',font=('arial',30,'bold'),textvariable=var) # Create entry to print the output
ent.pack(ipady=34,ipadx=150) # Edit entry location

val = "" # A variable to save user input
A = 0 # The variable of converting the string to an integer
operator = "" # Variable definition of arithmetic operation

# Numbers and operators functions
def number0():
    global val
    val += '0'
    var.set(val)
    
def number1():
    global val
    val += '1'
    var.set(val)
    
def number2():
    global val
    val += '2'
    var.set(val)

def number3():
    global val
    val += '3'
    var.set(val)

def number4():
    global val
    val += "4"
    var.set(val)

def number5():
    global val
    val += "5"
    var.set(val)

def number6():
    global val
    val += "6"
    var.set(val)

def number7():
    global val
    val += "7"
    var.set(val)

def number8():
    global val
    val += "8"
    var.set(val)

def number9():
    global val
    val += "9"
    var.set(val)
    
def plus():
    global A
    global opeartor
    global val
    A = int(val)
    opeartor = "+"
    val += "+"
    var.set(val)

def Multiplied ():
    global A
    global opeartor
    global val
    A = int(val)
    opeartor = "*"
    val = val + "*"
    var.set(val)

def Minus():
    global A
    global opeartor
    global val
    A = int(val)
    opeartor = "-"
    val = val + "-"
    var.set(val)

def division():
    global A
    global opeartor
    global val
    A = int(val)
    opeartor = "/"
    val = val + "/"
    var.set(val)

def equal():
    global A
    global opeartor
    global val
    if opeartor == "+":
        x = int(val.split("+")[1])
        C = A + x
        var.set(C)
    elif opeartor == "*":
        x = int(val.split("*")[1])
        C = A * x
        var.set(C)
    elif opeartor == "-":
        x = int(val.split("-")[1])
        C = A - x
        var.set(C)
    elif opeartor == "/":
        x = float(val.split("/")[1])
        C = A / x
        var.set(C)

def c():
    global A
    global operator
    global val
    val = ""
    A = ""
    operator = ""
    var.set(val)
    
# Numbers and operators buttons
but1 = Button(window,text='C',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=30,pady=20,command=c)
but1.place(x=0,y=340)

but2 = Button(window,text='0',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=30,pady=20,command=number0)
but2.place(x=95,y=340)

but3 = Button(window,text='=',font=('arial',20,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=30,pady=15,command=equal)
but3.place(x=184,y=340)

but4 = Button(window,text='/',font=('arial',20,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=50,pady=20,command=division)
but4.place(x=275,y=350)

but5 = Button(window,text='7',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=31,pady=20,command=number7)
but5.place(x=0,y=260)

but6 = Button(window,text='8',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=31,pady=20,command=number8)
but6.place(x=94,y=260)

but7 = Button(window,text='9',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=31,pady=20,command=number9)
but7.place(x=188,y=260)

but8 = Button(window,text='*',font=('arial',20,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=47,pady=16,command=Multiplied)
but8.place(x=275,y=265)

but9 = Button(window,text='4',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=31,pady=20,command=number4)
but9.place(x=0,y=180)

but9 = Button(window,text='5',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=28,pady=20,command=number5)
but9.place(x=93,y=180)

but10 = Button(window,text='6',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=30,pady=20,command=number6)
but10.place(x=181,y=180)

but11 = Button(window,text='-',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=50,pady=20,command=Minus)
but11.place(x=273,y=180)

but12 = Button(window,text='1',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=30,pady=20,command=number1)
but12.place(x=0,y=95)

but13 = Button(window,text='2',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=30,pady=20,command=number2)
but13.place(x=90,y=95)

but14 = Button(window,text='3',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=30,pady=20,command=number3)
but14.place(x=180,y=95)

but15 = Button(window,text='+',font=('arial',17,'bold'),bg='#FF5900',fg='#FFFFFF',relief='flat',padx=50,pady=20,command=plus)
but15.place(x=272,y=95)

window.mainloop() # show window
#End
