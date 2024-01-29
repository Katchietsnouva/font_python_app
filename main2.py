import tkinter as tk
from customtkinter import CTk, CTkLabel, CTkEntry, CTkCheckBox, CTkButton
from PIL import ImageTk, Image
import os
import json
from tkinter import messagebox

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Parking Management System")

        self.create_checkvalue()

        self.img1 = ImageTk.PhotoImage(Image.open("logo.png").resize((800, 800)))
        self.label_frame = CTkLabel(master, text="Registration Form", font=("ar", 15, "bold"), image=self.img1, anchor=tk.S)
        self.label_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.left_half_canvas = tk.Frame(self.label_frame)

        self.field_labels = ["Name", "Password"]
        self.entry_variables = [tk.StringVar() for _ in range(len(self.field_labels))]

        # Name field
        self.group1 = tk.Frame(self.left_half_canvas)
        self.group1.pack(padx=5, pady=2, fill=tk.X, expand=True)
        self.label1 = CTkLabel(self.group1, text=self.field_labels[0])
        self.label1.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        self.entry1 = CTkEntry(self.group1, textvariable=self.entry_variables[0])
        self.entry1.insert(0, f"{self.field_labels[0]} goes here")
        self.entry1.configure(font=('HP Simplified', 10, "italic"))
        self.entry1.pack(padx=5, pady=5, fill=tk.X, expand=True)
        self.entry1.bind('<FocusIn>', lambda event, entry=self.entry1, default_text=f"{self.field_labels[0]} goes here": self.on_entry_click(entry, default_text))
        self.entry1.bind('<Key>', lambda event, entry=self.entry1, default_text=f"{self.field_labels[0]} goes here": self.on_entry_typing(event, entry, default_text))
        self.entry1.bind('<FocusOut>', lambda event, entry=self.entry1, default_text=f"{self.field_labels[0]} goes here": self.on_focus_out(entry, default_text))

        # Password field
        self.group2 = tk.Frame(self.left_half_canvas)
        self.group2.pack(padx=5, pady=2, fill=tk.X, expand=True)
        self.label2 = CTkLabel(self.group2, text=self.field_labels[1])
        self.label2.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        self.entry2 = CTkEntry(self.group2, textvariable=self.entry_variables[1])
        self.entry2.insert(0, f"{self.field_labels[1]} goes here")
        self.entry2.configure(font=('HP Simplified', 10, "italic"))
        self.entry2.pack(padx=5, pady=5, fill=tk.X, expand=True)
        self.entry2.bind('<FocusIn>', lambda event, entry=self.entry2, default_text=f"{self.field_labels[1]} goes here": self.on_entry_click(entry, default_text))
        self.entry2.bind('<Key>', lambda event, entry=self.entry2, default_text=f"{self.field_labels[1]} goes here": self.on_entry_typing(event, entry, default_text))
        self.entry2.bind('<FocusOut>', lambda event, entry=self.entry2, default_text=f"{self.field_labels[1]} goes here": self.on_focus_out(entry, default_text))

        self.group3 = tk.Frame(self.left_half_canvas)
        self.group3.pack(padx=5, pady=2, fill=tk.X, expand=True)
        # Creating Checkbox
        self.checkbtn = CTkCheckBox(self.group3, text="Remember me?", variable=self.checkvalue)
        self.checkbtn.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        # Login button
        self.login_button = CTkButton(self.group3, text="Login", command=self.getvals, state="disabled")
        self.login_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        # Binding to check fields when any entry is updated
        for entry in self.entry_variables:
            entry.trace_add('write', lambda *args: self.check_fields())

        # Creating a list of all CTkEntry widgets
        self.entries = [entry for group in [self.group1, self.group2] for entry in group.winfo_children() if isinstance(entry, CTkEntry)]

        self.left_half_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Call the check_fields function initially
        self.check_fields()

    def create_checkvalue(self):
        self.checkvalue = tk.IntVar(value=1)

    def on_entry_click(self, entry, default_text):
        if entry.get() == default_text:
            entry.delete(0, tk.END)
            entry.insert(0, '')
            entry.configure(font=('Calibri', 14, "normal"))

    def on_entry_typing(self, event, entry, default_text):
        current_text = entry.get()
        if current_text == default_text:
            entry.delete(0, tk.END)
            entry.configure(font=('HP Simplified', 10, "italic"))
        else:
            entry.configure(font=('Calibri', 14, "normal"))

    def on_focus_out(self, entry, default_text):
        if entry.get() == '':
            entry.configure(font=('HP Simplified', 10, "italic"))
            entry.insert(0, default_text)

    def check_fields(self, *args):
        all_filled = all(entry_var.get() != f"{label} goes here" for entry_var, label in zip(self.entry_variables, self.field_labels))
        self.login_button.configure(state="normal" if all_filled else "disabled")

    def getvals(self):
        customer_data = {}
        for label, entry_var, entry in zip(self.field_labels, self.entry_variables, self.entries):
            customer_data[label] = entry_var.get()
            entry.delete(0, tk.END)
            self.on_focus_out(entry, f"{label} goes here")

        # Rest of your getvals function...

# Main Application
if __name__ == "__main__":
    root = CTk()
    login_page = LoginPage(root)
    root.mainloop()
