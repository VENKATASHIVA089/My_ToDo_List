# Generated by Django 2.1.2 on 2018-10-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='desg',
            field=models.CharField(default='Developer', max_length=25),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='name', max_length=20),
        ),
    ]
