import tkinter as tk
from tkinter import *
import random
import pyodbc 
import time
from PIL import ImageTk, Image
difficulty_level=0              #global variable to store difficulty level through out the program


def menu():
    """
    Menu that will be used by user to select the quiz difficulty level

    """
    root.destroy()              #destroying root window
    global menu 
    menu = Tk()
    
    menu_canvas = Canvas(menu,width=720,height=440,bg="black")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="white")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z ',fg="orange",bg="black") 
    wel.config(font=('Cooper black', 15))
    wel.place(relx=0.3,rely=0.02)
    
    
    level = Label(menu_frame,text='Select your Difficulty Level !!',bg="white",font="calibri 18")
    level.place(relx=0.25,rely=0.3)
    
    
    var = IntVar()              #creating variable to store user difficulty level selection
    easyR = Radiobutton(menu_frame,text='Easy',bg="white",font="calibri 16",value=1,variable = var)
    easyR.place(relx=0.25,rely=0.4)
    
    mediumR = Radiobutton(menu_frame,text='Medium',bg="white",font="calibri 16",value=2,variable = var)
    mediumR.place(relx=0.25,rely=0.5)
    
    hardR = Radiobutton(menu_frame,text='Hard',bg="white",font="calibri 16",value=3,variable = var)
    hardR.place(relx=0.25,rely=0.6)
    
    
    def navigate():                 #navigating to specific window based on difficulty level selection
        
        x = var.get()
        global difficulty_level
        difficulty_level=x
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
        
        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="grey",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()
