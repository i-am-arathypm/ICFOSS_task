
# ICFOSS-task-
Authentication page
## Overview
 This web page enable users to log in using their registered username and password , if user is not registered , they can register.

## Prerequisites
-python3

## Installation Instructions

1. **Clone the repository:**
```bash
git clone [git@github.com:i-am-arathypm/ICFOSS-task-.git](https://github.com/i-am-arathypm/ICFOSS_task.git)
```

3. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
5. **Create a superuser (optional):**
    ```bash
    python manage.py createsuperuser
    ```
6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```
7. Open your browser and go to `http://127.0.0.1:8000/` to see the project in action.

- **DATABASES:** - SQLite

- # Execution Steps
# User Registration and Login

## Register a New User

1. Navigate to [http://localhost:8000/register](http://localhost:8000/register).
2. Fill in the registration form with valid data.
3. Submit the form to create a new user account.

## Login

1. Navigate to [http://localhost:8000/](http://localhost:8000/).
2. Enter your registered username and password.
3. Submit the form to log in.# Execution Steps




  
