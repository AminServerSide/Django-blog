# Django Weblog Project

This is a simple weblog project built with Django.

## How to Use:

1. Install Python requirements:
```bash
pip install -r requirements.txt
```

2. Set up your database 
(SQLite by default, or configure PostgreSQL/MySQL in settings.py):

```bash
python manage.py migrate
```

3. Create a superuser:

```bash
python manage.py createsuperuser
```

4. Run the development server:

```bash
python manage.py runserver
```

## Description:
this is my first django project. it is a simple weblog.
it has some pages and pictures and texts. 
in weblog user can see some articles in home page and there is another page for all articles.
each articles has unique page and users can like articles,share them in social media and add comment.
users can register and login and admin can edit users and articles.

## Features:
User authentication (register/login/logout)

Create, read, update, delete posts

Image uploads for posts

Responsive design with Bootstrap

Search functionality

Category/tag system for posts

Comment system

## Installation:

1. Clone the repository:

```bash

git clone https://github.com/AminServerSide/Django-blog

cd django-weblog
```

2. Create and activate a virtual environment:

```bash

python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:

```bash

pip install -r requirements.txt
```

4. Configure your environment variables in a .env file:

```bash
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Tech Stack

 ![HTML5](https://img.shields.io/badge/-HTML5-333333?style=flat&logo=HTML5)
 ![CSS](https://img.shields.io/badge/-CSS-333333?style=flat&logo=CSS3&logoColor=1572B6)
 ![Bootstrap](https://img.shields.io/badge/-Bootstrap-333333?style=flat&logo=bootstrap&logoColor=563D7C)
 [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000)](#)
 [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
 [![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)](#)
 [![SQLite](https://img.shields.io/badge/SQLite-%2307405e.svg?logo=sqlite&logoColor=white)](#)
