from django.db import models

class Topic(models.Model):
    """ Um assunto sobre o qual o usuŕio está aprendendo. """
    text = models.CharField(max_length=200)#usado quando queremos armazenar uma quantidade pequena de texto
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text
