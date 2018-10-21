from django.contrib import admin

# Register your models here.
from . import models

class SlugAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ['nazev']}

admin.site.register(
  (
    models.Misto,
    models.Cvik,
    models.Vybaveni,
    models.Telo,
  ), SlugAdmin
)

admin.site.register(
  (
    models.Varianta,
    models.Potrebuje,
    models.TypMedia,
    models.Media,
    models.PouzitiMedia,
  )
)