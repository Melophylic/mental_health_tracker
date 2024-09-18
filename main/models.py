import uuid
from django.db import models
from django.contrib.auth.models import User


class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    mood = models.CharField(max_length=255, default='0')
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField(default='0')
    mood_intensity = models.IntegerField( default='0')
    nama = models.CharField(max_length=255, default='0')
    npm=models.IntegerField(default='0')
    kelas=models.CharField(max_length=255, default='0')

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5