from ckanapi import RemoteCKAN
from ckanloc import ckan_url, API_KEY, ua
import pprint
from cuid import cuid

pp = pprint.PrettyPrinter(indent=2)

# allow multiple records from the test dataset by changing the title and name.
ckan = RemoteCKAN(ckan_url, user_agent=ua, apikey=API_KEY)
cuid = cuid()  # generates a unique code

# Note Update only works if the resource is already present

resource_dict = {
    'id': '5b75fdf2-df9c-4a4f-bb28-d78ea7bc4e48',
    'package_id': 'cdcf576d-0b09-4df0-a506-61a7142d2b8f',
    'name':'Restaurantes con PYTHON',
    'url':'http://82.98.156.2/ckan_api/public_html/restaurantes.geojson',
    'description':'Description in  PYTHON',
    'format':'GEOJSON'
}
ckan.action.resource_update(**resource_dict)