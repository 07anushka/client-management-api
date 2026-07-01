# Client Management API

A production-ready Django REST API for managing clients, packages, subscriptions, payments, projects, and notes.

---

## Features

- JWT Authentication
- Client Management
- Package Management
- Subscription Management
- Payment Tracking
- Project Management
- Notes Management
- Dashboard Analytics
- PostgreSQL Database
- Docker Support
- Swagger API Documentation
- Django Admin

---

## Tech Stack

- Python 3.13
- Django 5
- Django REST Framework
- PostgreSQL
- Docker
- Gunicorn
- drf-spectacular (Swagger)

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/client-management-api.git

cd client-management-api
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file.

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

### Run Migrations

```bash
python manage.py migrate
```

---

### Create Superuser

```bash
python manage.py createsuperuser
```

---

### Run Server

```bash
python manage.py runserver
```

Server:

```
http://127.0.0.1:8000/
```

---

# Docker

Build

```bash
docker compose up --build
```

Run

```bash
docker compose up
```

Stop

```bash
docker compose down
```

---

# API Documentation

Swagger

```
http://localhost:8000/api/docs/
```

Schema

```
http://localhost:8000/api/schema/
```

Admin

```
http://localhost:8000/admin/
```

---

# API Modules

- Accounts
- Clients
- Packages
- Subscriptions
- Payments
- Projects
- Notes
- Dashboard

---

# Authentication

JWT Authentication

- Register
- Login
- Refresh Token
- Profile

---

# Project Structure

```
accounts/
clients/
dashboard/
notes/
packages/
payments/
projects/
subscriptions/

config/

Dockerfile

docker-compose.yml

requirements.txt

README.md
```

---

# Author

Anushka A Naik