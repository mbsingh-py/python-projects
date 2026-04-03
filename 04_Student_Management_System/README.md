# 🎓 Student Management System (CLI)

A command-line based Student Management System built using Python.
This project allows users to manage student records efficiently with basic CRUD operations and file handling.

---

## 🚀 Features

* ➕ Add Student
* 📋 View All Students
* 🔍 Search Student (by Roll, Name, Marks)
* ✏️ Update Student Marks
* ❌ Delete Student (with confirmation)
* 💾 Persistent data storage using file handling

---

## 🛠️ Tech Stack

* Python (Core)
* File Handling (`.txt`)
* CLI (Command Line Interface)

---

## 📂 Project Structure

```
04_student_management_system/
│── main.py
│── data.txt
│── README.md
```

---

## ▶️ How to Run

1. Make sure Python is installed
2. Run the program:

```
python main.py
```

---

## 📌 How It Works

* Student data is stored in a text file (`data.txt`)
* Each record is saved in this format:

```
roll,name,marks
```

Example:

```
101,Ram,85
102,Shyam,78
```

* Data is loaded when the program starts
* Any changes (add/update/delete) are saved immediately

---

## ⚠️ Notes

* Roll number must be unique
* Only valid numeric input is accepted for roll and marks
* Name accepts alphabets and spaces only
* Empty or corrupted file lines are ignored safely

---

## 🎯 Learning Outcomes

This project demonstrates:

* Structured programming using functions
* Input validation techniques
* File handling (read/write)
* CRUD operations (Create, Read, Update, Delete)
* Basic system design thinking

---

## 🚀 Future Improvements

* Grade calculation system
* Sorting and filtering options
* GUI version (Tkinter)
* Web-based version (HTML/CSS/JS + Backend)

---

## 👤 Author

Developed as part of a Python learning journey focused on building real-world projects.

---
