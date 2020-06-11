import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import make_aware

MONDAY_ToDo = 'M'
TUESDAY_ToDo = 'T'
WEDNESDAY_ToDo = 'W'
THURSDAY_ToDo = 'H'
FRIDAY_ToDo = 'F'
SATURDAY_ToDo = 'S'
SUNDAY_ToDo = 'U'
weekdays_list_ToDo = [MONDAY_ToDo, TUESDAY_ToDo, WEDNESDAY_ToDo, THURSDAY_ToDo, FRIDAY_ToDo, SATURDAY_ToDo, SUNDAY_ToDo]

class ToDo(models.Model):

    task = models.CharField('Task Description', max_length=200)
    refresh_days_field = models.CharField('Days of the week to reset task', max_length=7) # m t w h f s u
    refresh_time = models.TimeField('Time of day to reset task') #datetime.time
    last_refreshed = models.DateTimeField('Last time the task was refreshed', default=timezone.now())
    task_done = models.BooleanField('Is the task done', default=False)

    def refresh_task(self):
        if(weekdays_list_ToDo[timezone.now().weekday()] in self.refresh_days_field):
            refresh_today_datetime = make_aware(datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, self.refresh_time.hour, self.refresh_time.minute, self.refresh_time.second))
            if self.last_refreshed < refresh_today_datetime:
                #Store value of task_done in db for last refresh day
                self.task_done = False
                self.last_refreshed = timezone.now()
                self.save()
                return True #Task was refreshed
        return False #Task wasn't refreshed

    def __str__(self):
        return self.task


#TODO create bullet point class that automatically makes the super task complete when all bullets are done
