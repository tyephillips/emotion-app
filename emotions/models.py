from django.db import models


class Emotion(models.Model):
    """
    Represents an emotion that the user might be feeling.
    
    Attributes:
        name (str): The name of the emotion (e.g., Happy, Sad).
    """
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """
        Returns a string representation of the Emotion instance.
        
        Returns:
            str: The name of the emotion.
        """
        return self.name


class Affirmation(models.Model):
    """
    Represents an affirmation related to a specific emotion.
    
    Attributes:
        emotion (ForeignKey): A reference to the Emotion instance this affirmation belongs to.
        text (str): The content of the affirmation.
    """
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, 
                                related_name='affirmations')
    text = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the Affirmation instance.
        
        Returns:
            str: A string indicating which emotion the affirmation is for.
        """
        return f"Affirmation for {self.emotion.name}"
