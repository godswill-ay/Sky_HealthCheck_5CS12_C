from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = [
    ('engineer', 'Engineer'),
    ('team_leader', 'Team Leader'),
    ('dept_leader', 'Department Leader'),
    ('senior_manager', 'Senior Manager'),
]

class CustomUser(AbstractUser):
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='engineer')

    def __str__(self):
        return self.username

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return f"{self.name} ({self.department.name})"

class Session(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.date}"

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Vote(models.Model):
    VOTE_CHOICES = [
        ('green', 'Green'),
        ('amber', 'Amber'),
        ('red', 'Red'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='votes'
    )#zq
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='votes')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='votes')
    vote = models.CharField(max_length=10, choices=VOTE_CHOICES)
    progress_better = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'session', 'card')  # one vote per user/session/card

    def __str__(self):
        return f"{self.user.username} - {self.card.title} ({self.vote}) on {self.session}"
