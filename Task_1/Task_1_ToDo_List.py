from tkinter import*
from tkinter import messagebox

# Create window
root=Tk()

root.title("To-Do List")
root.geometry("400x400")
root.config(bg="lightgrey")
label=Label(root,text="To-Do List",font=("Cooper Black",15),fg="black",bg="light grey")
label.pack()



e = Entry(root, width=20, borderwidth=5, font=("Bell MT", 20), justify='right')
e.pack(pady=10, padx=20, fill=X,ipady=5)
# Function to add task
def add_task():
    task=e.get()
    if task:
        listbox.insert(END,task)
        e.delete(0,END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please add some task")

# Function to delete selected task
def delete_task():
    try:
        selected_task_index=listbox.curselection()[0]
        listbox.delete(selected_task_index)
        save_tasks()
    except:
        messagebox.showwarning("Selection Error", "Please select task to delete!")

# Function to clear all tasks
def clear_all():
    if messagebox.askyesno("Confirm","Are you sure you want to clear all tasks?"):
        listbox.delete(0, END)
        save_tasks()

# Save tasks
def save_tasks():
    with open("my_tasks.txt","w") as f:
        for i in range(listbox.size()):
            f.write(listbox.get(i)+ "\n")

def load_tasks():
    try:
        with open("my_tasks.txt","r") as f:
            my_tasks=f.read().splitlines()
            for task in my_tasks:
                listbox.insert(END,task)
    except FileNotFoundError:
        pass

# Buttons Frame
bttn_frame = Frame(root, bg="lightgrey")
bttn_frame.pack(pady=10)

# Add Button
bttn = Button(bttn_frame, text="Add Task", width=12, command=add_task, bg="sky blue", fg="white")
bttn.grid(row=0, column=0, padx=5)

# Delete Button
bttn = Button(bttn_frame, text="Delete Task", width=12, command=delete_task, bg="red", fg="white")
bttn.grid(row=0, column=1, padx=5)

# Clear All Button
bttn = Button(bttn_frame, text="Clear All", width=12, command=clear_all, bg="orange", fg="white")
bttn.grid(row=0, column=2, padx=5)

# Listbox for tasks
listbox = Listbox(root, font=("Bodoni MT", 14), height=8, selectbackground="light blue", activestyle='none')
listbox.pack(pady=7, padx=14, fill=BOTH, expand=True)


load_tasks()
root.mainloop()


