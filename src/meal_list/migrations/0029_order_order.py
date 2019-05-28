# Generated by Django 2.2 on 2019-05-22 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_list', '0028_remove_order_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='meal_list.Meal'),
        ),
    ]
