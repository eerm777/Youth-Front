import tkinter as tk

# simple front-end only version (no backend at all)

def search():
    # button does nothing on purpose
    pass

root = tk.Tk()
root.title("Youth Job Finder")
root.geometry("420x520")

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
tk.Label(root, text="Age (15–21):", font=("Georgia", 12), bg="#87a8ff").pack()
age_entry = tk.Entry(root, font=("Georgia", 11))
age_entry.pack(pady=5)

# interest input
tk.Label(
    root,
    text="Interest (retail, food, tech, etc):",
    font=("Georgia", 12),
    bg="#87a8ff"
).pack()
interest_entry = tk.Entry(root, font=("Georgia", 11))
interest_entry.pack(pady=5)

# search button (does nothing)
tk.Button(
    root,
    text="Search Jobs",
    command=search,
    bg="#d0d0d0",
    font=("Georgia", 11)
).pack(pady=10)

# results box (empty forever)
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
