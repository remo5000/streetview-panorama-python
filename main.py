import urllib.request
import json
from PIL import Image
from API_KEY import key

metadata_endpoint = 'https://maps.googleapis.com/maps/api/streetview/metadata?'
image_endpoint = 'https://maps.googleapis.com/maps/api/streetview?'

def getPanoramaAt(lat, long):
    url = metadata_endpoint + f'location={lat},{long}&key={key}'
    response = urllib.request.urlopen(url).read()
    image_available = json.loads(response).get('status') == 'OK'
    if not image_available:
        print(f'image not available at {lat}, {long}')
        return
    for heading in range(0, 360, 90):
        url = image_endpoint + f'size=640x640&location={lat},{long}&heading={heading}&fov=90&key={key}'
        img =  Image.open(urllib.request.urlopen(url))
        img.save("asdf.jpeg")

getPanoramaAt(40.457375,-80.009353)

