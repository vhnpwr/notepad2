from tkinter import*
from  PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox
import os
root=Tk()

root.title("Notepad")
root.geometry("650x650")

open_img=ImageTk.PhotoImage(Image.open("open.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))

lbl_FileName=Label(root,text="File Name",font=("Arial",18,"bold"))
lbl_FileName.place(relx=0.3,rely=0.05,anchor=CENTER)

input_FileName=Entry(root,font=("Arial",18,"bold"))
input_FileName.place(relx=0.6,rely=0.05,anchor=CENTER)

my_text=Text(root,height=30,width=80)
my_text.place(relx=0.5,rely=0.5,anchor=CENTER)

name=""
def openFile():
    global name
    my_text.delete(1.0,END)
    input_FileName.delete(0,END)
    text_file=filedialog.askopenfilename(title="open text file",filetypes=(("Text Files","*.txt"),))
    name=os.path.basename(text_file)
    formatted_name=name.split(".")[0]
    input_FileName.insert(END,formatted_name)
    root.title(formatted_name)
    text_file=open(name,"r")
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
    
def saveFile():
    fileName=input_FileName.get()
    file=open(fileName+".txt","w")
    data=my_text.get("1.0",END)
    file.write(data)
    input_FileName.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("update","your file has been saved successfully")
    
def exitFile():
    root.destroy()
    
    

btn_openFile=Button(root,text="Open File",image=open_img,command=openFile)
btn_openFile.place(relx=0.05,rely=0.1,anchor=CENTER)

btn_saveFile=Button(root,text="Save File",image=save_img,command=saveFile)
btn_saveFile.place(relx=0.1,rely=0.1,anchor=CENTER)

btn_exitFile=Button(root,text="Exit Button",image=exit_img,command=exitFile)
btn_exitFile.place(relx=0.15,rely=0.1,anchor=CENTER)

root.mainloop()
