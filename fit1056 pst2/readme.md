# MSMS - Music School Management System (PST2)

## Overview
This is a Python-based Music School Management System, upgraded from PST1.  
In this version, we have added **data persistence** (stored in a JSON file), **full CRUD operations**, and **receptionist features**.

With this system, you can:
- Add, update, and remove students
- Add, update, and remove teachers
- Check-in students for classes
- Print student ID cards (as text files)
- Automatically save and load all data from `msms.json`

All actions are handled via a command-line menu, and any changes are saved immediately.

---

## How to Run
1. Run the program in your terminal:
   ```bash
   python pst2_main.py
   ```
2. Follow the on-screen menu instructions, for example:
   - Enter `1` to add a student
   - Enter `7` to check-in a student
   - Enter `8` to print a student card
3. All changes are automatically saved to `msms.json` and will be loaded the next time you start the program.

---

## GitHub Repo
[Click here to view the repository](https://github.com/Zion904/msms-pst2)

---

## Features by Fragment

### Fragment 2.1 – Core Persistence
- `load_data()`: Loads data at startup; if the file does not exist, initializes a default structure.  
- `save_data()`: Saves all data to `msms.json` in a clean, human-readable format.  

### Fragment 2.2 – CRUD Operations
- **Teachers**: `add_teacher`, `update_teacher`, `remove_teacher`  
- **Students**: `add_student`, `update_student`, `remove_student`  

### Fragment 2.3 – Receptionist Features
- `check_in()`: Records student attendance with timestamp.  
- `print_student_card()`: Generates a student ID card as a text file.  

### Fragment 2.4 – Main Loop
- Loads data on startup.  
- Menu provides access to all CRUD and new features.  
- Saves data immediately after any change.  

---

## Design Notes
- `app_data` is a single global dictionary containing all students, teachers, attendance records, and ID counters.  
- `enrolled_in` is stored as a list for easy extension in the future.  
- Immediate save after any modification ensures no data loss.  
- Code is developed step-by-step following the Fragment structure, with commits for each stage.  