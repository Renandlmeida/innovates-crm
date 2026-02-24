# 🚀 Innovates CRM

A lightweight Customer Relationship Management (CRM) system built with Django.

Innovates CRM was developed to simulate a real-world business environment, focusing on lead management, sales pipeline tracking and revenue potential analysis.

---

## 🌟 Features

- 🔐 Secure user authentication (Login / Logout)
- 📋 Full Client CRUD (Create, Read, Update, Delete)
- 🔎 Search by name, email or phone
- 🎯 Status filtering (New, In Progress, Won, Lost)
- 💰 Automatic potential revenue calculation
- 📊 Dashboard with summary metrics
- ⚠ Basic error handling
- 🎨 Responsive UI built with Bootstrap

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
  <img src="https://github.com/Renandlmeida/innovates-crm/blob/main/images/teladelogin.png?raw=1" width="70%">
</p>

---

### 📋 Client List
<p align="center">
  <img src="https://github.com/Renandlmeida/innovates-crm/blob/main/images/listadeclientes.png?raw=1" width="85%">
</p>

---

### ➕ Add New Client
<p align="center">
  <img src="https://github.com/Renandlmeida/innovates-crm/blob/main/images/adicionandonovocliente.png?raw=1" width="85%">
</p>

---

### 💰 Client Table with Revenue Calculation
<p align="center">
  <img src="https://github.com/Renandlmeida/innovates-crm/blob/main/images/tabelacomvalorpontencial.png?raw=1" width="85%">
</p>

---

### ⚠ Error Handling Example
<p align="center">
  <img src="https://github.com/Renandlmeida/innovates-crm/blob/main/images/tratamentoDeErro.png?raw=1" width="85%">
</p>

---

## ⚙ Installation

```bash
git clone https://github.com/Renandlmeida/innovates-crm.git
cd innovates-crm

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver