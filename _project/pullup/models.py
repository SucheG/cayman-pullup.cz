from django.db import models


class Zaznam(models.Model):
  nazev = models.CharField(max_length=100)
  # slug = models.CharField(max_length=100)
  popis = models.CharField(max_length=500, blank=True)

  active = models.BooleanField(default=False)
  created_dt = models.DateTimeField(auto_now_add=True)
  updated_dt = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

  def __str__(self):
    return self.nazev


class Media(Zaznam):
  pass


class Telo(Zaznam):
  latin = models.CharField(max_length=100)


class Vybaveni(Zaznam):
  pass


class Misto(Zaznam):
  x = models.FloatField()
  y = models.FloatField()

  uploaded_to_mapbox = models.BooleanField(default=False)

  vybaveni = models.ManyToManyField(Vybaveni, blank=True)


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


class Potrebuje(models.Model):
  cvik = models.ForeignKey(Cvik, on_delete=models.CASCADE)
  vybaveni = models.ForeignKey(Vybaveni, on_delete=models.CASCADE)
  povinny = models.BooleanField(default=False)

  def __str__(self):
    return self.cvik.nazev + ' potřebuje ' + self.vybaveni.nazev

class Varianta(models.Model):
  cvik1 = models.ForeignKey(Cvik, on_delete=models.CASCADE, related_name='cvik1')
  cvik2 = models.ForeignKey(Cvik, on_delete=models.CASCADE, related_name='cvik2')
  popis = models.CharField(max_length=500, blank=True)  # v čem se cvik2 liší od cviku1
  obtiznost = models.SmallIntegerField(default=0)

  class Meta:
    unique_together = ('cvik1', 'cvik2')

  def __str__(self):
    return self.cvik2.nazev + ' je variantou ' + self.cvik1.nazev

