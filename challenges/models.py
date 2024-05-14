from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class Challenge(models.Model):
    """
    Challenge model, managed by an admin or creator.
    """
    SPORT_CHOICES = [
        ('cycling', 'Cycling'),
        ('hiking', 'Hiking'),
        ('swimming', 'Swimming'),
        ('yoga', 'Yoga'),
        ('running', 'Running'),
        ('physical_activity', 'Physical Activity'),
        ('nature', 'Nature'),
        ('other_activities', 'Other Activities'),
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='images/', default='../default_challenge_image', blank=True)
    sport = models.CharField(max_length=100, choices=SPORT_CHOICES, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

    def clean(self):
        super().clean()  
        if not self.sport:
            raise ValidationError('Sport selection cannot be empty upon submission.')
