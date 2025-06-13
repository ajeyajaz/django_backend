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

---

## 🛡️ Security Notes

* Tokens are stored in `HttpOnly`, `Secure`, `SameSite=Lax` cookies.
* DRF reads JWT from **cookies**, not headers, via a custom authentication class.

---

## 📁 File Overview

```
project/
├── users/
│   ├── views.py                  # Register, Login, Logout, API views
│   ├── serializers.py            # Register serializer
│   ├── authentication.py         # Custom CookieJWTAuthentication class
│   └── templates/
│       ├── login.html
│       └── register.html
├── settings.py
├── urls.py
└── manage.py
```

## 👤 Author

**Ajay H.**
Backend Developer | Django | Python | REST APIs



---

## 📦 Installation

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
