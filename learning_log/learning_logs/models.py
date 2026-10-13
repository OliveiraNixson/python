from django.db import models

# Create your models here.
class Topic(models.Model): 
    """ Um assunto sobre o qual o usuario esta aprendendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    def __str__(self):
        """Devolve uma representacao em string do modelo."""
        return self.text