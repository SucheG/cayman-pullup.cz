from django.shortcuts import render, HttpResponse

from mapbox import Uploader, Datasets
from pullup.models import Misto
from json import dumps

ALL_AT = 'sk.eyJ1IjoicHVsbHVwY3oiLCJhIjoiY2ptc3E0YTNlMGN6cTN2b3l2dm93amFiciJ9.UHSWkNTKNVZmqGjnYiITPw'
json_content_type = 'application/javascript'

class Mapbox():

  datasets = Datasets(access_token=ALL_AT)
  uploader = Uploader(access_token=ALL_AT)
  username = 'pullupcz'

  @classmethod
  def datasets_list(cls, response):
    resp = cls.datasets.list()
    return HttpResponse(resp.json(), content_type=json_content_type)

  @classmethod
  def datasets_insert(cls, response, dataset_id):
    ## pokud je nějaká změna musí se updated_to_mapbox změnit na false
    mista = Misto.objects.filter(active=True, uploaded_to_mapbox=False)

    results = {}

    for misto in mista:
      feature = {
        'id': str(misto.id),
        'type': 'Feature',
        'properties': {'nazev':  misto.nazev, 'popis': misto.popis},
        'geometry': {'type': 'Point', 'coordinates': [misto.y, misto.x]}
      }

      resp = cls.datasets.update_feature(dataset_id, str(misto.id), feature).json()
      results[misto.id] = resp
      misto.uploaded_to_mapbox = True
      misto.save()

    return HttpResponse(dumps(results), content_type=json_content_type)

  @classmethod
  def upload_tileset_from_dataset(cls, request, tileset_id, dataset_id):
    # https://github.com/mapbox/mapbox-sdk-py/issues/152#issuecomment-311708422
    # https://www.mapbox.com/api-documentation/?language=Python#create-an-upload
    uri = "mapbox://datasets/{username}/{dataset_id}".format(username=cls.username, dataset_id=dataset_id)
    res = cls.uploader.create(uri, tileset_id, name='Msta')
    return HttpResponse(dumps({'tileset_id': tileset_id, 'dataset_id': dataset_id, 'result': res.json()}), content_type=json_content_type)