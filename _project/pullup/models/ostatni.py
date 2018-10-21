from django.db import models
from .zaznam import Zaznam

"""
Lidé
Komunity
...
"""

class Telo(Zaznam):
  latin = models.CharField(max_length=100)

  class Meta:
    verbose_name = 'Část těla'
    verbose_name_plural = 'Části těl'

class Vybaveni(Zaznam):
  class Meta:
    verbose_name = 'Vybavení'
    verbose_name_plural = 'Vybavení'


class Misto(Zaznam):
  x = models.FloatField()
  y = models.FloatField()

  uploaded_to_mapbox = models.BooleanField(default=False)

  vybaveni = models.ManyToManyField(Vybaveni, blank=True)

  class Meta:
    verbose_name = 'Místo'
    verbose_name_plural = 'Místa'