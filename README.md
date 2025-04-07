# Join_Backend 


## Table of Contents

* [Description](#description)
* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Frontetnd](#frontend)
* [API Endpoints](#api-endpoints), [Documentation](#documentation)
* [Built with](#built-with)
* [License](#license)

## Description

This project was specifically created for the purpose of practicing with Python and the Django framework. 
This backend makes it possible to read, edit, and delete tasks and contacts through the "Join" frontend.


## Features

* Feature 1: Token based authorization
* Feature 2: Manage tasks (CRUD) and  manage contacts (CRUD)
* Feature 3: create example tasks and contacts after sign in

## Prerequisites

Before you begin, ensure you have the following software installed:

* **Python:** Version 3.11+
* **pip:** (Python Package Installer, usually included with Python)
* all you need for this project is in [requirements.txt](requirements.txt)


## Installation

Follow these steps to set up the project locally:

**Steps:**

1.  **Get the Code:**
    ```bash
    git clone [https://github.com/Philipp-Loetzsch/join_backend]
    cd join_backend
    ```

2.  **Set up Virtual Environment:**
    ```bash
    python -m venv env  # Creates a virtual environment named 'env'
    ```

3.  **Activate Virtual Environment:**
    ```bash
    # Linux/macOS:
    source env/bin/activate
    # Windows (cmd/PowerShell):
    .\env\Scripts\activate
    ```
    *(You should see `(env)` at the start of your prompt.)*

4.  **Install Dependencies:**
    * This command installs Django, djangorestframework, django-cors-headers, and everything else needed, based on the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Environment:**
    * Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    * **Edit the `.env` file:** Open the newly created `.env` file. You MUST replace the placeholder for `SECRET_KEY`. You can generate a new key easily using Python in your terminal (make sure your virtual environment is active):
        ```bash
        python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
        ```
    * Copy the long random string generated by this command and paste it as the value for `SECRET_KEY` in your `.env` file. Also, fill in any other necessary placeholder values.

6.  **(If Applicable) Set up Database:**
    ```bash
    python manage.py migrate
    ```

7.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
**Using VS Code:**

* After completing the steps above in your terminal, you can open the project folder (`[join_backend]`) in Visual Studio Code.
* VS Code should automatically detect and use the Python interpreter from your activated virtual environment (`env`) for running and debugging (you might need to select it manually the first time via the status bar or Command Palette).

## Frontend

This Backend is only used with the following frontend named "join"
Follow this link to download the join_frontend [https://github.com/Philipp-Loetzsch/join_frontend]

## Api-endpoints
http://127.0.0.1:8000/
* **tasks api**
   * api/user/tasks/
   * api/user/tasks/<int:pk>/
   * api/user/contacts/
   * api/user/contacts/<int:pk>/
   * api/user/tasks/<int:task_id>/subtasks/
   * api/user/tasks/<int:task_id>/subtasks/<int:pk>/
* **user api**
   * login/
   * registration/


## Docunemtation

Shows the documentation of the code created with sphinx
[DCUMENTAION](docs/build/html/index.html)

## Built With
* Python 3.13.1
* Django 5.1.6
* Django REST framework
* Django CORS Headers
* SQLite (Standard) / PostgreSQL (Optional)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.