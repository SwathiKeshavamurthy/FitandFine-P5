# Generated by Django 3.2.25 on 2024-05-14 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(blank=True, help_text='Name of the person for the routine, if different from the user.', max_length=100)),
                ('date', models.DateField()),
                ('wake_up_time', models.TimeField()),
                ('breakfast_time', models.TimeField()),
                ('lunch_time', models.TimeField()),
                ('dinner_time', models.TimeField()),
                ('total_calorie_intake', models.IntegerField(help_text='Total calories consumed in the day.')),
                ('water_intake', models.IntegerField(help_text='Water intake in milliliters')),
                ('sleep_time', models.TimeField()),
                ('workout_minutes', models.IntegerField(help_text='Total workout time in minutes.')),
                ('junk', models.BooleanField(default=False, help_text='Did the user consume junk food?')),
                ('mood', models.CharField(choices=[('happy', 'Happy'), ('sad', 'Sad'), ('tired', 'Tired'), ('energetic', 'Energetic'), ('stressed', 'Stressed')], default='happy', max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
