from django.db import models
from datetime import datetime

class ToDoList(models.Model):
    todo_id = models.AutoField(primary_key=True)
    todo_completed = models.BooleanField(default=False)
    todo_text = models.CharField(max_length=100)
    todo_update = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'todolist'