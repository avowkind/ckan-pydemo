from ckanapi import RemoteCKAN
from ckanloc import ckan_url, API_KEY, ua

import pprint
pp = pprint.PrettyPrinter(indent=2)

ckan = RemoteCKAN(ckan_url, user_agent=ua, apikey=API_KEY)

# show a specific result
package = ckan.action.package_show(id="lure-dispenser-comparison-trial")
pp.pprint(package)

