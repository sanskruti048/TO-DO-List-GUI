# TO-DO LIST ON GUI (Graphical User Interface)

import tkinter as tk
from tkinter import messagebox, font

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced To-Do List App")
        self.root.geometry("800x800")
        self.root.configure(bg="#f0f0f0")

        # Set a custom font
        self.custom_font = font.Font(family="Helvetica", size=12)

        # Create a frame for the content and center it
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title frame
        title_frame = tk.Frame(main_frame, bg="#f0f0f0")
        title_frame.grid(row=0, column=0, columnspan=2, pady=10)

        title_label = tk.Label(
            title_frame,
            text="Advanced To-Do List",
            font=("Georgia", 25, "bold"),
            bg="#f0f0f0"
        )
        title_label.grid(row=0, column=0)

        # Create a frame for the listbox and scrollbar
        frame = tk.Frame(main_frame, bg="#f0f0f0")
        frame.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

        # Create a listbox to display tasks
        self.task_listbox = tk.Listbox(
            frame,
            width=60,
            height=10,
            selectmode=tk.SINGLE,
            font=self.custom_font,
        )
        self.task_listbox.grid(row=0, column=0, sticky="nsew")

        # Create a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(frame)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Configure the scrollbar
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry box to add new tasks
        self.task_entry = tk.Entry(main_frame, width=50, font=self.custom_font)
        self.task_entry.grid(row=2, column=0, columnspan=2, pady=10)

        # Priority dropdown
        self.priority_var = tk.StringVar(value="Low")
        self.priority_menu = tk.OptionMenu(
            main_frame, self.priority_var, "Low", "Medium", "High"
        )
        self.priority_menu.config(font=self.custom_font)
        self.priority_menu.grid(row=3, column=0, columnspan=2, pady=5)

        # Create a frame for buttons to fit properly
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

        # Add task button
        self.add_task_button = tk.Button(
            button_frame,
            text="Add Task",
            command=self.add_task,
            font=self.custom_font,
            bg="#4CAF50",
            fg="white",
            width=20,
        )
        self.add_task_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        # Remove task button
        self.remove_task_button = tk.Button(
            button_frame,
            text="Remove Task",
            command=self.remove_task,
            font=self.custom_font,
            bg="#F44336",
            fg="white",
            width=20,
        )
        self.remove_task_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Mark as Completed button
        self.complete_task_button = tk.Button(
            button_frame,
            text="Mark as Completed",
            command=self.mark_completed,
            font=self.custom_font,
            bg="#2196F3",
            fg="white",
            width=20,
        )
        self.complete_task_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Edit Task button
        self.edit_task_button = tk.Button(
            button_frame,
            text="Edit Task",
            command=self.edit_task,
            font=self.custom_font,
            bg="#2196F3",
            fg="white",
            width=20,
        )
        self.edit_task_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Sort buttons
        self.sort_priority_button = tk.Button(
            button_frame,
            text="Sort by Priority",
            command=self.sort_by_priority,
            font=self.custom_font,
            bg="#8BC34A",
            fg="white",
            width=20,
        )
        self.sort_priority_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        # Search Entry and Button in a separate frame
        search_frame = tk.Frame(main_frame, bg="#f0f0f0")
        search_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

        self.search_entry = tk.Entry(search_frame, width=40, font=self.custom_font)
        self.search_entry.grid(row=0, column=0, padx=5, pady=5)

        self.search_button = tk.Button(
            search_frame,
            text="Search",
            command=self.search_task,
            font=self.custom_font,
            bg="#FF9800",
            fg="white",
        )
        self.search_button.grid(row=0, column=1, padx=5, pady=5)

        # Theme selector
        tk.Label(main_frame, text="Theme:", font=self.custom_font, bg="#f0f0f0").grid(
            row=6, column=0, pady=5, padx=20, sticky="w"
        )
        self.theme_var = tk.StringVar(value="Light")
        self.theme_menu = tk.OptionMenu(
            main_frame, self.theme_var, "Light", "Dark", command=self.change_theme
        )
        self.theme_menu.config(font=self.custom_font)
        self.theme_menu.grid(row=6, column=1, pady=5, padx=20, sticky="ew")

        # Data structure to hold task information
        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        if task:
            self.tasks.append(
                {"task": task, "priority": priority, "status": "Pending"}
            )
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def mark_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["status"] = "Completed"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def edit_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]

            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Task")
            edit_window.geometry("400x200")

            tk.Label(edit_window, text="Task:", font=self.custom_font).pack(pady=5)
            task_entry = tk.Entry(edit_window, font=self.custom_font, width=30)
            task_entry.insert(0, task["task"])
            task_entry.pack(pady=5)

            tk.Label(edit_window, text="Priority:", font=self.custom_font).pack(pady=5)
            priority_var = tk.StringVar(value=task["priority"])
            priority_menu = tk.OptionMenu(
                edit_window, priority_var, "Low", "Medium", "High"
            )
            priority_menu.pack(pady=5)

            def save_changes():
                task["task"] = task_entry.get()
                task["priority"] = priority_var.get()
                self.update_task_list()
                edit_window.destroy()

            tk.Button(
                edit_window,
                text="Save Changes",
                command=save_changes,
                font=self.custom_font,
                bg="#4CAF50",
                fg="white",
            ).pack(pady=10)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def search_task(self):
        query = self.search_entry.get().lower()
        if query:
            matching_tasks = [
                task for task in self.tasks if query in task["task"].lower()
            ]
            self.update_task_list(matching_tasks)
        else:
            messagebox.showwarning("Warning", "Please enter a keyword to search.")

    def sort_by_priority(self):
        self.tasks.sort(key=lambda x: {"High": 1, "Medium": 2, "Low": 3}[x["priority"]])
        self.update_task_list()

    def change_theme(self, theme):
        themes = {
            "Light": {"bg": "#f0f0f0", "fg": "black"},
            "Dark": {"bg": "#333333", "fg": "white"},
        }
        colors = themes[theme]
        self.root.configure(bg=colors["bg"])
        for widget in self.root.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.configure(bg=colors["bg"], fg=colors["fg"])

    def update_task_list(self, tasks=None):
        self.task_listbox.delete(0, tk.END)
        tasks_to_display = tasks if tasks else self.tasks
        for i, task in enumerate(tasks_to_display, 1):
            display_text = (
                f"{i}. {task['task']} (Priority: {task['priority']}, "
                f"Status: {task['status']})"
            )
            self.task_listbox.insert(tk.END, display_text)


if __name__ == "__main__":
    root = tk.Tk()
    todo_app = ToDoListApp(root)
    root.mainloop()
