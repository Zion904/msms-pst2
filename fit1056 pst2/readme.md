# MSMS - Music School Management System(pst2)

## Overview
This is a basic Python program simulating a music school management system.

It allows users to:
- Check in students to classes
- Print student cards
- Update teacher information
- Remove student records
- Save and load persistent data using JSON

## How to Run
Follow the menu instructions to interact with the system.


the link: https://github.com/Zion904/msms-pst2

# Each fragment function
Fragment 2.1 – Core Persistence
Implements load_data() and save_data() to load and store all program data in msms.json.
If the file does not exist, it creates a default data structure.

Fragment 2.2 – CRUD Operations
Refactors and adds functions for managing teachers and students:
add_teacher, update_teacher, remove_teacher, update_student, remove_student.

Fragment 2.3 – Receptionist Features
Adds check_in() for recording attendance and print_student_card() for generating a student ID card as a text file.

Fragment 2.4 – Main Loop
Creates the main menu, calls all functions from previous fragments, and ensures data is saved after any change.