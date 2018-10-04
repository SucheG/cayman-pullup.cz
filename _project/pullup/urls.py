from django.urls import path
from . import views

app_name = 'pullup'

urlpatterns = [
  # path('mapbox/', ) // udělat index pro tlačítkové ovládání
  path('mapbox-datasets-list/', views.Mapbox.datasets_list, name='mapbox-datasets-list'),
  path('mapbox-datasets-insert/<dataset_id>/', views.Mapbox.datasets_insert, name='mapbox-datasets-insert'),

  path('upload-tileset-from_dataset/<tileset_id>/<dataset_id>/', views.Mapbox.upload_tileset_from_dataset, name='upload-tileset-from_dataset')
]