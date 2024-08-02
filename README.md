# ICFOSS Task - Authentication Page

## Overview
This web page enables users to log in using their registered username and password. If the user is not registered, they can register.

## Prerequisites
- **Python 3**

## Installation Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/i-am-arathypm/ICFOSS_task.git
    ```

2. **Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install django
    ```

4. **Apply database migrations:**
    ```bash
    python manage.py migrate
    python manage.py makemigrations
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

## Database
- **SQLite**

## Execution Steps

### User Registration and Login

#### Register a New User

1. Navigate to [http://localhost:8000/register](http://localhost:8000/register).
2. Fill in the registration form with valid data.
3. Submit the form to create a new user account.

#### Login

1. Navigate to [http://localhost:8000/](http://localhost:8000/).
2. Enter your registered username and password.
3. Submit the form to log in.
