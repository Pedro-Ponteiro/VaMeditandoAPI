from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models


class Audio(models.Model):
    file = models.FileField(upload_to="sounds")
    activity = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.activity


class Meditation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.ForeignKey(Audio, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')} - {self.audio_file}"


class MeditationParameter(models.Model):
    meditation = models.ForeignKey(
        Meditation, on_delete=models.CASCADE, related_name="parameters"
    )
    parameter_name = models.CharField(
        max_length=50,
        validators=[RegexValidator(r"^[a-zA-Z]{3,}$")],
    )
    parameter_value = models.FloatField()

    def __str__(self) -> str:
        return f"{self.parameter_name} - {self.parameter_value}"
