from django.urls import path
from .views.mapbox import Mapbox
from .views.web_post import WebPost

app_name = 'pullup'

urlpatterns = []

# mapbox
urlpatterns += [
  # path('mapbox/', ) // udělat index pro tlačítkové ovládání
  path('mapbox-datasets-list/', Mapbox.datasets_list, name='mapbox-datasets-list'),
  path('mapbox-datasets-insert/<dataset_id>/', Mapbox.datasets_insert, name='mapbox-datasets-insert'),
  path('upload-tileset-from_dataset/<tileset_id>/<dataset_id>/', Mapbox.upload_tileset_from_dataset, name='upload-tileset-from_dataset')
]

# web post
urlpatterns += [
  path('web-post-iframe', WebPost.get_iframe, name='web-post-iframe'),
  path('web-post-solve', WebPost.solve_post, name='web-post-solve'),
]