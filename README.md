# django-daily-tasks
Simple web app for a daily refreshing to do list

Created with Django, Jquery, and Bootstrap. Allows you to create a custom todo list where each task resets itself at custom days
and times. This allows you to have tasks that refresh every single day or tasks that refresh only on Mondays or Tuesdays. I
like this style of todo list because it brings attention to tasks that don't need to be done every day.

# Setup guide
There is no database file included in this repository, so you will need to run
```
python manage.py makemigrations
python manage.py migrate
```
Before trying `python manage.py runserver` or the webpage won't work.
