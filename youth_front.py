import tkinter as tk
from tkinter import messagebox
from build_dictionary import builder
from job import Job

# --- Load job data ---
jobs_list = builder()
master_list = []

for job in jobs_list:
    temp = Job(job["company"], job["title"], job["age_min"], job["interest"],
               job["location"], job["pay"], job["contact"])
    master_list.append(temp)

user_interest = []


# --- Main search function ---
def search(retail_var, food_var, tech_var, labor_var, service_var, warehouse_var):
    age_str = age_entry.get()

    # Check if age is a number
    try:
        age = int(age_str)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for age.")
        return

    # Too young to work
    if age < 14:
        messagebox.showwarning("Age Restriction", "You are ineligible to work at this age.")
        result_box.delete("1.0", "end")
        return

    # Collect interests
    global user_interest
    user_interest = []
    if retail_var.get() == 1: user_interest.append("retail")
    if food_var.get() == 1: user_interest.append("food")
    if tech_var.get() == 1: user_interest.append("tech")
    if labor_var.get() == 1: user_interest.append("labor")
    if service_var.get() == 1: user_interest.append("service")
    if warehouse_var.get() == 1: user_interest.append("warehouse")

    # Filter jobs
    rec_jobs = []
    for interest in user_interest:
        for job in master_list:
            if interest in job.interest and age >= job.age_min:
                rec_jobs.append(job)

    # Show results
    result_box.delete("1.0", "end")
    if not rec_jobs:
        result_box.insert("1.0", "No jobs found for your age and interests.")
    else:
        for job in rec_jobs:
            result_box.insert("end", str(job) + "\n")


# --- GUI setup ---
root = tk.Tk()
root.title("Youth Job Finder")
root.state('zoomed')
root.geometry("500x700")
root.configure(bg="#ff8563")

# Title
tk.Label(root, text="Youth Job Finder", font=("Georgia", 20, "bold"),
         bg="#efcf67").pack(pady=10)

# Logo
img = tk.PhotoImage(file="logo.png")
tk.Label(root, image=img).pack(padx=20, pady=20)

# Age input
tk.Label(root, text="Age (15–17) (18–21):", font=("Georgia", 12),
         bg="#efcf67").pack()
age_entry = tk.Entry(root, font=("Georgia", 11))
age_entry.pack(pady=5)

# Interests
tk.Label(root, text="Select Your Interests:", font=("Georgia", 12),
         bg="#efcf67").pack(pady=5)

# Checkboxes
retail_var = tk.IntVar()
food_var = tk.IntVar()
tech_var = tk.IntVar()
labor_var = tk.IntVar()
service_var = tk.IntVar()
warehouse_var = tk.IntVar()

tk.Checkbutton(root, text="Retail", variable=retail_var, font=("Georgia", 11),
               bg="#efcf67").pack()
tk.Checkbutton(root, text="Food", variable=food_var, font=("Georgia", 11),
               bg="#efcf67").pack()
tk.Checkbutton(root, text="Tech", variable=tech_var, font=("Georgia", 11),
               bg="#efcf67").pack()
tk.Checkbutton(root, text="Labor", variable=labor_var, font=("Georgia", 11),
               bg="#efcf67").pack()
tk.Checkbutton(root, text="Service", variable=service_var, font=("Georgia", 11),
               bg="#efcf67").pack()
tk.Checkbutton(root, text="Warehouse", variable=warehouse_var, font=("Georgia", 11),
               bg="#efcf67").pack()

# Search button
tk.Button(root, text="Search Jobs",
          command=lambda: search(retail_var, food_var, tech_var,
                                 labor_var, service_var, warehouse_var),
          bg="#efcf67", font=("Georgia", 11)).pack(pady=10)

# Results box
result_box = tk.Text(root, width=48, height=15, bd=2, relief="groove",
                     font=("Georgia", 10))
result_box.pack(pady=5)

root.mainloop()
