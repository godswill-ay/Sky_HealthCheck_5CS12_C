# SKY Engineering Health Check System

**Industry Client Project** - Web application developed for SKY's Engineering Department to digitize their "Health Check" technique (based on Spotify's Squad Health Check model).

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## 🎯 Project Overview

- **Client:** SKY Engineering Department
- **Challenge:** Replace manual spreadsheet-based health assessments with a robust web application
- **Solution:** Full-stack Django application supporting multiple user roles and comprehensive team health visualization
- **Team:** 2 developers (collaborative development using Git)

## 🚀 Key Features

### Multi-Role Authentication System
- **Engineers:** Vote on health check cards, view team summaries
- **Team Leaders:** Manage team views, access departmental data
- **Department Leaders:** Department-wide analytics and reporting
- **Senior Managers:** Cross-departmental insights and strategic overview

### Health Assessment System
- **Traffic Light Voting:** Green/Amber/Red health assessments across 10+ health cards
- **Progress Tracking:** Historical data visualization and trend analysis
- **Session Management:** Organized assessment periods with data persistence
- **Team Analytics:** Automated vote aggregation and team health summaries

### Security & Access Control
- **Role-based Permissions:** Granular access control based on organizational hierarchy
- **Secure Authentication:** Django's built-in authentication with profile management
- **Data Privacy:** Individual votes protected, only aggregated data visible to managers

## 🏗 Technical Architecture

### Backend
- **Framework:** Django 5.0 with Python 3
- **Database:** SQLite with complex relational schema
- **Authentication:** Django's built-in user management
- **Data Models:** Department → Team → Engineer hierarchy

### Frontend
- **Templates:** Django templating engine
- **Styling:** Bootstrap 5 for responsive design
- **JavaScript:** Interactive voting interface and form validation
- **UX Design:** Intuitive navigation with role-specific dashboards

### Database Schema
- Departments (1:N) → Teams (1:N) → Engineers
Health Cards ← Votes → Sessions
Users ← Profiles → Roles

## 🛠 Technical Implementation

**Key technical challenges solved:**
- Complex many-to-many relationships between users, teams, and assessment data
- Role-based view rendering with Django's permission system
- Aggregated data visualization without exposing individual votes
- Scalable database design supporting organizational growth

## 🏃‍♂️ Getting Started

### Prerequisites
- Python 3.8+
- Django 5.0
- SQLite (included with Python)

### Installation
```bash
# Clone the repository
git clone https://github.com/godswill-ay/Sky_HealthCheck_5CS12_C.git
cd Sky_HealthCheck_5CS12_C

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
# venv\Scripts\activate   # On Windows

# Install dependencies
pip install django

# Setup database
python manage.py makemigrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Access the Application
- **Main Application:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## 📊 Features Demonstration

### User Roles & Capabilities
- **Self-registration** for all user types
- **Profile management** with secure password changes
- **Session-based voting** on health check cards
- **Progress visualization** over selected time periods
- **Department/team analytics** based on user permissions

### Admin Features
- Add/delete departments, teams, and users
- Manage health check cards and assessment sessions
- System-wide configuration and user role assignment

## 🎓 Academic Context

This project was developed as part of the **Software Development Group Project** module (5COSC021W) at University of Westminster, in collaboration with SKY Engineering Department as the industry client.

**Learning Outcomes Achieved:**
- Industry-standard software development lifecycle
- Team collaboration and version control
- Complex database design and implementation
- User experience design for enterprise applications
- Security considerations for multi-role systems

## 🤝 Contributors

- **Godswill Ayogu** - Database design, core application logic, authentication system
- **Zaamin Qadeer** - Frontend development, UI/UX design, testing implementation

## 📄 License

This project is for academic use only, developed in collaboration with SKY Engineering Department.

---

**Note:** This application represents real-world software development experience, working with an industry client to solve actual business challenges using modern web development technologies.
```
