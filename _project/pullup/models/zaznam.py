from django.db import models
from django.utils.text import slugify
from .media import PouzitiMedia

class Zaznam(models.Model):
  nazev = models.CharField(max_length=100)
  # vyřešit slug
  slug = models.SlugField(max_length=100, unique=True)
  popis = models.CharField(max_length=500, blank=True)

  active = models.BooleanField(default=False)
  created_dt = models.DateTimeField(auto_now_add=True)
  updated_dt = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

  def __str__(self):
    return self.nazev

  @property
  def unique(self):
    """ unikátní kombinace className:id """
    if self.pk:
      return '{0}:{1}'.format(self.__class__.__name__, self.pk)
    else:
      return None

  def save(self, *args, **kwargs):
    self.slug = slugify(self.nazev)
    super().save(*args, **kwargs)

  def delete(self, using=None, keep_parents=False):
    # když se maže, je potřeba také smazat vazebku PouzitiMedia - simulace CASCADE
    for vazebka in PouzitiMedia.objects.filter(zaznam_unique=self.unique):
      vazebka.delete()

    super().delete()
