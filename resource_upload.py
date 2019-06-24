from ckanapi import RemoteCKAN
from ckanloc import ckan_url, API_KEY, ua
import pprint
from cuid import cuid

pp = pprint.PrettyPrinter(indent=2)
import json

# allow multiple records from the test dataset by changing the title and name.
ckan = RemoteCKAN(ckan_url, user_agent=ua, apikey=API_KEY)
cuid = cuid()  # generates a unique code

resource_dict = {
    'name':'example.csv',
    # 'url':'',
    'description':'some misc data about vines',
    'format':'CSV'
}

with open('test_dataset.json') as json_file:  
    dataset = json.load(json_file)
    dataset["name"] = dataset["name"] + "_" + cuid
    dataset["title"] = dataset["title"] + " " + cuid
    package = ckan.action.package_create(**dataset) 
    pp.pprint(package['id'])
    new_resource = ckan.action.resource_create(
      package_id=package['id'],
      name='example.csv',
      description='some misc data about vines',
      format='CSV',
      upload=open('./example.csv')
      )