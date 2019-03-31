from django.db import models
from hashids import Hashids
from string import ascii_uppercase, digits

# tohle se nesmí změnit !
hashids = Hashids(
  salt="letadlo_.-._",
  min_length=8,
  alphabet=digits + ascii_uppercase
)

class Osoba(models.Model):
  nad = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT)
  jmeno = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  trener = models.BooleanField()
  aktivni = models.BooleanField(default=False)
  imgur_id = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return '{} [{}]'.format(self.jmeno, self.email)

  @property
  def hashid(self):
    return  hashids.encode(self.pk)