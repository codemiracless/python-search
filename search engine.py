from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import webbrowser
window=Tk()
window.geometry('400x400')
l1=Label(window,text="morse")
window.title('The Python Search Engine')
window.configure(bg='white')
window.grid()
def buttonfunction():
    try:
        message=simpledialog.askstring("enter url","enter website url")
        message=message.upper()
        webbrowser.open("www."+message+".com")
    except:
        messagebox.showinfo('question','the url is incorrect')
def butto():
    webbrowser.open("www.instagram.com")
def butt2():
    webbrowser.open("www.facebook.com")
def butt3():
    webbrowser.open("www.twitter.com")
b=Button(window,text=" Search engine",command=buttonfunction,bg='pink')
b.pack()
b1=Button(window,text="Instagram",command=butto,bg='orange')
b1.pack()
b2=Button(window,text="Facebook",command=butt2,bg='lightblue')
b2.pack()
b3=Button(window,text="Twitter",command=butt3,bg='orange')
b3.pack()
window.mainloop()
