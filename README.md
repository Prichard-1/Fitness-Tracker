
# 🏋️‍♂️ Fitness Tracker API

A RESTful backend service built with Django and Django REST Framework (DRF) that allows users to log, manage, and analyze their fitness activities securely.

## 📌 Project Overview

This API enables:
- User registration and authentication
- CRUD operations for fitness activities
- Activity history filtering and sorting
- Metrics aggregation (duration, distance, calories)
- Secure access via JWT tokens

---

## 🚀 Features

### 👤 User Management
- Register, login, and manage user accounts
- JWT-based authentication
- Users can only access their own data

### 📝 Activity Management
- Create, Read, Update, Delete fitness activities
- Fields: `activity_type`, `duration`, `distance`, `calories_burned`, `date`, `user`

### 📅 Activity History
- Filter by date range or activity type
- Sort by date, duration, or calories burned
- Paginated results

### 📊 Activity Metrics
- Summary of total duration, distance, and calories
- Optional: Weekly/monthly trends

---

## 🧱 Tech Stack

| Layer         | Technology                     |
|---------------|--------------------------------|
| Backend       | Django, Django REST Framework  |
| Auth          | Django Auth + JWT (SimpleJWT)  |
| Database      | SQLite (dev), PostgreSQL (prod)|
| Deployment    | Heroku / PythonAnywhere        |
| API Format    | RESTful JSON                   |

---

## 🔐 Authentication

JWT-based authentication using `djangorestframework-simplejwt`.

| Endpoint              | Description                      |
|-----------------------|----------------------------------|
| `/api/token/`         | Obtain access and refresh tokens |
| `/api/token/refresh/` | Refresh access token             |

All activity endpoints require authentication.

---

## 📦 API Endpoints

### Users

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | `/api/users/`     | Register new user        |
| GET    | `/api/users/me/`  | Get current user profile |
| PUT    | `/api/users/me/`  | Update profile           |

### Activities

| Method | Endpoint              | Description                      |
|--------|-----------------------|----------------------------------|
| GET    | `/api/activities/`     | List user activities             |
| POST   | `/api/activities/`     | Create new activity              |
| GET    | `/api/activities/<id>/`| Retrieve activity details        |
| PUT    | `/api/activities/<id>/`| Update activity                  |
| DELETE | `/api/activities/<id>/`| Delete activity                  |

### Metrics

| Method | Endpoint              | Description                      |
|--------|-----------------------|----------------------------------|
| GET    | `/api/metrics/`        | Summary of user activity metrics|

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Prichard-1/fitness-tracker.git
cd fitness-tracker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver

