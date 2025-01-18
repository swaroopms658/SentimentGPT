from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomerFeedback
from .sentiment import sentiment_analyzer

def analyze_sentiment(request):
    sentiment = None
    if request.method == 'POST':
        # Get customer experience text from the POST request
        experience = request.POST.get('experience', '')

        # Analyze the sentiment of the customer's experience text
        sentiment = sentiment_analyzer(experience)

        # Get sentiment label and score
        sentiment_label = sentiment[0]['label']
        sentiment_score = sentiment[0]['score']

        # Save the customer feedback and sentiment result to the database
        feedback = CustomerFeedback(
            experience_text=experience,
            sentiment_label=sentiment_label,
            sentiment_score=sentiment_score
        )
        feedback.save()

    # Render the sentiment result in the template
    return render(request, 'feedback/sentiment_form.html', {'sentiment': sentiment})
