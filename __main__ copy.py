import tkinter as tk
import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkEntry, CTkCheckBox, CTkButton
from PIL import ImageTk, Image
import os
import json
from tkinter import messagebox

file_path = "customerdb.json"
user_data_path = "user_data\\"
# checkvalue = tk.IntVar(value=1)

checkvalue = None 

def create_login_window():
    login_window = CTk()
    login_window_width = 500
    login_window_height = 500
    login_window.geometry(f"{login_window_width}x{login_window_height}")
    login_window.title("Parking Management System")


    def create_checkvalue():
        global checkvalue
        checkvalue = tk.IntVar(value=1)

    def on_entry_click(entry, default_text):
        if entry.get() == default_text:
            entry.delete(0, tk.END)
            entry.insert(0, '')
            entry.configure(font=('Calibri', 14, "normal"))

    def on_entry_typing(event, entry, default_text):
        current_text = entry.get()
        if current_text == default_text:
            entry.delete(0, tk.END)
            entry.configure(font=('HP Simplified', 10, "italic"))
        else:
            entry.configure(font=('Calibri', 14, "normal"))


    def on_focus_out(entry, default_text):
        if entry.get() == '':
            entry.configure(font=('HP Simplified', 10, "italic"))
            entry.insert(0, default_text)
            

    def check_fields(*args):
        all_filled = all(entry_var.get() != f"{label} goes here" for entry_var, label in zip(entry_variables, field_labels))
        Login_button.configure(state="normal" if all_filled else "disabled")


    if not os.path.exists(file_path):
        with open(file_path, "w") as json_file:
            json_file.write("[]") 


    def getvals():
        customer_data = {}
        for label, entry_var, entry in zip(field_labels, entry_variables, entries):
            customer_data[label] = entry_var.get()
            entry.delete(0, tk.END)
            on_focus_out(entry, f"{label} goes here")

        with open(file_path, "r+") as json_file:
            content = json_file.read()
            existing_entries = json.loads(content)
            customer_number = len(existing_entries) + 1
            customer_entry = {"Customer Number": customer_number, **customer_data}
            existing_entries.append(customer_entry)
            json_file.seek(0)
            json_file.truncate()
            json.dump(existing_entries, json_file, indent=2)
        # Save user data in a separate file if the checkbox is checked
        if checkvalue.get() == 1:
            user_file_path = os.path.join(user_data_path, f"{customer_data['Name']}_userdata.json")
            with open(user_file_path, "w") as user_file:
                user_data = {"Name": customer_data["Name"], "Password": customer_data["Password"]}
                json.dump(user_data, user_file, indent=2)
        
        messagebox.showinfo("Success", f"Customer number {customer_number} data stored in {file_path}")
        print(f"Customer number {customer_number} data stored in {file_path}")
        Login_button.configure(state="disabled")
        check_fields()

        login_window.destroy()
        create_homepage_window(login_window)

    def load_user_data():
        if not os.path.exists(user_data_path):
            os.makedirs(user_data_path)
        # Find the latest modified file in the user_data_path
        latest_file = max([f for f in os.listdir(user_data_path) if f.endswith(".json")],
                        key=lambda f: os.path.getmtime(os.path.join(user_data_path, f)), default=None)

        if latest_file:
            latest_file_path = os.path.join(user_data_path, latest_file)
            with open(latest_file_path, "r") as user_file:
                user_data = json.load(user_file)
                # Populate entry fields based on user data
                entry_variables[0].set(user_data.get("Name", ""))
                entry_variables[1].set(user_data.get("Password", ""))
                # Check the checkbox if user data exists
                checkvalue.set(1)
        else:
            # Set default values for entry fields
            entry_variables[0].set("Name goes here")
            entry_variables[1].set("Password goes here")
            checkvalue.set(1)


    create_checkvalue()
    # Form label
    # img1 = ImageTk.PhotoImage(Image.open("logo.png").resize((800, 800)))
    # Label_frame = CTkLabel(login_window, text="Registration Form", font=("ar", 15, "bold"), image=img1, anchor=tk.S)
    Label_frame = CTkLabel(login_window, text="Registration Form", font=("ar", 15, "bold"), anchor=tk.S)
    Label_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    left_half_canvas = ctk.CTkFrame(Label_frame)

    # Form fields names and packing
    field_labels = ["Name", "Password"]
    entry_variables = [tk.StringVar() for _ in range(len(field_labels))]

    # Name field
    group1 = ctk.CTkFrame(left_half_canvas)
    group1.pack(padx=5, pady=2, fill=tk.X, expand=True)
    label1 = CTkLabel(group1, text=field_labels[0])
    label1.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
    entry1 = CTkEntry(group1, textvariable=entry_variables[0])
    entry1.insert(0, f"{field_labels[0]} goes here")
    entry1.configure(font=('HP Simplified', 10, "italic"))
    entry1.pack(padx=5, pady=5, fill=tk.X, expand=True)
    entry1.bind('<FocusIn>', lambda event, entry=entry1, default_text=f"{field_labels[0]} goes here": on_entry_click(entry, default_text))
    entry1.bind('<Key>', lambda event, entry=entry1, default_text=f"{field_labels[0]} goes here": on_entry_typing(event, entry, default_text))
    entry1.bind('<FocusOut>', lambda event, entry=entry1, default_text=f"{field_labels[0]} goes here": on_focus_out(entry, default_text))


    # Password field
    group2 = ctk.CTkFrame(left_half_canvas)
    group2.pack(padx=5, pady=2, fill=tk.X, expand=True)
    label2 = CTkLabel(group2, text=field_labels[1])
    label2.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
    entry2 = CTkEntry(group2, textvariable=entry_variables[1])
    entry2.insert(0, f"{field_labels[1]} goes here")
    entry2.configure(font=('HP Simplified', 10, "italic"))
    entry2.pack(padx=5, pady=5, fill=tk.X, expand=True)
    entry2.bind('<FocusIn>', lambda event, entry=entry2, default_text=f"{field_labels[1]} goes here": on_entry_click(entry, default_text))
    entry2.bind('<Key>', lambda event, entry=entry2, default_text=f"{field_labels[1]} goes here": on_entry_typing(event, entry, default_text))
    entry2.bind('<FocusOut>', lambda event, entry=entry2, default_text=f"{field_labels[1]} goes here": on_focus_out(entry, default_text))

    group3 = ctk.CTkFrame(left_half_canvas)
    group3.pack(padx=5, pady=2, fill=tk.X, expand=True)
    # Creating Checkbox
    checkbtn = CTkCheckBox(group3, text="Remember me?", variable=checkvalue)
    checkbtn.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
    # Login button
    Login_button = CTkButton(group3, text="Login", command=getvals, state="disabled")
    Login_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

    # Binding to check fields when any entry is updated
    for entry in entry_variables:
        entry.trace_add('write', lambda *args: check_fields())

    # Creating a list of all CTkEntry widgets
    entries = [entry for group in [group1, group2] for entry in group.winfo_children() if isinstance(entry, CTkEntry)]

    left_half_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Call the check_fields function initially
    check_fields()
    load_user_data()

    return login_window



