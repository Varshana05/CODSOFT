from  tkinter import *
from tkinter.messagebox import *

def entertask():
    def add():
        task = txtTask.get(1.0, "end-1c")
        if task=="":
            showwarning(title="Warning!",
                        message="Please enter some text")
        else:
            lbTask.insert(END,task)
            dialog.destroy()

    dialog = Tk()
    dialog.title("Add Task")
    txtTask = Text(dialog,
                width=40,
                height=4)
    txtTask.pack()
    btnAdd = Button(dialog,
            text="Add Task",
            command = add)
    btnAdd.pack()
    dialog.mainloop()
    

def deletetask():
    selected=lbTask.curselection()
    lbTask.delete(selected[0])

def markcompleted():
    marked=lbTask.curselection()
    temp=marked[0]
    temp_marked=lbTask.get(marked)
    temp_marked=temp_marked+" ✔"
    lbTask.delete(temp)
    lbTask.insert(temp,temp_marked)

w = Tk()
w.title("My ToDo App")

f = Frame(w)
f.pack()

lbTask = Listbox(f,
            bg="pink",
            fg="white",
            height=15,
            width=50,
            font = "Helvetica")

lbTask.pack(side=LEFT)

sbTask = Scrollbar(f)
sbTask.pack(side=RIGHT,fill=Y)
lbTask.config(yscrollcommand=sbTask.set)
sbTask.config(command=lbTask.yview)

btnAdd = Button(w,
        text="Add task",
        width=50,
        command=entertask)

btnAdd.pack(pady=3)

btnDelete = Button(w,
        text="Delete selected task",
        width=50,
        command=deletetask)

btnDelete.pack(pady=3)

btnMark = Button(w,
        text="Mark as completed ",
        width=50,
        command=markcompleted)

btnMark.pack(pady=3)

w.mainloop()
