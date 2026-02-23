# Innovates CRM

Innovates CRM is a lightweight Customer Relationship Management (CRM) system built with Django.  
It was designed to simulate real-world business scenarios such as lead management, pipeline tracking and revenue potential analysis.

---

## 🚀 Features

- User authentication (login & logout)
- Client CRUD (Create, Read, Update, Delete)
- Lead status tracking:
  - New
  - In Progress
  - Won
  - Lost
- Search by name, phone or email
- Filter by status
- Potential revenue calculation
- Dashboard with summary data
- Responsive UI built with Bootstrap

---

## 🛠 Tech Stack

- Python
- Django
- SQLite
- Bootstrap

---

## 📦 Installation

```bash
git clone https://github.com/Renandlmeida/innovates-crm.git
cd innovates-crm

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
acess http://127.0.0.1:8000

## 📸 Screenshots

### Login
![Login](images/login.png)

### Client Management
![Clients](images/clients.png)

### Create Client
![New Client](images/new-client.png)

### Dashboard
![Dashboard](images/dashboard.png)