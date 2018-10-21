from django.db import models

class TypMedia(models.Model):
  nazev = models.CharField(max_length=100)
  kod = models.CharField(max_length=20, unique=True)
  # patern pro získání zdroje, v řetězci je jednou {} pro doplnění kodu
  pattern = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return '{0} [{1}]'.format(self.nazev, self.kod)

  class Meta:
    verbose_name = 'Typ média'
    verbose_name_plural = 'Typy médií'

class Media(models.Model):
  unique = models.CharField(max_length=100)# unikatní identifikátor url/hash_id/kod ...
  typ = models.ForeignKey(TypMedia, on_delete=models.PROTECT)
  active = models.BooleanField(default=False)

  class Meta:
    unique_together = ('unique', 'typ')
    verbose_name = 'Média'
    verbose_name_plural = 'Média'

  def __str__(self):
    return self.typ.nazev

  @property
  def url(self):
    return self.typ.pattern.format(self.unique) if self.typ.pattern else self.unique

class PouzitiMedia(models.Model):
  """
  Nelze použít ManyToMany na abstraktní třídu
  Tak toto je způsob jak to obejít:
  Třída Zaznam má property unique, která vrací kombinaci className:id
  Přes tuto kombinaci se získá objekt přes property zaznam
  - toto je vlastně vazebka (má odkaz na media) a pomocí property zaznam se dostaneme na záznam
  """
  media = models.ForeignKey(Media, on_delete=models.CASCADE)
  zaznam_unique = models.CharField(max_length=50) # className:id pro záznam ke kterému se vztahuje

  class Meta:
    unique_together = ('media', 'zaznam_unique')
    verbose_name = 'Použití média'
    verbose_name_plural = 'Použití médií'

  def clean(self):
    print(self.zaznam)

  @property
  def zaznam(self):
    cls, pk = self.zaznam_unique.split(':')
    return eval('{0}.objects.get(pk={1})'.format(cls, pk))

  def save(self, *args, **kwargs):
    self.full_clean()
    super().save(*args, **kwargs)