# 💰 Expense Tracker (Flask + MySQL)

🚀 **Live Demo:** https://expense-tracker-bhushan-bhabal.up.railway.app/

A full-stack Expense Management Web Application built using Flask and MySQL.
Users can add, edit, delete, and analyze expenses with category-wise insights and time-based summaries.

⚠️ **Note:** This is a demo project. Data may reset anytime.

---

## 🚀 Features

* Add, Edit, Delete Expenses
* Category-based expense tracking
* Daily, Monthly, Yearly summaries
* Total expense calculation
* Clean and responsive UI
* Flash messages for user feedback
* MySQL database integration
* Deployed on Railway

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Flask (Python)
* **Database:** MySQL
* **Deployment:** Railway
* **Version Control:** Git & GitHub

---

## 📊 Screens

* Dashboard (All Expenses)
* Add Expense
* Edit Expense
* Summary Page (Today, Month, Year + Category)

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/bhushan-bhabal/expense-tracker.git
cd expense-tracker
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup MySQL database

Create database:

```sql
CREATE DATABASE expense_tracker;
```

Import schema:

```sql
source schema.sql;
```

### 5️⃣ Configure DB connection

Update `db.py`:

```python
host = "localhost"
user = "root"
password = ""
database = "expense_tracker"
```

### 6️⃣ Run the app

```bash
python app.py
```

---

## 🌐 Deployment

This project is deployed using **Railway**:

* Backend hosted on Railway
* MySQL database hosted on Railway

### Environment Variables

```env
MYSQLHOST=
MYSQLUSER=
MYSQLPASSWORD=
MYSQLDATABASE=
MYSQLPORT=
SECRET_KEY=
```

---

## 🔐 Security Notes

* Sensitive data (DB credentials, secret keys) are stored in environment variables
* `.env` file is NOT pushed to GitHub
* Uses parameterized queries to prevent SQL Injection

---

## 📈 Future Improvements

* User Authentication (Login/Register)
* Expense charts (graphs)
* API version (REST API)
* Pagination & filters
* Export to CSV
