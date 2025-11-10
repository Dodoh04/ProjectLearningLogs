from django.db import models

# Create your models here.

class Topic(models.Model):
    """Um assunto sobre qual o usuario esta aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """DEvolve uma representação em string do modelo"""
        return self.text 

class Entry(models.Model):
    """Algo especifico aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text =  models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma string do modelo"""
        return self.text[:50] + '...'

class Vaga(models.Model):
    """Algo especifico aprendido sobre um assunto"""
    Tipo = models.ForeignKey(Topic, on_delete=models.CASCADE)
    Cargo =  models.TextField(max_length=30)
    Data =  models.DateTimeField()   
    CPF =  models.TextField(max_length=11)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'vagas'

    def __str__(self):
        """Devolve uma string do modelo"""
        return self.text , self.DateTimeField