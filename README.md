# 🚀 Innovates CRM

A lightweight Customer Relationship Management (CRM) system built with Django.

Innovates CRM was designed to simulate real-world business environments, focusing on lead management, sales pipeline tracking and revenue analysis.

---

## 🌟 Features

- 🔐 User Authentication (Login / Logout)
- 📋 Full Client CRUD
- 🔎 Search by name, email or phone
- 🎯 Status filtering (New, In Progress, Won, Lost)
- 💰 Potential revenue calculation
- 📊 Dashboard with summary metrics
- 🎨 Responsive interface built with Bootstrap

---

## 🛠 Tech Stack

- Python
- Django
- SQLite
- Bootstrap

---

## 📸 Screenshots

### 🔐 Login
<p align="center">
  <img src="images/login.png" width="70%">
</p>

---

### 📋 Client Management
<p align="center">
  <img src="images/clients.png" width="85%">
</p>

---

### ➕ Create Client
<p align="center">
  <img src="images/new-client.png" width="85%">
</p>

---

### 📊 Dashboard
<p align="center">
  <img src="images/dashboard.png" width="85%">
</p>

---

## ⚙️ Installation

```bash
git clone https://github.com/Renandlmeida/innovates-crm.git
cd innovates-crm

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver