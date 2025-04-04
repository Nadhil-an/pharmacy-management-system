# 💊 Pharmacy Management System (PMS) - Python + SQLite

📌 Description
------------------------------------------------------------------------------------------------------------------
A command-line based Pharmacy Management System built with Python and SQLite.  
It allows pharmacy administrators to securely manage medicine inventory including adding, updating, deleting, and searching medicine details.  
User authentication is also implemented using password hashing for secure login and signup.

🛠 Features
-----------------------------------------------------------------------------------------------------------------
- 🔐 User Signup & Login System (with password hashing using SHA-256)
- 📦 Add New Medicines to the Inventory
- 📝 Update Existing Medicine Details
- 🔍 Search Medicines by:
  - Name
  - Manufacturer
  - Price Range
  - Stock Limit
  - Expiry Date
- 📃 View All Medicines
- ❌ Delete Medicine Entry

📦 Requirements
------------------------------------------------------------------------------------------------------------------
- Python 3.x
- SQLite3 (Python’s built-in library)

🚀 How to Run
------------------------------------------------------------------------------------------------------------------
# Clone the repo
git clone https://github.com/your-username/pharmacy-management.git

# Navigate to project folder
cd pharmacy-management

# Run the script
python main.py

🧪 Usage
--------------------------------------------------------------------------------------------------------------------
After running:

Choose Signup (1) to register.
https://github.com/Nadhil-an/pharmacy-management-system/blob/main/1.png

Choose Login (2) to access the inventory system.
https://github.com/Nadhil-an/pharmacy-management-system/blob/main/2.png
https://github.com/Nadhil-an/pharmacy-management-system/blob/main/3.png

Navigate through the menu to manage medicine records.

Choose Logout (3) to exit the authentication system.

🔒 Security
------------------------------------------------------------------------------------------------------------------
User passwords are stored as hashed values (SHA-256) — not in plain text.

SQLite parameterized queries are used to prevent SQL injection.










