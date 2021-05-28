from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(verbose_name='Descrição')
    horario_funcionamento = models.TextField(verbose_name='Horário de Funcionamento')
    idade_minima = models.IntegerField()

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'
