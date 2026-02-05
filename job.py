class Job:
    # The Constructor (__init__)
    def __init__(self,company, title, age_min, interest, location, pay, contact):
        self.company = company      # Attribute
        self.title = title    # Attribute
        self.age_min = age_min      # Attribute
        self.interest = interest     # Default Attribute
        self.location = location
        self.pay = pay
        self.contact = contact



    def __str__(self):
        return f"Company: {self.company}, Tittle: {self.title}"
#job1 = Job("Target", "Cashier", 18, ["retail", "money"], "Phily", 15, "www.target.com")
#print(job1.company)
#print(job1.title)
#print(job1.age_min)
