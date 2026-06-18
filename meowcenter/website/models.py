from django.db import models

# Create your models here.
class Pet(models.Model):
    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ]

    STATUS_CHOICES = [
        ('available', 'Доступен для помощи'),
        ('adopted', 'Взят домой'),
        ('foster', 'Взят на передержку'),
    ]

    name = models.CharField(max_length=100, blank=False)
    age = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=False)

    health_issues = models.BooleanField(default=False)

    description = models.TextField(blank=False)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=False)

    photo = models.CharField(max_length=255, blank=False)
    video = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)