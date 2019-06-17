from ckanapi import RemoteCKAN
from ckanloc import ckan_url, API_KEY, ua

import pprint
pp = pprint.PrettyPrinter(indent=2)

ckan = RemoteCKAN(ckan_url, user_agent=ua, apikey=API_KEY)

#get PFR organisation information
pfr = ckan.action.organization_show(id='plant-and-food-research-nz', include_datasets=True)
print( pfr['display_name'], pfr['package_count'], 'datasets')

# datasets = pfr['packages']
# for d in datasets: 
#   print (d['name'])  
#   dataset = ckan.action.package_show(id=d['id'])
#   for r in dataset['resources']:
#     print( r['name'], r['format'], r['url'])
  
# list public packages
packages = ckan.action.current_package_list_with_resources()
pp.pprint(packages)

# just print package titles.
titles = list(map(lambda p: p['title'], packages))
pp.pprint(titles)

