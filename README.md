# HealthCheck System

This is a web-based system designed to help manage departments, teams, and users efficiently within an organisation.

---

## Project Features
- User Registration and Login
- Department Management (Search and List Departments)
- Team Management (Search and List Teams)
- User Management (Search and List Users)
- Simple Navigation Bar
- Protected Pages (only logged-in users can access certain pages)
- Footer information about project team
- Responsive and clean design

---

## Technologies Used
- Python 3
- Django 5
- HTML / CSS
- Git and GitHub (Version Control)

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/godswill-ay/Sky_HealthCheck_5CS12_C.git

2.	**Navigate to the Project Directory**
    ```bash
    cd Sky_HealthCheck_5CS12_C

3.	**Create and Activate Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate         # On Mac/Linux
    venv\Scripts\activate            # On Windows

4.	**Install Dependencies**
    ```bash
    pip install django

5.	**Apply Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

6.	**Run the Server**
    ```bash
    python manage.py runserver

7.	**Access the Site**
    ```bash
    Open your browser and visit:
    http://127.0.0.1:8000/

---

## Project Team
- Godswill Ayogu
- Zaamin Qadeer
- Krystian Dolinski
- Fares Bouchair
- Mohammed Shahin

---


## Notes
- Only logged-in users can access Department, Team, and User pages.
- About page is public and does not require login.
- Admin panel available at /admin/ (only for superusers).
- The system is built for local development and academic coursework purposes.

---

## License

- This project is for academic use only.

---
