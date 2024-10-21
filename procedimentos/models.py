from django.db import models

class Dentista(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=75, null=False, blank=False)
    cro = models.CharField(max_length=15)



class Procedimento(models.Model):
    nome_paciente = models.CharField(max_length=100, null=False, blank=False)
    procedimento = models.CharField(max_length=200, null=False, blank=False)
    data_procedimento = models.DateTimeField()
    valor_procedimento = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    dentista = models.ForeignKey(Dentista, on_delete=models.SET_NULL, null=True, related_name="procedimentos")
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