def create_homepage_window(login_window):
    homepage = CTk()
    homepage_width = 600
    homepage_height = 600
    homepage.geometry(f"{homepage_width}x{homepage_height}")
    homepage.title("Homepage (Parking Management System)")

    # Welcome Label
    welcome_label = CTkLabel(homepage, text="Welcome to Parking Management System", font=("Helvetica", 18, "bold"))
    welcome_label.pack(pady=20)

    # # Image
    # img_path = "parking_image.webp"  # Replace with the path to your image
    # if os.path.exists(img_path):
    #     img = ImageTk.PhotoImage(Image.open(img_path).resize((200, 200)))
    #     img_label = CTkLabel(homepage, image=img)
    #     img_label.image = img  # Keep a reference to avoid garbage collection
    #     img_label.pack(pady=20)
    # else:
    #     print("Image not found!")
    
        
    def manage_parking():
        # Functionality for managing parking
        print("Manage Parking")

    def view_reports():
        # Functionality for viewing reports
        print("View Reports")

    def log_out(current_window):
        current_window.withdraw()  # Hide the current window
        login_window = create_login_window()  # Recreate the login window
        login_window.mainloop()


    # Functionality Buttons
    button_frame = ctk.CTkFrame(homepage)
    button_frame.pack(pady=20)

    # Add more buttons as needed
    manage_parking_button = CTkButton(button_frame, text="Manage Parking", command=manage_parking)
    manage_parking_button.pack(side=tk.LEFT, padx=10)

    view_reports_button = CTkButton(button_frame, text="View Reports", command=view_reports)
    view_reports_button.pack(side=tk.LEFT, padx=10)

    go_back_button = CTkButton(button_frame, text="Logout", command=lambda: log_out (homepage))
    go_back_button.pack(side=tk.LEFT, padx=10)

    exit_button = CTkButton(button_frame, text="Exit", command=homepage.destroy)
    exit_button.pack(side=tk.LEFT, padx=10)

    homepage.mainloop()


# Initial creation of the login window
login_window = create_login_window()
login_window.mainloop()
