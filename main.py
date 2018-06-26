import urllib.request
import json
from PIL import Image
from API_KEY import key

metadata_endpoint = 'https://maps.googleapis.com/maps/api/streetview/metadata?'
image_endpoint = 'https://maps.googleapis.com/maps/api/streetview?'

indexToYMapping = {0: 0, 1: 15, 2: 35, 3: 20}
    

def getPanoramaAt(lat, long):
    url = metadata_endpoint + f'location={lat},{long}&key={key}'
    response = urllib.request.urlopen(url).read()
    image_available = json.loads(response).get('status') == 'OK'
    if not image_available:
        print(f'image not available at {lat}, {long}')
        return
    canvas = Image.new('RGB', (4 * 640, 640))
    for heading in range(0, 360, 90):
        print(f'Fetching {lat},{long} -- heading {heading}')
        url = image_endpoint + f'size=640x640&location={lat},{long}&heading={heading}&fov=90&key={key}'
        img =  Image.open(urllib.request.urlopen(url))
        x = int((heading / 90) * 640)
        y = indexToYMapping.get(int(heading/90))
        canvas.paste(img, (x, y))
    maxDepression = max(list(indexToYMapping.values()))
    width, height = canvas.size
    canvas.crop((0, maxDepression, width, height)).show()

getPanoramaAt(40.457375,-80.009353)

