# Django Interview Projects

A collection of common Django applications built for interview preparation and practical learning.

## About

This project demonstrates practical Django development skills through implementation of commonly requested features and apps. Each app showcases different aspects of Django development including models, views, templates, and URL routing.

## Apps Included

### Todo App
A simple task management application that allows users to:
- Create, read, update, and delete todo items
- Manage tasks efficiently
- Basic CRUD operations demonstration

### Calculator App
A calculator application showcasing:
- Form handling and validation
- Dynamic calculations
- Basic arithmetic operations

## Project Structure

```
interview_projects/           # Main Django project
├── manage.py                  # Django management script
├── interview_projects/        # Project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py               # Root URL routing
│   └── wsgi.py               # WSGI configuration
├── todo/                      # Todo application
│   ├── models.py             # Data models
│   ├── views.py              # View logic
│   ├── urls.py               # App URL routing
│   ├── templates/            # HTML templates
│   └── migrations/           # Database migrations
└── db.sqlite3                # SQLite database
```

## Getting Started

### Prerequisites
- Python 3.8+
- Django 3.2+
- pip

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd django-interview-projects
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Apply migrations
```bash
cd interview_projects
python manage.py migrate
```

4. Run the development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser to access the applications.

## Technologies Used

- **Django**: Web framework
- **SQLite**: Database
- **HTML/CSS**: Frontend
