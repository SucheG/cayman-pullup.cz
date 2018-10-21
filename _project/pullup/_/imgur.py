from requests import request as http_request
import json

# api: https://apidocs.imgur.com/

class Imgur(object):
  client_id = '0e3018f09a810e1'
  client_secret = '6c34c57b9b1a0aac1b79f516b2f2908ecc0b0e80'
  username = 'pullupcz'
  refresh_token = '0f11739d6876349efa78960fcb3e4ee3110331d9' # nutná autorizace pro získání refresh_token
  access_token = '54235d35006443061c54158f2e13e6327fd5a778' # ručně zadané AT - možná bude potřeba reload, ale psali tam platnost na 3650 dnů ... :)
  _form = '------WebKitFormBoundary'
  _hash = '7MA4YWxkTrZu0gW'
  url = 'https://api.imgur.com/3/'

  def get_payload(self, **kwargs):
    """ složí payload - aby ty stringy nebyly tak dlouhý ... a nečitený """
    item = self._form + self._hash + "\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n{value}\r\n"
    payload = "".join([item.format(name=key, value=value) for key, value in kwargs.items()])
    return payload + self._form + self._hash + "--"

  def request(self, method, url, headers, data=None):
    response = http_request(method, url, headers=headers, data=data)
    return response.json()

  def get_access_token(self):
    if self.access_token: return self.access_token # pokud mám access token tak jej použiju

    payload = self.get_payload(
      refresh_token=self.refresh_token,
      client_id=self.client_id,
      client_secret=self.client_secret,
      grant_type='refresh_token',
    )
    headers = {'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'}
    return self.request("POST", "https://api.imgur.com/oauth2/token", headers, payload)

  def album_list(self):
    """list ids of albums"""
    url = self.url + "account/{username}/albums/ids/".format(username=self.username)
    headers = {'Authorization': "Bearer {accessToken}".format(accessToken=self.get_access_token())}
    return self.request("GET", url, headers)

  def album_create(self, nazev, popis, privacy='hidden'):
    """Create a new album"""
    url = self.url + "album"
    payload = self.get_payload(title=nazev, description=popis, privacy=privacy)
    headers = {
      'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
      'Authorization': "Bearer {accessToken}".format(accessToken=self.get_access_token())
    }
    return self.request("POST", url, headers, payload)

  def album_images(self, album_hash):
    """Gets images from album"""
    url = self.url + "album/{albumHash}/images".format(albumHash=album_hash)
    headers = {'Authorization': 'Client-ID {clientId}'.format(clientId=self.client_id)}
    return self.request("GET", url, headers)

  def image_upload(self, image, name, album):
    """

    :param image: url or binary file or base64 (max size 10MB)
    :param name:
    :param album:
    :return:
    """
    url = self.url + "image"
    payload = self.get_payload(image=image, name=name, album=album)
    headers = {
      'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
      'Authorization': "Bearer {accessToken}".format(accessToken=self.get_access_token())
    }
    return self.request("POST", url, headers, payload)


if __name__ == '__main__':
  client = Imgur()
  print(client.album_list())
  print(client.image_upload('R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7', 'test image 1', 'OKgmZlx'))
  ##################### integrovat do djanga a do třídy Media