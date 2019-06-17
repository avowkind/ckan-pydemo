from ckanapi import RemoteCKAN
from ckanloc import ckan_url, API_KEY, ua

import pprint
pp = pprint.PrettyPrinter(indent=2)

ckan = RemoteCKAN(ckan_url, user_agent=ua, apikey=API_KEY)

# list groups
groups = ckan.action.group_list()
print(groups)

