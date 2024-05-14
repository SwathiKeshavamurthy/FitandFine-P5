# Generated by Django 3.2.25 on 2024-05-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('cycling', 'Cycling'), ('hiking', 'Hiking'), ('swimming', 'Swimming'), ('yoga', 'Yoga'), ('running', 'Running'), ('physical_activity', 'Physical Activity'), ('nature', 'Nature'), ('other_activities', 'Other Activities')], default='physical_activity', max_length=100),
        ),
    ]