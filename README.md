# Client Management API

A production-ready **Django REST Framework (DRF)** backend for managing clients, packages, subscriptions, payments, projects, and notes. The project includes **JWT Authentication**, **PostgreSQL**, **Docker support**, **Swagger/OpenAPI documentation**, and **Django Admin**.

---

# Project Overview

The Client Management API is a RESTful backend application built using Django REST Framework. It enables organizations to manage client records, package subscriptions, payments, projects, and notes through secure REST APIs.

This project was developed as part of a backend assessment and follows REST API best practices.

---

# Features

* JWT Authentication
* User Registration & Login
* Client Management (CRUD)
* Package Management (CRUD)
* Client Package Assignment
* Payment Management
* Project Management
* Notes Management
* Dashboard Analytics
* Search, Filtering & Pagination
* Soft Delete Support
* PostgreSQL Integration
* Docker & Docker Compose Support
* Swagger/OpenAPI Documentation
* Django Admin Panel

---

# Tech Stack

* Python 3.11+ (Tested with Python 3.13)
* Django 5
* Django REST Framework
* PostgreSQL
* Docker
* Docker Compose
* Gunicorn
* drf-spectacular (Swagger/OpenAPI)

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

Install the following before running the project:

* Python 3.11 or above
* PostgreSQL
* Git
* Docker Desktop (Optional)

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/07anushka/client-management-api.git

cd client-management-api
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

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

Create a file named:

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

## 5. Configure PostgreSQL

Ensure PostgreSQL is installed and running.

Create a database named:

```
client_management
```

Update the credentials in the `.env` file if they differ from your local PostgreSQL setup.

---

## 6. Apply Database Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## 7. Create Superuser

```bash
python manage.py createsuperuser
```

---

## 8. Run Development Server

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

---

# Docker Setup

## Build and Start Containers

```bash
docker compose up --build
```

## Start Existing Containers

```bash
docker compose up
```

## Stop Containers

```bash
docker compose down
```

---

# API Documentation

## Swagger UI

```
http://localhost:8000/api/docs/
```

## OpenAPI Schema

```
http://localhost:8000/api/schema/
```

## Django Admin

```
http://localhost:8000/admin/
```

---

# Authentication

The project uses JWT Authentication.

## Register

```
POST /api/accounts/register/
```

## Login

```
POST /api/accounts/login/
```

After login:

1. Copy the **Access Token**
2. Click **Authorize** in Swagger
3. Enter:

```
Bearer <access_token>
```

You can now access all protected endpoints.

---

# API Modules

| Endpoint            | Description               |
| ------------------- | ------------------------- |
| /api/accounts/      | Authentication            |
| /api/clients/       | Client Management         |
| /api/packages/      | Package Management        |
| /api/subscriptions/ | Client Package Assignment |
| /api/payments/      | Payment Management        |
| /api/projects/      | Project Management        |
| /api/notes/         | Notes Management          |
| /api/dashboard/     | Dashboard Analytics       |

---

# Database

Database:

* PostgreSQL

Main Tables:

* Users
* Clients
* Packages
* Client Packages
* Payments
* Projects
* Notes

---

# API Features

* JWT Authentication
* CRUD Operations
* Dashboard Analytics
* Search
* Filtering
* Pagination
* Soft Delete
* Swagger Documentation

---

# API Verification

The following functionality has been verified:

* User Registration
* JWT Login
* Create Client
* Assign Package
* Create Payment
* Create Project
* Update Project Status
* Add Notes
* Dashboard APIs

---

# Docker Support

The project includes:

* Dockerfile
* Docker Compose
* PostgreSQL Container
* Gunicorn Application Server

Run everything with:

```bash
docker compose up --build
```

---

# Future Improvements

* Email Notifications
* Client Activity Logs
* Role-Based Access Control (RBAC)
* File Upload Support
* Report Generation
* Unit Tests
* Integration Tests

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
