class Job:
    """Simple class to store job information."""

    def __init__(self, company, title, age_min, interest, location, pay, contact):
        # Basic job attributes
        self.company = company
        self.title = title
        self.age_min = age_min
        self.interest = interest
        self.location = location
        self.pay = pay
        self.contact = contact

    def __str__(self):
        """Return a formatted string for displaying job info."""
        return (
            f"{self.company} - {self.title}\n"
            f" Location: {self.location}\n"
            f" Pay: {self.pay}\n"
            f" Apply: {self.contact}\n"
            f"--------------------------------"
        )
