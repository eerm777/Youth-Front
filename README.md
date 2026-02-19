## What is this?
I created this app to help teenagers in Northeast Philadelphia find jobs that actually fit their age and interests. Instead of scrolling through huge job boards only to find out you're too young to apply, this app filters everything for you based on the legal working age and local business rules.

## Why I built it
Finding a first job is hard. I wanted to make a tool where you can just put in your age, check off what you're into (like Tech or Food), and instantly see who is hiring nearby on Roosevelt Blvd, Bustleton Ave, or in the Northeast area.

## How it Works
The project is split into three main parts:

1.The Database (jobs.txt): A list of local spots like Wawa, Target, and Best Buy with their pay and age requirements.
2.The Logic:
    build_dictionary.py cleans up the text file so the computer can read the data correctly.
    job.py defines a "Job" object to keep track of things like company name, location, and contact info.
3. The App Interface (youth_front.py): A window built with tkinter where you type your age and click search.

## Features

Age Check: If you're under 14, the app lets you know you're not quite old enough to work yet.
Interest Filters: You can search specifically for Retail, Food, Tech, Labor, Service, or Warehouse jobs.
Direct Links: The results show you exactly where to go online to apply for each job.

## Getting Started

To run this project yourself, make sure you have Python installed and follow these steps:

Download all the files into one folder on your computer.

Open your terminal or command prompt.

Navigate to that folder and run:
      Bash
      python youth_front.py
Enter your age, pick your interests, and hit Search Jobs!

## Code & Tools Used

Python: The main programming language.
Tkinter: Used to create the buttons, text boxes, and the main window.
Classes & Objects: I used a Job class to keep the code organized and easy to read.
Note: This was made as a school project to show how coding can solve real problems for students in our community!


Author: [Elnur Ermekov, Isabella Francis, Darya Hramianok]
Location: Philadelphia, PA
    

