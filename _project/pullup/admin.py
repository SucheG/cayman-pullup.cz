from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(
  (
    models.Misto,
    models.Cvik,
    models.Vybaveni,
    models.Telo,
    models.Varianta,
    models.Potrebuje,
  )
)
