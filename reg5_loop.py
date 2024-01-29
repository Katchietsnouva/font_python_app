import tkinter as tk
import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkEntry, CTkCheckBox, CTkButton
from PIL import ImageTk, Image
import json

def on_entry_click(entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, tk.END)
        entry.insert(0, '')
        entry.configure(font=('normal', 10))

def on_entry_typing(event, entry, default_text):
    current_text = entry.get()
    if current_text == default_text or current_text == '':
        entry.delete(0, tk.END)
        entry.configure(font=('italic', 10))
    else:
        entry.configure(font=('normal', 14))

def on_focus_out(entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.configure(font=('normal', 10))

def check_fields(*args):
    all_filled = all(entry_var.get() != f"{label} goes here" for entry_var, label in zip(entry_variables, field_labels))
    submit_button.configure(state="normal" if all_filled else "disabled")



def getvals():
    customer_data = {}
    for label, entry_var in zip(field_labels, entry_variables):
        customer_data[label] = entry_var.get()

    with open("customerdb.json", "a") as json_file:
        json.dump(customer_data, json_file)
        json_file.write("\n")  # Add a newline for each entry

    print("Customer data stored in customerdb.json")

    # Clear the entry fields
    for entry_var in entry_variables:
        entry.delete(0, tk.END)


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

groups = [ctk.CTkFrame(left_half_canvas) for _ in range(len(field_labels))]
for i, group in enumerate(groups):
    group.pack(padx=5, pady=2, fill=tk.X, expand=True)

    label = ctk.CTkLabel(group, text=field_labels[i])
    label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

    entry = ctk.CTkEntry(group, textvariable=entry_variables[i])
    entry.insert(0, f"{field_labels[i]} goes here")
    entry.configure(font=('italic', 10))
    entry.pack(padx=5, pady=5, fill=tk.X, expand=True)
    entry.bind('<FocusIn>', lambda event, entry=entry, default_text=f"{field_labels[i]} goes here": on_entry_click(entry, default_text))
    entry.bind('<Key>', lambda event, entry=entry, default_text=f"{field_labels[i]} goes here": on_entry_typing(event, entry, default_text))
    entry.bind('<FocusOut>', lambda event, entry=entry, default_text=f"{field_labels[i]} goes here": on_focus_out(entry, default_text))

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

left_half_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Call the check_fields function initially
check_fields()

root.mainloop()
