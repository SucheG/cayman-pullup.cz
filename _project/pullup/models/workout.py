from django.db import models
from .zaznam import Zaznam
from .ostatni import Telo, Vybaveni

class Cvik(Zaznam):
  telo = models.ManyToManyField(Telo, blank=True)
  vybaveni = models.ManyToManyField(
    Vybaveni,
    through='Potrebuje',
    through_fields=('cvik', 'vybaveni'),
    blank=True
  )
  varianty = models.ManyToManyField(
    'self',
    through='Varianta',
    through_fields=('cvik1', 'cvik2'),
    symmetrical=False,
    blank=True
  )

  class Meta:
    verbose_name_plural = 'Cviky'


class Potrebuje(models.Model):
  """
  Vazebka M:N cvik potřebuje vybavení
  """
  cvik = models.ForeignKey(Cvik, on_delete=models.CASCADE)
  vybaveni = models.ForeignKey(Vybaveni, on_delete=models.CASCADE)
  povinny = models.BooleanField(default=False)
  active = models.BooleanField(default=False)

  class Meta:
    unique_together = ('cvik', 'vybaveni')
    verbose_name_plural = 'Potřeby'
    verbose_name = 'Potřeba'

  def __str__(self):
    return self.cvik.nazev + ' potřebuje ' + self.vybaveni.nazev

class Varianta(models.Model):
  """
  Vazebka M:N cvik1 a cvik2
  """
  cvik1 = models.ForeignKey(Cvik, on_delete=models.CASCADE, related_name='cvik1')
  cvik2 = models.ForeignKey(Cvik, on_delete=models.CASCADE, related_name='cvik2')
  popis = models.CharField(max_length=500, blank=True)  # v čem se cvik2 liší od cviku1
  obtiznost = models.SmallIntegerField(default=0)
  active = models.BooleanField(default=False)

  class Meta:
    unique_together = ('cvik1', 'cvik2')
    verbose_name_plural = 'Varianty'

  def __str__(self):
    return self.cvik2.nazev + ' je variantou ' + self.cvik1.nazev