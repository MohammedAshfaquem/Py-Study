from tkinter import *

window = Tk()
window.title('First Gui')
window.geometry("600x400")
window.resizable(False,False)
window.iconbitmap('Week4\Day4\phython.ico')
window.configure(bg='red')

n1 = Label(window,text='Num 1',font='Impact 20')
n2 = Label(window,text='Num 2')
n3 = Label(window,text='Result')
 
def Sum():
    tot = int(t1.get())+ int(t2.get())  
    res.set(tot)
res = StringVar()
b1 = Button(window,text="Submit",command=Sum)   

# for btn


t1 = Entry(window)
t2 = Entry(window)
t3 = Entry(window,textvariable=res)



n1.pack() 
t1.pack()    
n2.pack()   
t2.pack() 
n3.pack()      
t3.pack()    
b1.pack()



window.mainloop()