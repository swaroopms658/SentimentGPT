# Generated by Django 5.1.3 on 2025-01-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_feedback_confidence_score_feedback_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_text', models.TextField()),
                ('sentiment_label', models.CharField(choices=[('POSITIVE', 'Positive'), ('NEGATIVE', 'Negative'), ('NEUTRAL', 'Neutral')], max_length=10)),
                ('sentiment_score', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
