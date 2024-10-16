import tkinter as tk
from tkinter import messagebox

print("Program is Running")

def submit_form():
    name = name_entry.get()
    surname = surname_entry.get()
    date_of_birth = dob_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    id_type = id_var.get()
    id_number = id_entry.get()
    fiscal_code = fiscal_code_entry.get()

    # Validate form submission
    if all([name, surname, date_of_birth, email, phone, id_type, id_number, fiscal_code]):
        messagebox.showinfo("Submission Successful", f"SPID for {name} {surname} submitted!")
    else:
        messagebox.showwarning("Incomplete Form", "Please fill in all fields.")


# Create main window
root = tk.Tk()
root.title("SPID Release Form (Italy)")
root.geometry("400x400")

# Create labels and entry fields for the form
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Surname:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
surname_entry = tk.Entry(root)
surname_entry.grid(row=1, column=1)

tk.Label(root, text="Date of Birth (DD/MM/YYYY):").grid(row=2, column=0, padx=10, pady=10, sticky='e')
dob_entry = tk.Entry(root)
dob_entry.grid(row=2, column=1)

tk.Label(root, text="Email:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1)

tk.Label(root, text="Phone Number:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
phone_entry = tk.Entry(root)
phone_entry.grid(row=4, column=1)

# ID Type Dropdown
tk.Label(root, text="ID Type:").grid(row=5, column=0, padx=10, pady=10, sticky='e')
id_var = tk.StringVar(root)
id_var.set("ID Card")  # default value
id_menu = tk.OptionMenu(root, id_var, "ID Card", "Passport", "Driving License")
id_menu.grid(row=5, column=1)

tk.Label(root, text="ID Number:").grid(row=6, column=0, padx=10, pady=10, sticky='e')
id_entry = tk.Entry(root)
id_entry.grid(row=6, column=1)

tk.Label(root, text="Fiscal Code:").grid(row=7, column=0, padx=10, pady=10, sticky='e')
fiscal_code_entry = tk.Entry(root)
fiscal_code_entry.grid(row=7, column=1)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=8, column=0, columnspan=2, pady=20)

root.mainloop()
