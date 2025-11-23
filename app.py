import json
import os
import time
from datetime import datetime

NOTES_FILE = "notes.json"
TASKS_FILE = "tasks.json"


#Helper functins for storage

def load_json(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_json(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Could not save file:", filename, e)


# Notes functions

def add_note():
    title = input("Enter note title: ").strip()
    if title == "":
        print("Title cannot be empty.")
        return
    body = input("Enter note body: ").strip()
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes = load_json(NOTES_FILE)
    note = {"id": int(time.time()), "title": title, "body": body, "created": created}
    notes.append(note)
    save_json(NOTES_FILE, notes)
    print("Note added successfully")

def view_notes():
    notes = load_json(NOTES_FILE)
    if not notes:
        print("No notes found.")
        return
    print("\n-- Your Notes --")
    for n in notes:
        print(f"ID: {n['id']} | {n['title']} ({n['created']})")
        print(f"  {n['body']}\n")
    print("------------------")

def search_notes():
    key = input("Enter keyword to search in title/body: ").strip().lower()
    if key == "":
        print("Empty keyword")
        return
    notes = load_json(NOTES_FILE)
    found = []
    for n in notes:
        if key in n['title'].lower() or key in n['body'].lower():
            found.append(n)
    if not found:
        print("No notes matched.")
        return
    print("\n--- Search Results ---")
    for n in found:
        print(f"ID: {n['id']} | {n['title']} ({n['created']})")
        print(f"  {n['body']}\n")
    print("---------------------")

def delete_note():
    view_notes()
    nid = input("Enter ID of note to delete: ").strip()
    if nid == "":
        print("No ID entered")
        return
    notes = load_json(NOTES_FILE)
    new = [n for n in notes if str(n['id']) != nid]
    if len(new) == len(notes):
        print("No note with that ID")
    else:
        save_json(NOTES_FILE, new)
        print("Note deleted")


# Tasks functions

def add_task():
    title = input("Enter task title: ").strip()
    if title == "":
        print("Title cannot be empty.")
        return
    due = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
   
    if due:
        try:
            datetime.strptime(due, "%Y-%m-%d")
        except:
            print("Invalid date format, leaving due date empty.")
            due = ""
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks = load_json(TASKS_FILE)
    task = {"id": int(time.time()), "title": title, "due": due, "done": False, "created": created}
    tasks.append(task)
    save_json(TASKS_FILE, tasks)
    print("Task added successfully")

def view_tasks(show_all=True):
    tasks = load_json(TASKS_FILE)
    if not tasks:
        print("No tasks found.")
        return
    print("\n---- Your Tasks ----")
    for t in tasks:
        status = "Done" if t.get("done") else "Pendng"
        if show_all or not t.get("done"):
            print(f"ID: {t['id']} | {t['title']} | Due: {t.get('due','-')} | {status}")
    print("--------------------")

def mark_task_done():
    view_tasks(show_all=True)
    tid = input("Enter ID of task to mark as done: ").strip()
    if tid == "":
        print("No ID entered.")
        return
    tasks = load_json(TASKS_FILE)
    found = False
    for t in tasks:
        if str(t['id']) == tid:
            t['done'] = True
            found = True
            break
    if not found:
        print("No task with that ID.")
    else:
        save_json(TASKS_FILE, tasks)
        print("Task marked as done.")

def delete_task():
    view_tasks(show_all=True)
    tid = input("Enter ID of task to delete: ").strip()
    if tid == "":
        print("No ID entered.")
        return
    tasks = load_json(TASKS_FILE)
    new = [t for t in tasks if str(t['id']) != tid]
    if len(new) == len(tasks):
        print("No task with that ID.")
    else:
        save_json(TASKS_FILE, new)
        print("Task deleted.")

# -----------------------------
# Simple reports / utils
# -----------------------------
def show_summary():
    notes = load_json(NOTES_FILE)
    tasks = load_json(TASKS_FILE)
    pending = len([t for t in tasks if not t.get("done")])
    done = len([t for t in tasks if t.get("done")])
    print("\n======= SUMMARY ========")
    print(f"Total Notes: {len(notes)}")
    print(f"Total Tasks: {len(tasks)} (Pending: {pending}, Done: {done})")
    print("=========================\n")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Menu

def notes_menu():
    while True:
        print("\n--- NOTES MENU ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def tasks_menu():
    while True:
        print("\n--- TASKS MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("5. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("\n================ COLLEGE HELPER ================")
        print("1. Notes")
        print("2. Tasks")
        print("3. Summary")
        print("4. Clear Screen")
        print("5. Exit")
        print("===============================================")
        choice = input("Enter option: ").strip()
        if choice == "1":
            notes_menu()
        elif choice == "2":
            tasks_menu()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            clear_screen()
        elif choice == "5":
            print("Good luck with your studies! Bye.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()

