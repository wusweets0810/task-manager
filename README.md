# Task Manager

## Project Purpose
This project is a simple task and goal manager built with Django.  
It helps users organize study tasks and everyday tasks in one place, create long-term goals, and manage progress through categories and tasks.

## Main Features
- User registration, login, and logout
- Dashboard page
- Create and view tasks
- Create and view goals
- Organize tasks using categories
- Basic access control so users can view their own tasks and goals
- Admin management through Django admin

## Models
The project includes the following models:
- Category
- Goal
- Task
- Comment
- Reminder
- User (Django built-in model)

## Views
The project includes the following views:
- register_view
- login_view
- logout_view
- dashboard
- task_list
- task_create
- goal_list
- goal_create

## Forms
The project includes:
- TaskForm
- GoalForm
- RegisterForm
- AuthenticationForm (Django built-in)

## Authentication and Access Control
The application uses Django’s built-in authentication system.  
Users can register, log in, and log out.  
Some pages require login, and task/goal lists are filtered by the currently logged-in user.

## Static Files
The project uses a simple CSS file to improve layout and readability.

## How to Run the Project
1. Clone the repository
2. Install dependencies from `requirements.txt`
3. Run migrations
4. Start the development server

Example commands:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Repository Contents

The repository includes:

application source code
requirements.txt
data.json data dump
Sample Credentials

Sample credentials for testing are provided separately in the final report.

AI Usage

AI tools were used for limited support in debugging, explaining Django errors, and generating small boilerplate code examples.
The final integration, testing, and project assembly were completed and reviewed manually.