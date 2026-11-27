# 📚  Library Management System

> A menu-driven Python program to manage books, issuing, and inventory with persistent file storage.

---

## 🎯 Objective

The primary objective of the **Library Management System** is to digitize and simplify day-to-day library operations using Python. Specifically, it aims to:
* 📋 Maintain an organized, duplicate-free catalog of books with their author, price, and available copy count.
* 🔄 Automate book issuing and return workflows while keeping real-time stock counts accurate.
* 🧾 Maintain a permanent, append-only transaction log (`IssuanceLog.txt`) of student borrowing and returns.
* 💾 Ensure zero data loss across program restarts by saving all inventory updates to `Library Records.txt`.
* 💰 Provide instant library insights, including complete record views and total inventory valuation in **Rs.**.

---

## 🧠 Python Concepts Used

This project applies core Python programming fundamentals:

* **🗂️ Dictionaries (`dict`):** Used as the main in-memory database, mapping each book title (key) to its **3 fields** (`author`, `price`, and `copies`).
* **📁 File Handling (`open`, read, write, append):**
  * **Read/Write mode:** Loads existing records from `Library Records.txt` at start-up and rewrites updated records after every modification.
  * **Append mode (`'a'`):** Logs every book issue and return into `IssuanceLog.txt` without overwriting past entries.
* **🔁 Loops (`while` & `for`):**
  * A `while` loop powers the continuous menu-driven interface until the user enters `0` to exit.
  * A `for` loop iterates through the dictionary to display all books and calculate the **Total Inventory Value** ($\sum \text{Price} \times \text{Copies}$).
* **🔀 Conditional Statements (`if-elif-else`):** Handles menu routing (`1`–`6`), duplicate title checks, copy availability validation before issuing, and `"Book Not Found"` checks.
* **🔤 String Manipulation (`.lower()`, `.strip()`):** Normalizes book titles to lowercase so searches and duplicate checks remain case-insensitive.
* **🧩 Modular Functions (`def`):** Separates each core feature (Add, Search, Update, Issue, Return, Stats) into clean, reusable blocks of code.

---

## 🚀 Six Core Features

| Option | Feature | Description |
| :---: | :--- | :--- |
| **1** | ➕ **Add Book** | Creates a new record with author, price, and copies. Saves book names in lowercase and rejects duplicate titles. |
| **2** | 🔍 **Search Book** | Performs a case-insensitive title match to display author, price, and copies (prints `Book Not Found` if missing). |
| **3** | ✏️ **Update Book** | Edits the author, price, or copies of an existing book title and saves changes to the file. |
| **4** | 📤 **Issue Book** | Verifies available copies, logs the student's name in `IssuanceLog.txt`, and reduces copies by `1`. |
| **5** | 📥 **Return Book** | Logs the returned book and student's name in `IssuanceLog.txt` and increases copies by `1`. |
| **6** | 📊 **Library Stats** | Displays all stored records and calculates **Total Inventory Value** ($\sum \text{Price} \times \text{Copies}$) in **Rs.**. |

---

## 🗄️ Files Used

1. **`main.py` (Main Program Script)**
   * Contains the core menu-driven `while` loop (`Options 1–6` and `0` to exit) and handles all user interactions.
   * Loads book records into a Python dictionary at start-up, performs CRUD operations (Add, Search, Update), manages book issuing/returns, and calculates the **Total Inventory Value** in **Rs**.

2. **`Library Records.txt` (Inventory Database)**
   * Stores the entire book catalog as a Python dictionary (`{'book_title': {'Author': ..., 'Price': ..., 'Copies': ...}}`).
   * Currently holds sample records for books like *Ramayana*, *Mahabharat*, *Iron Man*, and *Puppy*, and is automatically overwritten after every inventory change so data persists across sessions.

3. **`IssuanceLog.txt` (Transaction Audit Log)**
   * An append-only plain-text log that records every book borrowing and return event.
   * Each line tracks the student's name, the action performed (`issued` or `returned`), and the book title (e.g., `<Student Name> issued <book name>`).
---

## 💻 How To Run

1. Ensure **Python 3.x** is installed on your computer.
2. Clone or download this repository.
3. Open a terminal in the project folder and run:
   ```bash
   python main.py
   ```
4. Follow the on-screen menu prompts (`1`–`6` to perform actions, `0` to exit).

---

## 👥 Team & Mentorship

* **Team Members:**
  * 👨‍💻 **Harshit Kumar**
  * 👩‍💻 **Shalini Baghel**
  * 👨‍💻 **Ronak Kumar**
  
* **Faculty Mentor:**
  * 👨‍🏫 **Himanshu Shrivastava**

---

## 🏁 Conclusion

This project demonstrates how fundamental Python concepts—such as dictionaries, loops, conditional logic, string methods, and file handling—come together to solve real-world record-keeping tasks. By automating inventory updates, preventing duplicate entries, tracking student borrowing logs, and computing total library valuation in Rs., the system provides a reliable foundation for small-scale library operations.

---

## 🙏 Thank You

A heartfelt thank you to our faculty mentor, **Himanshu Shrivastava**, for guiding us throughout this Python project. We also appreciate everyone who took the time to explore our work—**questions and feedback are always welcome!** 😊
