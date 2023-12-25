
# TASK - 2

import tkinter as tk
import tkinter.messagebox



def adding():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def removing():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
            tkinter.messagebox.showwarning("Warning", "Please add the task first .")



def updating():
     try:
        index = task_listbox.curselection()
        updated_task = task_entry.get()
        if updated_task:
            task_listbox.delete(index)
            task_listbox.insert(index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            tkinter.messagebox.showwarning("Warning", "Please enter an updated task.")
     except IndexError:
        tkinter.messagebox.showwarning("Warning", "Please select a task to update.")




screen = tk.Tk()
screen.title("To-Do List")
tasks = []
list_frame = tk.Listbox(screen,height=90,width=100)

task_listbox = tk.Listbox(screen)
task_listbox.pack(pady=10)

task_entry = tk.Entry(screen)
task_entry.pack(pady=10)

add_button = tk.Button(screen, text="  ADD   ",background="#ffd343", command=adding)
add_button.pack()

remove_button = tk.Button(screen, text="DELETE  ",background="#ffd343", command=removing)
remove_button.pack()

update_button = tk.Button(screen, text=" UPDATE",background="#ffd343", command=updating)
update_button.pack()



screen.mainloop()