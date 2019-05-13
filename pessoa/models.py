from django.db import models

# Create your models here.

class PessoaModel(models.Model):
    pessoa_id = models.AutoField(primary_key=True)
    pessoa_nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Nome")
    pessoa_logradouro = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Logradouro")
    pessoa_numero = models.CharField(
        max_length=5,
        null=False,
        blank=False,
        verbose_name="Número")

    class Meta:
        ordering = ['pessoa_nome']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.pessoa_nome


class ContatoModel(models.Model):
    
    contato_id = models.AutoField(primary_key=True)
    contato_telefone = models.CharField(
                       max_length=15,
                       null=False,
                       blank=False,
                       verbose_name="Telefone")
    pessoa = models.ForeignKey(PessoaModel, on_delete=models.CASCADE)
                    
