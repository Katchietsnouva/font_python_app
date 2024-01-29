import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkCheckBox, CTkButton
from PIL import ImageTk, Image
import os
import json
from tkinter import messagebox

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Parking Management System")
        self.master.geometry("500x500")

        self.create_checkvalue()
        self.create_widgets()

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
        self.Login_button.configure(state="normal" if all_filled else "disabled")

    def getvals(self):
        customer_data = {}
        for label, entry_var, entry in zip(self.field_labels, self.entry_variables, self.entries):
            customer_data[label] = entry_var.get()
            entry.delete(0, tk.END)
            self.on_focus_out(entry, f"{label} goes here")

        with open(self.file_path, "r+") as json_file:
            content = json_file.read()
            existing_entries = json.loads(content)
            customer_number = len(existing_entries) + 1
            customer_entry = {"Customer Number": customer_number, **customer_data}
            existing_entries.append(customer_entry)
            json_file.seek(0)
            json_file.truncate()
            json.dump(existing_entries, json_file, indent=2)

        if self.checkvalue.get() == 1:
            user_file_path = os.path.join(self.user_data_path, f"{customer_data['Name']}_userdata.json")
            with open(user_file_path, "w") as user_file:
                user_data = {"Name": customer_data["Name"], "Password": customer_data["Password"]}
                json.dump(user_data, user_file, indent=2)

        messagebox.showinfo("Success", f"Customer number {customer_number} data stored in {self.file_path}")
        print(f"Customer number {customer_number} data stored in {self.file_path}")
        self.Login_button.configure(state="disabled")
        self.check_fields()
        self.master.destroy()
        LoginPage(self.master)

    def load_user_data(self):
        if not os.path.exists(self.user_data_path):
            os.makedirs(self.user_data_path)
        latest_file = max([f for f in os.listdir(self.user_data_path) if f.endswith(".json")],
                          key=lambda f: os.path.getmtime(os.path.join(self.user_data_path, f)), default=None)

        if latest_file:
            latest_file_path = os.path.join(self.user_data_path, latest_file)
            with open(latest_file_path, "r") as user_file:
                user_data = json.load(user_file)
                self.entry_variables[0].set(user_data.get("Name", ""))
                self.entry_variables[1].set(user_data.get("Password", ""))
                self.checkvalue.set(1)
        else:
            self.entry_variables[0].set("Name goes here")
            self.entry_variables[1].set("Password goes here")
            self.checkvalue.set(1)

    def create_widgets(self):
        img1 = ImageTk.PhotoImage(Image.open("logo.png").resize((800, 800)))
        Label_frame = CTkLabel(self.master, text="Registration Form", font=("ar", 15, "bold"), image=img1, anchor=tk.S)
        Label_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        left_half_canvas = CTkFrame(Label_frame)

        self.field_labels = ["Name", "Password"]
        self.entry_variables = [tk.StringVar() for _ in range(len(self.field_labels))]

        group1 = CTkFrame(left_half_canvas)
        group1.pack(padx=5, pady=2, fill=tk.X, expand=True)
        label1 = CTkLabel(group1, text=self.field_labels[0])
        label1.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        entry1 = CTkEntry(group1, textvariable=self.entry_variables[0])
        entry1.insert(0, f"{self.field_labels[0]} goes here")
        entry1.configure(font=('HP Simplified', 10, "italic"))
        entry1.pack(padx=5, pady=5, fill=tk.X, expand=True)
        entry1.bind('<FocusIn>', lambda event, entry=entry1, default_text=f"{self.field_labels[0]} goes here": self.on_entry_click(entry, default_text))
        entry1.bind('<Key>', lambda event, entry=entry1, default_text=f"{self.field_labels[0]} goes here": self.on_entry_typing(event, entry, default_text))
        entry1.bind('<FocusOut>', lambda event, entry=entry1, default_text=f"{self.field_labels[0]} goes here": self.on_focus_out(entry, default_text))

        group2 = CTkFrame(left_half_canvas)
        group2.pack(padx=5, pady=2, fill=tk.X, expand=True)
        label2 = CTkLabel(group2, text=self.field_labels[1])
        label2.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        entry2 = CTkEntry(group2, textvariable=self.entry_variables[1])
        entry2.insert(0, f"{self.field_labels[1]} goes here")
        entry2.configure(font=('HP Simplified', 10, "italic"))
        entry2.pack(padx=5, pady=5, fill=tk.X, expand=True)
        entry2.bind('<FocusIn>', lambda event, entry=entry2, default_text=f"{self.field_labels[1]} goes here": self.on_entry_click(entry, default_text))
        entry2.bind('<Key>', lambda event, entry=entry2, default_text=f"{self.field_labels[1]} goes here": self.on_entry_typing(event, entry, default_text))
        entry2.bind('<FocusOut>', lambda event, entry=entry2, default_text=f"{self.field_labels[1]} goes here": self.on_focus_out(entry, default_text))

        group3 = CTkFrame(left_half_canvas)
        group3.pack(padx=5, pady=2, fill=tk.X, expand=True)
        checkbtn = CTkCheckBox(group3, text="Remember me?", variable=self.checkvalue)
        checkbtn
if __name__ == "__main__":
    root = CTk()
    login_page = LoginPage(root)
    root.mainloop()
