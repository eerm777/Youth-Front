import tkinter as tk
from build_dictionary import builder
from job import Job
jobs_list = builder()
master_list = []
for job in jobs_list:
    temp = Job(job["company"], job["title"], job["age_min"], job["interest"], job["location"], job["pay"], job["contact"])
    master_list.append(temp)

str_rec = ""

    




user_interest = []


def search(retail_var, food_var, tech_var, labor_var, service_var, warehouse_var):
    global user_interest
    user_interest = []
    if retail_var.get() == 1:
        user_interest.append("retail")
    if food_var.get() == 1:
        user_interest.append("food")
    if tech_var.get() == 1:
        user_interest.append("tech")        
    if labor_var.get() == 1:
        user_interest.append("labor")       
    if service_var.get() == 1:
        user_interest.append("service")       
    if warehouse_var.get() == 1:
        user_interest.append("warehouse")

    rec_jobs = []
    for interest in user_interest:
        for job in master_list:
            if interest in job.interest:
                rec_jobs.append(job)

    str_rec = ""
    for job in rec_jobs:
        str_rec += str(job) + "\n"

    global result_box
    result_box.delete("1.0", "end")
    result_box.insert("1.0", str_rec)
            
    


root = tk.Tk()
root.title("Youth Job Finder")
root.geometry("420x560")

# blue background
root.configure(bg="#87a8ff")

# title
title_label = tk.Label(
    root,
    text="Youth Job Finder",
    font=("Georgia", 20, "bold"),
    bg="#87a8ff"
)
title_label.pack(pady=10)

# age input
tk.Label(root, text="Age (15–17) (18-21):", font=("Georgia", 12), bg="#87a8ff").pack()
age_entry = tk.Entry(root, font=("Georgia", 11))
age_entry.pack(pady=5)

# interest label
tk.Label(
    root,
    text="Select Your Interests:",
    font=("Georgia", 12),
    bg="#87a8ff"
).pack(pady=5)

# checkbox variables
retail_var = tk.IntVar()
food_var = tk.IntVar()
tech_var = tk.IntVar()
labor_var = tk.IntVar()
service_var = tk.IntVar()
warehouse_var = tk.IntVar()

# checkboxes
tk.Checkbutton(root, text="Retail", variable=retail_var, font=("Georgia", 11), bg="#87a8ff").pack()
tk.Checkbutton(root, text="Food", variable=food_var, font=("Georgia", 11), bg="#87a8ff").pack()
tk.Checkbutton(root, text="Tech", variable=tech_var, font=("Georgia", 11), bg="#87a8ff").pack()
tk.Checkbutton(root, text="Labor", variable=labor_var, font=("Georgia", 11), bg="#87a8ff").pack()
tk.Checkbutton(root, text="Service", variable=service_var, font=("Georgia", 11), bg="#87a8ff").pack()
tk.Checkbutton(root, text="Warehouse", variable=warehouse_var, font=("Georgia", 11), bg="#87a8ff").pack()

# search button
tk.Button(
    root,
    text="Search Jobs",
    command=lambda: search(retail_var, food_var, tech_var, labor_var, service_var, warehouse_var),
    bg="#d0d0d0",
    font=("Georgia", 11)
).pack(pady=10)

# results box
result_box = tk.Text(
    root,
    width=48,
    height=20,
    bd=2,
    relief="groove",
    font=("Georgia", 10)
)
result_box.pack(pady=5)

root.mainloop()
