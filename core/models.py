from django.db import models

from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(verbose_name='Descrição')
    status = models.BooleanField(verbose_name='Ativo', default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Ponto Turístico'
        verbose_name_plural = 'Pontos Turísticos'
