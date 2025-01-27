from django.shortcuts import render
from .models import Emotion


def get_affirmations(request):
    emotions = Emotion.objects.all()  # Fetch all emotions
    affirmations = []

    selected_emotion_name = request.GET.get('emotion')  # Get emotion name from query params
    if selected_emotion_name:
        # Fetch the corresponding Emotion object
        emotion = Emotion.objects.filter(name=selected_emotion_name).first()
        if emotion:
            affirmations = emotion.affirmations.all()  # Fetch affirmations for the emotion

    return render(request, 'emotions/affirmations.html', {
        'emotions': emotions,
        'affirmations': affirmations,
    })
