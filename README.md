#College Helper – Notes & Task Organiser
Project Title

#College Helper – CLI Notes & Task Manager

Overview of the Project

College Helper is a lightweight command-line application designed for students to organise their academic workload efficiently. It enables users to create, view, edit, and delete both notes and tasks from a single interactive terminal menu. The app uses simple file-based storage (like .txt files) to preserve user data across sessions, making it beginner-friendly while providing a complete practical implementation of modular programming.

#Features

No Database Required
All data is stored in simple files, making it portable and easy to run anywhere.

Full CRUD Operations
Users can:
1.Add new tasks and notes

2.View all saved data

3.Update existing entries

4.Delete items permanently

5.Task Status Tracking
Mark tasks as:

Pending

Completed

5.Simple File-Based Persistence
Notes and tasks remain saved even after closing the program.

6.Modular Code Structure
Logic is separated into multiple Python files (modules), improving:

7.Clarity

8.Maintainability

9.Scalability

10.Beginner Friendly
No external libraries or installations needed beyond Python.

3Technologies / Tools Used

Language: Python 3.x

Storage: Text files (such as notes.txt and tasks.txt)

Architecture: Modular programming with multiple .py files

Libraries Used: Only Python standard libraries

Steps to Install & Run the Project
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/college-helper
cd college-helper

2️. Verify Project Files

Make sure the following are present:

app.py

notes.py

tasks.py

utils.py

storage files like:

notes.txt

tasks.txt

(If these files don’t exist, the program will create them automatically on first run.)

3️⃣ Run the Application
python app.py


You will see a menu allowing you to manage notes and tasks interactively.

Instructions for Testing
Test 1 – Adding Data

Select:

1. Add Note

2. Add Task

Add at least:

Two different notes

Two tasks with different titles or priorities

Confirm that the content is saved inside the .txt files.

Test 2 – Viewing Data

Select:

3. View Notes

4. View Tasks

Check that:

All added entries are displayed properly

Task status is shown (e.g., Pending / Completed)

Test 3 – Modify & Delete

Choose:

5. Edit/Delete Notes

6. Edit/Delete Tasks

Perform:

One update (modify content or status)

One delete action

View the lists again using options 3 and 4 to confirm changes are permanent.

