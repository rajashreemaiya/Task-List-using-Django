# Task-List-using-Django
A simple tasks app using django framework

This app uses the django default database sqlite3. We can also use other database engines by installing the appropriate database bindings. This requires some modifications in the settings.py file.

This application has the following features:

1. Add a new task
2. Update the contents of an existing task
3. Mark a task as completed
4. Delete a task

The following links does each job mentioned above:

1. /tasks - Homepage : Displays a list of existing tasks and lets you create a new task.
2. /tasks/id/detail - A single task page, displays each task and gives an option to update if it is not marked as completed. Also, has a link 'All Tasks' on header to navigate back to the homepage.

To run this app on your local machine, follow the below steps:

1. cd /TasksApp
2. python manage.py migrate
3. python manage.py runserver

The server will be started at http://127.0.0.1:8000/

A django admin interface is set up at http://127.0.0.1:8000/admin

username: admin

password: password

Navigate to tasks homepage using http://127.0.0.1:8000/tasks. This page will let you perform all the functionalities of the app.

If the admin interface does not work, create a user using:

python manage.py createsuperuser

username : admin

email : admin@example.com

Enter the desired password.
