from django.db import models

class BananaRecord(models.Model):
    STATUS_CHOICES = [
        ('Fresh', 'Fresh'),
        ('Rotten', 'Rotten'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    confidence = models.FloatField(help_text="Enter confidence between 0.0 and 1.0")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.status} ({self.confidence * 100:.1f}%) - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
