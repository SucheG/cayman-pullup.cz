from django.db import models

class Zaznam(models.Model):
  nazev = models.CharField(max_length=100)
  popis = models.CharField(max_length=500)

  active = models.BooleanField(default=True)
  created_dt = models.DateTimeField(auto_now_add=True)
  updated_dt = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

  def __str__(self):
    return self.nazev



class Misto(Zaznam):
  x = models.FloatField()
  y = models.FloatField()

  uploaded_to_mapbox = models.BooleanField(default=False)