def easy():
    """
    it provide easy level questions to the user

    """

    global e
    e = Tk()
    easy_canvas = Canvas(e,width=720,height=440,bg="black")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="white")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():         #it is used to set the timer 
        check = 0
        for k in range(30, 0, -1):
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        easy_frame.update()
        time.sleep(2)
        if check==-1:
            return (-1)
        else:
            return 0
    
    global scores           
    score = 0
    
    conn = pyodbc.connect('Driver={SQL Server};'            #it is used to make connection with the SQL database
                      'Server=DESKTOP-F8MPIMM\SQLEXPRESS;'
                      'Database=quizapplication;'
                      'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM quizapplication.dbo.easy')    #extracting data from databse
    lst=[]
    lstofques=[]
    lstofans=[]
    for row in cursor:
        lst.append(list(row))
   
    i=0
    while (i <len(lst)):                        #coverting of data into two different list
        lstofques.append(lst[i][1:-1])
        lstofans.append((lst[i][-1]))
        i=i+1
    
    easyQ = lstofques
    answer =lstofans

    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])

    
    ques = Label(easy_frame,text =easyQ[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar(e,"1")                  #creating variable to store question's answer
    
    a = Radiobutton(easy_frame,text=easyQ[x][1],font="calibri 10",value=easyQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=easyQ[x][2],font="calibri 10",value=easyQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_frame,text=easyQ[x][3],font="calibri 10",value=easyQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_frame,text=easyQ[x][4],font="calibri 10",value=easyQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():  #method to display series of question and options
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
            li.remove(x)

            
    def calc():   #method to calculate score
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(easy_frame,command=calc,text="Submit",bg="grey")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(easy_frame,command=display,text="Next",bg="grey")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    y = countDown()
    if y == -1:
        e.destroy()
        showMark(score)
    e.mainloop()
      
def medium():
    """
    it provide difficulty level questions to the user

    """
    """
    it provide medium level question to the user

    """
    
    global m
    m = Tk()
    
    med_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="white")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():        #it is used to set the timer 
        check = 0
        for k in range(30, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        med_frame.update()
        time.sleep(2)
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0

    conn = pyodbc.connect('Driver={SQL Server};'           #it is used to make connection with the SQL database
                      'Server=DESKTOP-F8MPIMM\SQLEXPRESS;'
                      'Database=quizapplication;'
                      'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM quizapplication.dbo.medium')    #extracting data from databse
    lst=[]
    lstofques=[]
    lstofans=[]
    for row in cursor:
        lst.append(list(row))
   
    i=0
    while (i <len(lst)):                  #coverting of data into two different list
        lstofques.append(lst[i][1:-1])
        lstofans.append((lst[i][-1]))
        i=i+1
    
    mediumQ = lstofques
    answer = lstofans 
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(med_frame,text =mediumQ[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar(m,"1")
    
    a = Radiobutton(med_frame,text=mediumQ[x][1],font="calibri 10",value=mediumQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_frame,text=mediumQ[x][2],font="calibri 10",value=mediumQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_frame,text=mediumQ[x][3],font="calibri 10",value=mediumQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_frame,text=mediumQ[x][4],font="calibri 10",value=mediumQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():             #method to display series of question and options
        
        if len(li) == 1:
                m.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =mediumQ[x][0])
            
            a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
            b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
            c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
            d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
            
            li.remove(x)

    def calc():                 #method to calculate score
        global score
        if (var.get() in answer):
            score+=1
        display()
    submit = Button(med_frame,command=calc,text="Submit",bg="grey")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med_frame,command=display,text="Next",bg="grey")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        m.destroy()
        showMark(score)
    m.mainloop()

    m.mainloop()
def difficult():
    
       
    global h
    h = Tk()
    
    hard_canvas = Canvas(h,width=720,height=440,bg="#101357")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas,bg="white")
    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():          #it is used to set the timer 
        check = 0
        for k in range(30, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    conn = pyodbc.connect('Driver={SQL Server};'              #it is used to make connection with the SQL database
                      'Server=DESKTOP-F8MPIMM\SQLEXPRESS;'
                      'Database=quizapplication;'
                      'Trusted_Connection=yes;')
     
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM quizapplication.dbo.hard')        #extracting data from databse
    lst=[]
    lstofques=[]
    lstofans=[]
    for row in cursor:
        lst.append(list(row))
   
    i=0
    while (i <len(lst)):                    #coverting of data into two different list
        lstofques.append(lst[i][1:-1])
        lstofans.append((lst[i][-1]))
        i=i+1

    hardQ = lstofques
    answer = lstofans  
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(hard_frame,text =hardQ[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar(h,"1")                          #creating variable to store question's answer
    
    a = Radiobutton(hard_frame,text=hardQ[x][1],font="calibri 10",value=hardQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(hard_frame,text=hardQ[x][2],font="calibri 10",value=hardQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(hard_frame,text=hardQ[x][3],font="calibri 10",value=hardQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(hard_frame,text=hardQ[x][4],font="calibri 10",value=hardQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(h)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():          #method to display series of question and options
        
        if len(li) == 1:
                h.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =hardQ[x][0])
            
            a.configure(text=hardQ[x][1],value=hardQ[x][1])
      
            b.configure(text=hardQ[x][2],value=hardQ[x][2])
      
            c.configure(text=hardQ[x][3],value=hardQ[x][3])
      
            d.configure(text=hardQ[x][4],value=hardQ[x][4])
            
            li.remove(x)

            
    def calc():           #method to calculate score
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(hard_frame,command=calc,text="Submit",bg="grey")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(hard_frame,command=display,text="Next",bg="grey")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(mark):
    
    
    global sh
    sh = Tk()
    
    show_canvas = Canvas(sh,width=720,height=440,bg="black")
    show_canvas.pack()

    show_frame = Frame(show_canvas,bg="white")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    if(mark==5):                        #setting result based on marks scored
        st="Very Strong"
    elif(mark==4):
        st="Strong"
    elif(mark==3):
        st="Good"
    elif(mark==2):
        st="Bad"
    elif(mark==1):
        st="Poor"
    else:
        st="Failed"
    
    mlabel = Label(show_canvas,text=st,fg="orange",font=("cooper black",40),bg="white")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    button = Button(sh, text='Check Answers',command = answer ) 
    button.configure(width = 10,height=2, activebackground = "#33B5E5", bg ='grey', relief = RAISED)
    button.place(relx=0.5,rely=0.6,anchor=CENTER)
    sh.mainloop()

def answer():
    sh.destroy()
    global a
    a = Tk()
    ans_canvas = Canvas(a,width=720,height=500,bg="black")
    ans_canvas.pack()

    ans_frame = Frame(ans_canvas,bg="white")
    ans_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    if(difficulty_level==1):        #Extracting question and ans for difficulty level: Easy
         conn = pyodbc.connect('Driver={SQL Server};'
                               'Server=DESKTOP-F8MPIMM\SQLEXPRESS;'
                              'Database=quizapplication;'
                              'Trusted_Connection=yes;')
         cursor = conn.cursor()
         cursor.execute('SELECT * FROM quizapplication.dbo.easy')
    elif(difficulty_level==2):      #Extracting question and ans for difficulty level: Medium
        conn = pyodbc.connect('Driver={SQL Server};'
                               'Server=DESKTOP-F8MPIMM\SQLEXPRESS;'
                              'Database=quizapplication;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM quizapplication.dbo.medium')
    else:                           #Extracting question and ans for difficulty level: Hard
        conn = pyodbc.connect('Driver={SQL Server};'
                               'Server=DESKTOP-F8MPIMM\SQLEXPRESS;'
                              'Database=quizapplication;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM quizapplication.dbo.hard')

    lst=[]
    lstofques=[]
    lstofans=[]
    for row in cursor:
        lst.append(list(row))
   
    i=0
    while (i <len(lst)):
        lstofques.append(lst[i][1])
        lstofans.append((lst[i][6]))
        i=i+1
    
    question = lstofques
    answer =lstofans

      #displaying question and its answer
    ques = Label(ans_frame,text =question[0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.1,anchor=CENTER)
    ans = Label(ans_frame,text =answer[0],font="calibri 12",bg="white")
    ans.place(relx=0.5,rely=0.15,anchor=CENTER)
    
    ques = Label(ans_frame,text =question[1],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.25,anchor=CENTER)
    ans = Label(ans_frame,text =answer[1],font="calibri 12",bg="white")
    ans.place(relx=0.5,rely=0.3,anchor=CENTER)
    
    ques = Label(ans_frame,text =question[2],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.4,anchor=CENTER)
    ans = Label(ans_frame,text =answer[2],font="calibri 12",bg="white")
    ans.place(relx=0.5,rely=0.45,anchor=CENTER)
    
    ques = Label(ans_frame,text =question[3],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.55,anchor=CENTER)
    ans = Label(ans_frame,text =answer[3],font="calibri 12",bg="white")
    ans.place(relx=0.5,rely=0.6,anchor=CENTER)
    
    ques = Label(ans_frame,text =question[4],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.7,anchor=CENTER)
    ans = Label(ans_frame,text =answer[4],font="calibri 12",bg="white")
    ans.place(relx=0.5,rely=0.75,anchor=CENTER)
   
    a.mainloop()

def start():
    """
    Home screen of application

    Returns
    -------
    None.

    """
    global root 
    root = Tk()
    canvas = Canvas(root,width = 720,height = 440)
    canvas.grid(column = 0 , row = 1)
    img = ImageTk.PhotoImage(file="quiztime.png")   #using image as background of home screen
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Start',command = menu ) 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", bg ='blue', relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if __name__=='__main__':    #application initializes
    start()
