from django.shortcuts import render
from .models import Emotion


def get_affirmations(request):
    """
    Retrieves affirmations based on the selected emotion.
    
    This view fetches all available emotions and displays them in a dropdown form.
    If the user selects an emotion and submits the form, it fetches the related affirmations.
    
    Args:
        request (HttpRequest): The HTTP request object that contains the submitted form data.

    Returns:
        HttpResponse: A rendered template containing the emotion selection form and relevant affirmations.
    """
    emotions = Emotion.objects.all()
    
    if request.method == 'POST':
        # Get the selected emotion from the form data
        selected_emotion = request.POST.get('emotion')
        # Retrieve the affirmations associated with the selected emotion
        affirmations = selected_emotion.affirmations.all() if selected_emotion else []
    else:
        affirmations = []

    return render(request, 'emotions/affirmations.html', {'emotions': emotions,
                                             'affirmations': affirmations})

