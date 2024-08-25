# Generated by Django 5.1 on 2024-08-25 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('todo_id', models.AutoField(primary_key=True, serialize=False)),
                ('todo_completed', models.BooleanField(default=False)),
                ('todo_text', models.CharField(max_length=100)),
                ('todo_update', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'todolist',
            },
        ),
    ]
