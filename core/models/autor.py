from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100, default='Autor')
    
    def __str__(self) -> str:
        return self.nome