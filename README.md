# 🔐 IMPLEMENTION 1

This 'implemention 1' implements a secure user authentication system using **Django**, **Django REST Framework**, and **SimpleJWT**.
Access and refresh tokens are stored in **HttpOnly cookies**, enabling safe authentication from web clients.

---

## 🚀 Features

* User Registration API
* Login API using JWT (sets cookies)
* Public API (accessible to everyone)
* Protected API (requires authentication)
* Django `login.html` and `register.html` pages
* Custom JWT authentication class that supports cookie-based token reading


---

## API Development

### 1. Public API Endpoint

* **URL**: `/api/public/`
* **Method**: `GET`
* **Access**: Public (no authentication required)
* **Response**:

  ```json
  {
    "message": "Hi welcome to the public API endpoint."
  }
  ```

### 2. Protected API Endpoint

* **URL**: `/api/protected/`
* **Method**: `GET`
* **Access**: Requires authentication (JWT token stored in cookie)
* **Authentication Used**: `CookieJWTAuthentication`
* **Response**:

  ```json
  {
    "message": "Seeing this because you are authenticated."
  }
  ```

### 3. User Registration API

* **URL**: `/api/register/`
* **Method**: `POST`
* **Body**:

  ```json
  {
    "username": "ajay123",
    "email": "ajay@example.com",
    "password": "strongpassword"
  }
  ```
* **Response**:

  ```json
  {
    "id": 1,
    "username": "ajay123",
    "email": "ajay@example.com"
  }
  ```

### 4. JWT Login API (Sets Cookies)

* **URL**: `/api/login/`
* **Method**: `POST`
* **Body**:

  ```json
  {
    "username": "ajay123",
    "password": "strongpassword"
  }
  ```
* **Response**: Sets `access_token` and `refresh_token` in HttpOnly cookies

  ```json
  {
    "message": "Login successful"
  }
  ```
### 5. Register page for Django web based login
* **URL**: `/api/register_page/`

  

# Implementation 2: Send Welcome Email After Registration (Celery + Redis)

---

## Features

* Sends welcome email after successful registration in console
* Email task runs in background using Celery


---
# Telegram Bot + Django Backend

a Telegram Bot integrated with a Django REST API using environment variables and PostgreSQL.

🚀 Features

Collect Telegram usernames via /start

Store them in a PostgreSQL database using Django


## 🧩 Folder Structure

```
project_root/
├── django_backend/
│   ├── users/
│   ├── backend/         # Django project
│   ├── manage.py
├── telegram/
     ├── bot.py          # Telegram bot script
├── .env                 # Environment variables
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone and Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2.env File
Create a .env file in the root:
```
  SECRET_KEY=your_django_secret_key
  
  # Used PostgreSQL
  DB_NAME=your_db_name
  DB_USER=your_db_user
  DB_PASSWORD=your_db_password
  DB_HOST=localhost
  DB_PORT=5432
  
  BOT_TOKEN=your_telegram_bot_token
  API_ENDPOINT=http://127.0.0.1:8000/api/telegram_user/

```


### 3. Start Redis Server

```bash
sudo service redis-server start
```

### 4. Start Django Server

```bash
python manage.py runserver
```
### 5. start Telegram Bot

```bash
telegram/bot.py
```

### 6. Start Celery Worker

```bash
celery -A project_name worker --loglevel=info
```






