from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, time


class DailyRoutine(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    person_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Name of the person for the routine, if different from the user."
    )
    date = models.DateField()
    wake_up_time = models.TimeField()
    breakfast_time = models.TimeField()
    lunch_time = models.TimeField()
    dinner_time = models.TimeField()
    total_calorie_intake = models.IntegerField(
        help_text="Total calories consumed in the day."
    )
    water_intake = models.IntegerField(
        help_text="Water intake in milliliters"
    )
    sleep_time = models.TimeField()
    workout_minutes = models.IntegerField(
        help_text="Total workout time in minutes."
    )
    junk = models.BooleanField(
        default=False,
        help_text="Did the user consume junk food?"
    )

    MOOD_CHOICES = (
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('tired', 'Tired'),
        ('energetic', 'Energetic'),
        ('stressed', 'Stressed')
    )
    mood = models.CharField(
        max_length=10,
        choices=MOOD_CHOICES,
        default='happy'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.person_name or self.owner.username}'s routine on {self.date}"

    def clean(self):
        super().clean()
        if self.water_intake > 10000:
            raise ValidationError("Water intake is unrealistically high.")
        if self.date > date.today():
            raise ValidationError("The date cannot be in the future.")
