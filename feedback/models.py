from django.db import models

class CustomerFeedback(models.Model):
    EXPERIENCE_CHOICES = [
        ('POSITIVE', 'Positive'),
        ('NEGATIVE', 'Negative'),
        ('NEUTRAL', 'Neutral'),
    ]
    
    experience_text = models.TextField()  # Stores the customer feedback text
    sentiment_label = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
    sentiment_score = models.FloatField()  # Stores the confidence score of the sentiment

    def __str__(self):
        return f"Feedback ({self.sentiment_label}): {self.experience_text[:50]}..."
