import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []

# Function to display menu
def display_menu():
    menu_frame.pack()
    task_frame.pack_forget()

# Function to add a task
def add_task():
    task = simpledialog.askstring("Add Task", "Enter a task:")
    if task:
        tasks.append(task)
        messagebox.showinfo("Task Manager", "Task added!")
        view_tasks()

# Function to view tasks
def view_tasks():
    menu_frame.pack_forget()
    task_frame.pack()
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        task_list.insert(tk.END, f"{i}. {task}")

# Function to delete a task
def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_number = selected_task_index[0]
        tasks.pop(task_number)
        messagebox.showinfo("Task Manager", "Task deleted!")
        view_tasks()
    else:
        messagebox.showwarning("Task Manager", "No task selected!")

def quit_program():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Task Manager")

# Menu frame
menu_frame = tk.Frame(root)
tk.Button(menu_frame, text="Add Task", command=add_task).pack(fill=tk.BOTH, expand=True)
tk.Button(menu_frame, text="View Tasks", command=view_tasks).pack(fill=tk.BOTH, expand=True)
tk.Button(menu_frame, text="Quit", command=quit_program).pack(fill=tk.BOTH, expand=True)

# Task frame
task_frame = tk.Frame(root)
task_list = tk.Listbox(task_frame)
task_list.pack(fill=tk.BOTH, expand=True)
tk.Button(task_frame, text="Delete Task", command=delete_task).pack(fill=tk.BOTH, expand=True)
tk.Button(task_frame, text="Back to Menu", command=display_menu).pack(fill=tk.BOTH, expand=True)

# Start with the menu frame
display_menu()

root.mainloop()
