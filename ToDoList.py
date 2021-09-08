# TODO GUI
from os import sep
import tkinter as tk
from tkinter import Entry, Label, Button, Listbox, StringVar
from tkinter.constants import END, INSIDE, TRUE
from typing import Text



def addTasks():
    """
    Arguments:
        if text in entry box
        StringVar - new_task: is inserted into the list box at the end or bottom 
        reset StringVar to nothing
    """
    task_list_box.insert(END, new_task.get())
    new_task.set("")
    
def deleteTasks():
    """
    Arguments:
        if element is selected in listbox and delete button selected
        remove selected tasks   
    """
    item = task_list_box.curselection()
    task_list_box.delete(item)

def updateFile():
    """
    Arguments:
        when save button is selected
        open txt file in write mode
        write each element of the list box 
        close file when done
    """
    my_file = open(task_list_file, "w")
    for item in task_list_box.get(0, END):
        my_file.writelines(str(item) + "\n")
    my_file.flush()    
    my_file.close()
global task_list    

#file to store tasks
task_list_file = "\coding-portfolio\current_tasks.txt"

#if file exists, read text and store into a list, otherwise keep going
if task_list_file:
    tlf = open(task_list_file, "r")
    existing_tasks = tlf.read().split("\n")
else:
    pass

root = tk.Tk()
root.title("To Do List")

mainframe = tk.Frame(root, padx=3, pady=5, bg="#828282")
mainframe.grid(row=0, column=0, sticky="NSEW")

root.resizable(width=False, height=True)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=20)

root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(2, weight=1)

#button that will save elements in listbox to a txt file
save_button = tk.Button(mainframe, text="Save", highlightbackground="#07f55a", padx=10, pady=10, command=updateFile)
save_button.grid(row=0, column=1, sticky="N", padx=(50,10), pady=(15,15))

#button to remove tasks when they select it in the listbox and select the delete button
remove_tasks = tk.Button(mainframe, text="Delete", highlightbackground="#e01212", padx=10, pady=10, command=deleteTasks)
remove_tasks.grid(row=0, column=2, sticky="N", padx=(200, 10), pady=(15,15))

#button to add tasks
add_tasks = tk.Button(mainframe, text="+", highlightbackground="#0013b5", padx=10, pady=10, command=addTasks)
add_tasks.grid(row=0, column=3, sticky="NE", pady=(15,15))

#variable to capture the text in the entry box
new_task = StringVar()

#entry widget where user will type in tasks
task_entry = Entry(mainframe, textvariable=new_task)
task_entry.grid(row=1, column=0, columnspan=3)

#widget to hold tasks
task_list_box = Listbox(mainframe, background="#18261c", fg="#ebedeb")
task_list_box.grid(row=2, column=0, columnspan=3)

#load existings files if current_tasks.txt exists
if len(existing_tasks) > 0:
    for item in existing_tasks:
        task_list_box.insert(END, item)

root.mainloop()