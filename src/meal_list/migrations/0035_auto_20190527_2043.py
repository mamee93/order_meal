# Generated by Django 2.2 on 2019-05-27 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_list', '0034_auto_20190527_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='post_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
