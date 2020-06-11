from django.urls import path

from .views import (
        indexView,
        postTask,
        updateTaskDone,
    )

app_name = 'todo'
urlpatterns = [
        path('', indexView, name='index'),
        path('post/ajax/task', postTask, name='post_task'),
        path('post/ajax/taskDone', updateTaskDone, name='update_task_done'),
    ]
