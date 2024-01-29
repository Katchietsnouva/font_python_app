import tkinter as tk
import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkEntry, CTkCheckBox, CTkButton
from PIL import ImageTk, Image
import os
import json
from tkinter import messagebox

file_path = "customerdb.json"
# user_data_path = "user_data\"

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
    submit_button.configure(state="normal" if all_filled else "disabled")


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

        # Parse the existing content as JSON
        existing_entries = json.loads(content)

        # Determine the customer number dynamically
        customer_number = len(existing_entries) + 1

        # Append the new entry with the customer number
        customer_entry = {"Customer Number": customer_number, **customer_data}
        existing_entries.append(customer_entry)

        # Set the cursor to the beginning of the file and truncate the content
        json_file.seek(0)
        json_file.truncate()

        # Write the updated content back to the file
        json.dump(existing_entries, json_file, indent=2)

    # Display a popup message with the customer number
    messagebox.showinfo("Success", f"Customer number {customer_number} data stored in {file_path}")
    print(f"Customer number {customer_number} data stored in {file_path}")

    # Disable the submit button after submitting
    submit_button.configure(state="disabled")

    # Call the check_fields function to update the button state
    check_fields()
          
root = CTk()
root_width = 500
root_height = 500
root.geometry(f"{root_width}x{root_height}")
root.title("Parking Management System")

# Form label
img1 = ImageTk.PhotoImage(Image.open("logo.png").resize((800, 800)))
Label_frame = CTkLabel(root, text="Registration Form", font=("ar", 15, "bold"), image=img1, anchor=tk.S)
Label_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

left_half_canvas = ctk.CTkFrame(Label_frame)

# Form fields names and packing
field_labels = ["Name", "Phone", "Gender", "Car Number Plate", "Time In", "Payment Mode"]
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


# Phone field
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

# Gender field
group3 = ctk.CTkFrame(left_half_canvas)
group3.pack(padx=5, pady=3, fill=tk.X, expand=True)
label3 = CTkLabel(group3, text=field_labels[2])
label3.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
entry3 = CTkEntry(group3, textvariable=entry_variables[2])
entry3.insert(0, f"{field_labels[2]} goes here")
entry3.configure(font=('HP Simplified', 10, "italic"))
entry3.pack(padx=5, pady=5, fill=tk.X, expand=True)
entry3.bind('<FocusIn>', lambda event, entry=entry3, default_text=f"{field_labels[2]} goes here": on_entry_click(entry, default_text))
entry3.bind('<Key>', lambda event, entry=entry3, default_text=f"{field_labels[2]} goes here": on_entry_typing(event, entry, default_text))
entry3.bind('<FocusOut>', lambda event, entry=entry3, default_text=f"{field_labels[2]} goes here": on_focus_out(entry, default_text))

# Car Number Plate field
group4 = ctk.CTkFrame(left_half_canvas)
group4.pack(padx=5, pady=4, fill=tk.X, expand=True)
label4 = CTkLabel(group4, text=field_labels[3])
label4.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
entry4 = CTkEntry(group4, textvariable=entry_variables[3])
entry4.insert(0, f"{field_labels[3]} goes here")
entry4.configure(font=('HP Simplified', 10, "italic"))
entry4.pack(padx=5, pady=5, fill=tk.X, expand=True)
entry4.bind('<FocusIn>', lambda event, entry=entry4, default_text=f"{field_labels[3]} goes here": on_entry_click(entry, default_text))
entry4.bind('<Key>', lambda event, entry=entry4, default_text=f"{field_labels[3]} goes here": on_entry_typing(event, entry, default_text))
entry4.bind('<FocusOut>', lambda event, entry=entry4, default_text=f"{field_labels[3]} goes here": on_focus_out(entry, default_text))

# Time In field
group5 = ctk.CTkFrame(left_half_canvas)
group5.pack(padx=5, pady=5, fill=tk.X, expand=True)
label5 = CTkLabel(group5, text=field_labels[4])
label5.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
entry5 = CTkEntry(group5, textvariable=entry_variables[4])
entry5.insert(0, f"{field_labels[4]} goes here")
entry5.configure(font=('HP Simplified', 10, "italic"))
entry5.pack(padx=5, pady=5, fill=tk.X, expand=True)
entry5.bind('<FocusIn>', lambda event, entry=entry5, default_text=f"{field_labels[4]} goes here": on_entry_click(entry, default_text))
entry5.bind('<Key>', lambda event, entry=entry5, default_text=f"{field_labels[4]} goes here": on_entry_typing(event, entry, default_text))
entry5.bind('<FocusOut>', lambda event, entry=entry5, default_text=f"{field_labels[4]} goes here": on_focus_out(entry, default_text))

# Payment Mode field
group6 = ctk.CTkFrame(left_half_canvas)
group6.pack(padx=6, pady=6, fill=tk.X, expand=True)
label6 = CTkLabel(group6, text=field_labels[5])
label6.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
entry6 = CTkEntry(group6, textvariable=entry_variables[5])
entry6.insert(0, f"{field_labels[5]} goes here")
entry6.configure(font=('HP Simplified', 10, "italic"))
entry6.pack(padx=5, pady=5, fill=tk.X, expand=True)
entry6.bind('<FocusIn>', lambda event, entry=entry6, default_text=f"{field_labels[5]} goes here": on_entry_click(entry, default_text))
entry6.bind('<Key>', lambda event, entry=entry6, default_text=f"{field_labels[5]} goes here": on_entry_typing(event, entry, default_text))
entry6.bind('<FocusOut>', lambda event, entry=entry6, default_text=f"{field_labels[5]} goes here": on_focus_out(entry, default_text))

# Creating Checkbox
checkvalue = tk.IntVar()
checkbtn = CTkCheckBox(left_half_canvas, text="Remember me?", variable=checkvalue)
checkbtn.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

# Submit button
submit_button = CTkButton(left_half_canvas, text="Submit", command=getvals, state="disabled")
submit_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

# Binding to check fields when any entry is updated
for entry in entry_variables:
    entry.trace_add('write', lambda *args: check_fields())

# Creating a list of all CTkEntry widgets
entries = [entry for group in [group1, group2, group3, group4, group5, group6] for entry in group.winfo_children() if isinstance(entry, CTkEntry)]

left_half_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Call the check_fields function initially
check_fields()

root.mainloop()
