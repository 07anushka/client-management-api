# Client Management API

A production-ready Django REST Framework (DRF) backend for managing clients, packages, subscriptions, payments, projects, and notes. This project includes JWT authentication, PostgreSQL integration, Docker support, Swagger API documentation, and Django Admin.

---

# Project Overview

The Client Management API is a RESTful backend application developed using Django REST Framework. It enables organizations to efficiently manage client information, package subscriptions, payments, projects, and notes through secure APIs.

This project was built as part of a backend assessment and follows REST API best practices.

---

# Features

- JWT Authentication
- User Registration & Login
- Client Management (CRUD)
- Package Management
- Client Package Assignment
- Payment Tracking
- Project Management
- Notes Management
- Dashboard Analytics
- PostgreSQL Database
- Docker Support
- Swagger API Documentation
- Django Admin Panel

---

# Tech Stack

- Python 3.13
- Django 5
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Gunicorn
- drf-spectacular (Swagger/OpenAPI)

---

# Project Structure

```
client-management-api/

├── accounts/
├── clients/
├── config/
├── core/
├── dashboard/
├── notes/
├── packages/
├── payments/
├── projects/
├── subscriptions/

├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── README.md
├── .env.example
├── .gitignore
└── .dockerignore
```

---

# Prerequisites

Before running the project, install:

- Python 3.13+
- PostgreSQL
- Git
- Docker Desktop (Optional)

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/07anushka/client-management-api.git

cd client-management-api
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a file named

```
.env
```

Example:

```env
SECRET_KEY=your-secret-key

DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=client_management
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

---

## 5. Apply Database Migrations

```bash
python manage.py migrate
```

---

## 6. Create Superuser

```bash
python manage.py createsuperuser
```

---

## 7. Run Development Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# Docker Setup

## Build Containers

```bash
docker compose up --build
```

## Start Containers

```bash
docker compose up
```

## Stop Containers

```bash
docker compose down
```

---

# API Documentation

Swagger UI

```
http://localhost:8000/api/docs/
```

OpenAPI Schema

```
http://localhost:8000/api/schema/
```

Django Admin

```
http://localhost:8000/admin/
```

---

# Authentication

This project uses **JWT (JSON Web Token)** Authentication.

Workflow:

1. Register a user

```
POST /api/accounts/register/
```

2. Login

```
POST /api/accounts/login/
```

3. Copy the Access Token

4. Click **Authorize** in Swagger UI

5. Enter

```
Bearer <access_token>
```

Now all protected APIs can be accessed.

---

# Available API Modules

- Accounts
- Clients
- Packages
- Subscriptions
- Payments
- Projects
- Notes
- Dashboard

---

# Database

Database used:

- PostgreSQL

Main Tables:

- Users
- Clients
- Packages
- Client Packages
- Payments
- Projects
- Notes

---

# Docker

The project includes:

- Dockerfile
- Docker Compose
- PostgreSQL Container
- Gunicorn Application Server

Run the complete project using:

```bash
docker compose up --build
```

---

# API Features

- JWT Authentication
- CRUD Operations
- Dashboard Analytics
- Search
- Filtering
- Pagination
- Soft Delete
- Swagger Documentation

---

# Future Improvements

- Email Notifications
- Client Activity Logs
- Role-Based Access Control (RBAC)
- File Upload Support
- Report Generation
- Unit & Integration Tests

---

# Author

**Anushka A Naik**

GitHub:
https://github.com/07anushka

Repository:
https://github.com/07anushka/client-management-api

---

# License

This project was developed as part of a Django REST Framework Backend Assessment for educational and evaluation purposes.
