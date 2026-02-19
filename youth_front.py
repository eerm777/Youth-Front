import tkinter as tk
from tkinter import messagebox
from build_dictionary import builder
from job import Job

# --- Data Setup ---
jobs_list = builder()
master_list = []
for job in jobs_list:
    temp = Job(job["company"], job["title"], job["age_min"], job["interest"], job["location"], job["pay"], job["contact"])
    master_list.append(temp)

user_interest = []

# --- Logic ---
def search(retail_var, food_var, tech_var, labor_var, service_var, warehouse_var):
    age_str = age_entry.get()
    
    # 1. Check if the input is a valid number
    try:
        age = int(age_str)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid entry! Please enter a number for your age.")
        return

    # 2. Check if the user is younger than 14
    if age < 14:
        messagebox.showwarning("Age Restriction", "You are ineligible to work at this age.")
        result_box.delete("1.0", "end") # Clear the box
        return # Stop the function here so no jobs are shown

    # 3. Process Interests
    global user_interest
    user_interest = []
    if retail_var.get() == 1: user_interest.append("retail")
    if food_var.get() == 1: user_interest.append("food")
    if tech_var.get() == 1: user_interest.append("tech")        
    if labor_var.get() == 1: user_interest.append("labor")       
    if service_var.get() == 1: user_interest.append("service")       
    if warehouse_var.get() == 1: user_interest.append("warehouse")

    # 4. Filter Jobs
    rec_jobs = []
    for interest in user_interest:
        for job in master_list:
            # Check if interest matches AND user is old enough for THIS specific job
            if interest in job.interest and age >= job.age_min:
                rec_jobs.append(job)

    # 5. Display Results
    str_rec = ""
    for job in rec_jobs:
        str_rec += str(job) + "\n"

    result_box.delete("1.0", "end")
    if str_rec == "":
        result_box.insert("1.0", "No jobs found for your age and interests.")
    else:
        result_box.insert("1.0", str_rec)

# --- GUI Setup ---
root = tk.Tk()
root.title("Youth Job Finder")
root.geometry("420x600")
root.configure(bg="#a0a0a0")

# Title
tk.Label(root, text="Youth Job Finder", font=("Georgia", 20, "bold"), bg="#d0d0d0").pack(pady=10)

# Age Input
tk.Label(root, text="Age (15–17) (18-21):", font=("Georgia", 12), bg="#d0d0d0").pack()
age_entry = tk.Entry(root, font=("Georgia", 11))
age_entry.pack(pady=5)

# Interest Label
tk.Label(root, text="Select Your Interests:", font=("Georgia", 12), bg="#d0d0d0").pack(pady=5)

# Checkbox variables
retail_var, food_var, tech_var = tk.IntVar(), tk.IntVar(), tk.IntVar()
labor_var, service_var, warehouse_var = tk.IntVar(), tk.IntVar(), tk.IntVar()

# Checkboxes
tk.Checkbutton(root, text="Retail", variable=retail_var, font=("Georgia", 11), bg="#d0d0d0").pack()
tk.Checkbutton(root, text="Food", variable=food_var, font=("Georgia", 11), bg="#d0d0d0").pack()
tk.Checkbutton(root, text="Tech", variable=tech_var, font=("Georgia", 11), bg="#d0d0d0").pack()
tk.Checkbutton(root, text="Labor", variable=labor_var, font=("Georgia", 11), bg="#d0d0d0").pack()
tk.Checkbutton(root, text="Service", variable=service_var, font=("Georgia", 11), bg="#d0d0d0").pack()
tk.Checkbutton(root, text="Warehouse", variable=warehouse_var, font=("Georgia", 11), bg="#d0d0d0").pack()

# Search Button
tk.Button(
    root, 
    text="Search Jobs", 
    command=lambda: search(retail_var, food_var, tech_var, labor_var, service_var, warehouse_var),
    bg="#d0d0d0", 
    font=("Georgia", 11)
).pack(pady=10)

# Results Box
result_box = tk.Text(root, width=48, height=15, bd=2, relief="groove", font=("Georgia", 10))
result_box.pack(pady=5)

root.mainloop()
