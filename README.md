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
# Implementation 2: Send Welcome Email After Registration (Celery + Redis)

---

## Features

* Sends welcome email after successful registration in console
* Email task runs in background using Celery


---

## 🧩 Folder Structure (Relevant Files Only)

```
project_name/
├── project_name/
│   ├── __init__.py        # Initializes Celery app
│   └── celery.py          # Celery config
├── your_app/
│   ├── views.py           # RegisterApiView
│   ├── tasks.py           # Celery email task
│   ├── serializers.py     # RegisterSerializer
├── manage.py
```

---

## ⚙️ Setup Instructions

### 1. Clone and Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Configure Email Settings in `settings.py`


```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```

### 3. Start Redis Server

```bash
sudo service redis-server start
```

### 4. Start Django Server

```bash
python manage.py runserver
```

### 5. Start Celery Worker

```bash
celery -A project_name worker --loglevel=info
```

---

## 🛠️ RegisterApiView (DRF)

```python
class RegisterApiView(CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email_task.delay(user.username, user.email)
```

---

## 📨 Celery Task Example

```python
@shared_task
def send_welcome_email_task(username, email):
    send_mail(
        subject="Welcome to MyApp",
        message=f"Hi {username},\n\nThanks for registering at MyApp!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )
```

---

## 📫 API Endpoint

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| POST   | `/api/register/` | Register a new user |

---

## 📎 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Built by Ajay H. For learning and demonstration purposes.



