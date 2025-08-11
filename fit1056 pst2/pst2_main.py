# pst2_main.py - The Persistent Application

import json
import datetime

DATA_FILE = "msms.json"
app_data = {} # This global dictionary will hold ALL our data.

# --- Core Persistence Engine ---
def load_data(path=DATA_FILE):
    """
    Loads all application data from a JSON file.
    Returns:
        None
    """
    global app_data
    try:
        with open(path, 'r') as f:
            app_data = json.load(f)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("Data file not found. Initializing with default structure.")
        app_data = {
            "students": [],
            "teachers": [],
            "attendance": [],
            "next_student_id": 1,
            "next_teacher_id": 1
        }

def save_data(path=DATA_FILE):
    """
    Saves all application data to a JSON file.
    Returns:
        None
    """
    with open(path, 'w') as f:
        json.dump(app_data, f, indent=4)
    print("Data saved successfully.")


# --- Full CRUD for Core Data ---
# Note: We are now working with lists of dictionaries, not lists of objects.

def add_teacher(name, speciality):
    """
    Adds a teacher dictionary to the data store.
    Returns:
        None
    """
    teacher_id = app_data['next_teacher_id']
    new_teacher = {"id": teacher_id, "name": name, "speciality": speciality}
    app_data['teachers'].append(new_teacher)
    app_data['next_teacher_id'] += 1
    print(f"Core: Teacher '{name}' added.")

def update_teacher(teacher_id, **fields):
    """
    Finds a teacher by ID and updates their data with provided fields.
    Returns:
        None
    """
    for teacher in app_data['teachers']:
        if teacher['id'] == teacher_id:
            teacher.update(fields)
            print(f"Teacher {teacher_id} updated.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")

def remove_student(student_id):
    """
    Removes a student from the data store.
    Returns:
        None
    """
    for student in app_data['students']:
        # If found, use the .remove() method on the list to delete it.
        if student['id'] == student_id:
            # A list comprehension is a clean way to do this:
            app_data['students'].remove(student)
            print(f"student {student['id']} has been removed.")
            return
    # app_data['students'] = [s for s in app_data['students'] if s['id'] != student_id]
    print(f"student {student_id} hasn't been found.")
    
    
def remove_teacher(teacher_id):
    """
    Removes a teacher from the data store.
    Returns:
        None
    """
    for teacher in app_data['teachers']:
        if teacher['id'] == teacher_id:
            app_data['teachers'].remove(teacher)
            print(f"teacher {teacher['id']} has been removed.")
            return
    print(f"teacher {teacher_id} hasn't been found.")

def update_student(student_id, **fields):
    """
    Finds a student by ID and updates their data with provided fields.
    Returns:
        None
    """
    for student in app_data['students']:
        if student['id'] == student_id:
            student.update(fields)
            print(f"student {student_id} updated.")
            return
    print(f"Error: student with ID {student_id} not found.")


# --- New Receptionist Features ---
def check_in(student_id, course_id, timestamp=None):
    """
    Records a student's attendance for a course.
    Returns:
        None
    """
    if timestamp is None:
        timestamp = datetime.datetime.now().isoformat()
    
    # It should contain 'student_id', 'course_id', and 'timestamp'.
    check_in_record = {
        "student_id": student_id,
        "course_id": course_id,
        "timestamp": timestamp
    }
    app_data['attendance'].append(check_in_record)
    print(f"Receptionist: Student {student_id} checked into {course_id}.")

def print_student_card(student_id):
    """
    Creates a text file badge for a student.
    Returns:
        None
    """
    student_to_print = None
    for s in app_data['students']:
        if s['id'] == student_id:
            student_to_print = s
            break
    
    if student_to_print:
        filename = f"{student_id}_card.txt"
        with open(filename, 'w') as f:
            # Write the student's details to the file in a nice format.
            f.write("========================\n")
            f.write(f"  MUSIC SCHOOL ID BADGE\n")
            f.write("========================\n")
            f.write(f"ID: {student_to_print['id']}\n")
            f.write(f"Name: {student_to_print['name']}\n")
            f.write(f"Enrolled In: {', '.join(student_to_print.get('enrolled_in', []))}\n")
        print(f"Printed student card to {filename}.")
    else:
        print(f"Error: Could not print card, student {student_id} not found.")


# --- Main Application Loop ---
def main():
    """
    Console menu loop.
    Loads data on start; after any mutating action, saves immediately; saves again on exit.
    """
    load_data() # Load all data from file at startup.

    while True:
        print("\n===== MSMS v2 (Persistent) =====")
        print("1. Check-in Student")
        print("2. Print Student Card")
        print("3. Update Teacher Info")
        print("4. Remove Student")
        print("q. Quit and Save")
        
        choice = input("Enter your choice: ")
        
        made_change = False # A flag to track if we need to save
        if choice == '1':
            student_id = int(input("Enter Student ID: "))
            course_id = input("Enter Course ID: ")
            check_in(student_id, course_id)            
            made_change = True
        elif choice == '2':
            student_id = int(input("Enter Student ID: "))
            print_student_card(student_id)            
        elif choice == '3':
            teacher_id = int(input("Enter Teacher ID: "))
            field = input("Field to update (name or speciality): ")
            value = input("Enter new value: ")
            update_teacher(teacher_id, **{field: value})            
            # Example: update_teacher(1, speciality="Advanced Piano")
            made_change = True
        elif choice == '4':
            student_id = int(input("Enter Student ID to remove: "))
            remove_student(student_id)            
            made_change = True
        elif choice.lower() == 'q':
            print("Saving final changes and exiting.")
            break
        else:
            print("Invalid choice.")
            
        if made_change:
            save_data() # Save the data immediately after any change.

    save_data() # One final save on exit.

# --- Program Start ---
if __name__ == "__main__":
    main()

