from ckan_api_client.high_level import CkanHighlevelClient
from ckan_api_client.objects import CkanDataset
from ckan import ckan_url, API_KEY

import pprint
pp = pprint.PrettyPrinter(indent=2)


if __name__ == "__main__":
  ds = ckan_client.list_datasets()
  print(ds)

  # for ds in ckan_client.iter_datasets():
  #   print(ds)

  # get dataset by name
  myds = 'the-goat-picture'  
  rua = ckan_client.get_dataset_by_name(myds)
  print(rua)

  # list organisations
  # orgs = ckan_client.list_organizations()
  # print(orgs)

  #get PFR organisation information
  # pfr = ckan.action.organization_show(id='plant-and-food-research-nz', include_datasets=True)
  # print( pfr['display_name'], pfr['package_count'], 'datasets')

  # datasets = pfr['packages']
  # for d in datasets: 
  #   print (d['name'])  
  #   dataset = ckan.action.package_show(id=d['id'])
  #   for r in dataset['resources']:
  #     print( r['name'], r['format'], r['url'])
    
  # list public packages
  # packages = ckan.action.current_package_list_with_resources()
  # pp.pprint(packages)

  # just print package titles.
  # titles = list(map(lambda p: p['title'], packages))
  # pp.pprint(titles)

  # list packages for organization


  # datasets = ckan.action.organization_list()
  # pp.pprint(datasets)