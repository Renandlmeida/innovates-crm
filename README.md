# 🚀 Innovates CRM

A lightweight Customer Relationship Management (CRM) system built with Django.

Innovates CRM simulates a real-world business environment, focusing on lead management, pipeline tracking and revenue analysis.

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
  <img src="https://github.com/Renandlmeida/innovates-crm/blob/main/images/login.png?raw=1" width="70%">
</p>

---

### 📋 Client Management
<p align="center">
  <img src="https://github.com/Renandlmeida/innovates-crm/blob/main/images/clients.png?raw=1" width="85%">
</p>

---

### ➕ Create Client
<p align="center">
  <img src="https://github.com/Renandlmeida/innovates-crm/blob/main/images/new-client.png?raw=1" width="85%">
</p>

---

### 📊 Dashboard
<p align="center">
  <img src="https://github.com/Renandlmeida/innovates-crm/blob/main/images/dashboard.png?raw=1" width="85%">
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