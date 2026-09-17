# Appointment Booking System

A salon/service appointment booking system with a **Django REST Framework** backend and a **React (Vite)** frontend.

## Overview

The backend exposes a REST API for managing salon **services** (e.g. haircut) and **appointments** booked against those services.

## Tech Stack

**Backend**
- Django REST Framework
- django-cors-headers
- python-decouple (environment-based settings)
- SQLite (default dev database)

**Frontend**
- React
- Vite
- ESLint

## Project Structure

```
Appointment-Booking-System-main/
├── backend/
│   ├── config/              # Django project settings, URLs, WSGI/ASGI
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── api_urls.py
│   ├── salon/                # Main app
│   │   ├── models/           # Service, Appointment
│   │   ├── serializers/      # DRF serializers
│   │   ├── views/            # API views
│   │   ├── urls/             # App-level routes
│   │   ├── admin/             # Django admin registration
│   │   └── migrations/
│   ├── manage.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── pages/ServicePage.jsx
    │   └── components/ServiceForm.jsx
    ├── package.json
    └── vite.config.js
```

## Data Models

### Service
| Field | Type | Notes |
|---|---|---|
| `name` | string | Unique |
| `price` | decimal | Must be > 0 |
| `duration` | integer | Duration in minutes, must be > 0 |

### Appointment
| Field | Type | Notes |
|---|---|---|
| `customer_name` | string | |
| `customer_phone` | string | |
| `service` | FK → Service | Protected on delete |
| `date` | date | |
| `time` | time | |
| `notes` | text | Optional |
| `status` | choice | `Pending`, `Confirmed`, `Completed`, `Cancelled` (defaults to `Pending`) |
| `created_at` / `updated_at` | datetime | Auto-managed |

## API Endpoints

Base path: `/api/`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/services/` | List all services |
| `POST` | `/api/services/` | Create a service |
| `PUT` | `/api/services/<id>/` | Update a service |
| `DELETE` | `/api/services/<id>/` | Delete a service (blocked if it has existing appointments) |
| `GET` | `/api/appointments` | List appointments (optional `?status=` filter, e.g. `?status=Confirmed`) |
| `POST` | `/api/appointments` | Create an appointment |
| `DELETE` | `/api/appointments/<pk>` | Cancel/delete an appointment |


## Getting Started

### Backend setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file inside `backend/` (values are read via `python-decouple`):

```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Then run migrations and start the server:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`.

### Frontend setup

```bash
cd frontend
npm install
npm run dev
```

The dev server runs at `http://127.0.0.1:5173` by default, which is already whitelisted in the backend's CORS settings.

## Project Status

This project is a work in progress:
- The backend API (services, appointments, admin) is functional.
- The frontend is currently a fresh Vite/React scaffold — `App.jsx`, `ServicePage.jsx`, and `ServiceForm.jsx` are present but not yet implemented.

