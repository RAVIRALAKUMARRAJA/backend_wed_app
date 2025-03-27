# backend_wed_app
Project Overview

This project is a Django-based web application that includes a REST API built with Django REST Framework (DRF). The application has two main components:

Admin Facing: Where admins can add Android apps, assign points for downloading them, and manage user submissions.

User Facing: Where users can view available apps, earn points for completing tasks, and upload screenshots for verification.

Features

Admin Panel

Custom Admin Panel (Not Django Admin)

Add & Manage Android Apps with categories

Assign points for app downloads

View and verify user submissions

User Dashboard

Signup/Login (JWT Authentication / Django-Allauth)

View Profile Information (Name, Points Earned, Completed Tasks)

List of available apps & their assigned points

Upload screenshots for task completion (Drag-and-Drop feature)

Technology Stack

Backend: Django, Django REST Framework (DRF)

Frontend: HTML, CSS, Bootstrap

Database: MySQL

Authentication: JWT / Django-Allauth

API Documentation: Swagger (drf-yasg)

API Endpoints

Authentication

POST /api/auth/signup/ - Register a new user

POST /api/auth/login/ - Login and get a token

POST /api/auth/logout/ - Logout

Admin Actions

POST /api/admin/apps/ - Add a new app

GET /api/admin/apps/ - View all apps

PUT /api/admin/apps/{id}/ - Update an app

DELETE /api/admin/apps/{id}/ - Delete an app

GET /api/admin/submissions/ - View user submissions

POST /api/admin/verify_submission/ - Verify user submission

User Actions

GET /api/user/profile/ - View user profile

GET /api/user/apps/ - List all available apps

POST /api/user/upload_screenshot/ - Upload screenshot for verification

Installation & Setup

1. Clone the Repository

 git clone https://github.com/your-repo-url.git
 cd your-repo-folder

2. Set Up Virtual Environment

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate    # For Windows

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Database

python manage.py migrate
python manage.py createsuperuser  # Create an admin user

5. Run the Server

python manage.py runserver

6. Access the Application

API Documentation: http://127.0.0.1:8000/swagger/

User Dashboard: http://127.0.0.1:8000/user/

Admin Dashboard: http://127.0.0.1:8000/admin/

Project Structure

backend/
│── backend/                  # Django Project Root
│── adminpanel/               # Admin Panel API
│── tasks/                    # User Tasks API
│── users/                    # User Authentication & Profile
│── templates/                # HTML Templates for User/Admin UI
│   ├── base.html             # Common Base Template
│   ├── admin_dashboard.html  # Admin Panel for Adding Apps
│   ├── user_dashboard.html   # User Dashboard (View Apps, Upload Screenshots)
│   ├── login.html            # User Login Page
│   ├── register.html         # User Signup Page
│── static/                   # CSS, JS, Bootstrap
│   ├── css/                  # Custom Styles
│   │   ├── styles.css
│   ├── js/                   # JavaScript Files
│   ├── images/               # Logo, Icons
│── media/                    # Uploaded Screenshots
│── manage.py                 # Django Command-Line Tool



