from django.urls import path

from .views import (
        indexView,
        modView,
        postMod,
        updateModAdded,
        postTask,
        updateTaskDone,
    )

app_name = 'todo'
urlpatterns = [
        path('todo/', indexView, name='index'),
        path('mods/', modView, name="mod_list"),
        path('post/ajax/mod', postMod, name='post_mod'),
        path('post/ajax/modAdded', updateModAdded, name="update_mod_added"),
        path('post/ajax/task', postTask, name='post_task'),
        path('post/ajax/taskDone', updateTaskDone, name='update_task_done'),
    ]
