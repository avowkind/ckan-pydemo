# ckan-pydemo
Test and demonstration of python clients##  for CKAN

Purpose: show how python users can create scripts or functions to create and update metadata records in CKAN and upload resources. 


There are two api clients 

## __ckanapi__: Simple Python wrapper around the CKAN action API

    pip install ckanapi

ckanapi is the most generically useful. It works with Python 3 and can be used as a command line or module.

## ckan-api-client: an improved client for the Ckan API

    pip install ckan-api-client

Providing a a low-level client, a high-level client, a synchronization client and it attempts to get work around some common issues with that API 

Requires Python 2.x.x  
    
ckan-api-client is friendlier. you can load and manipulate datasets in local python objects before uploading.  However, I am not sure if it handles custom data set schemas correctly. 

# Example files

__ckanloc.py__: set the local ckan url and API key 

__list1.py__ demonstrates read only calls using ckanapi
__list2.py__ demonstrates read only calls using ckan-api-client.

__create.py__ demonstrates loading a dataset and associated resource from a json file. 
This json file is the format exported by the Excel Metadata reader in ckan_collector.

# ckanapi command line examples
In most cases we can achieve our goals using the command line api. 
All the api calls available are documented at https://docs.ckan.org/en/ckan-2.7.3/api/


    ckanapi action group_list -r http://localhost:5000 
    ckanapi action package_list -r http://localhost:5000
    ckanapi action current_package_list_with_resources -r http://localhost:5000
    ckanapi action revision_list -r http://localhost:5000
    ckanapi action package_revision_list id="lure-dispenser-comparison-trial" -r http://localhost:5000
    ckanapi action organization_list -r http://localhost:5000
    ckanapi action organization_list all_fields="True" -r http://localhost:5000
    ckanapi action organization_list all_fields="True" include_users="True" -r http://localhost:5000
    ckanapi action package_show id="lure-dispenser-comparison-trial" -r http://localhost:5000
    ckanapi action search-index rebuild -r http://localhost:5000
    ckanapi action package_search q=lure -r http://localhost:5000 | ckanapi delete datasets -r http://localhhost:5000 -a "03511628-ff4e-47a6-abc0-afa971004c83"

## Using jq to filter 
JQ is a useful command line filter that reads and writes json. 
https://stedolan.github.io/jq/

This example uses the ckan api to search for items matching the work lure and then filters out the titles.

    ckanapi action package_search q=lure -r http://localhost:5000 | jq '.results | .[] | .id .title' 
 
## Delete requires an api key
key functions require authorisation. THis is indicated by including the api key in the parameters

    ckanapi delete datasets "207e12e6-9fec-4ed4-bc67-6e8527e2ce9a" -r http://localhost:5000 -a "03511628-ff4e-47a6-abc0-afa971004c83"


# Dependencies

cuid - used to generate non colliding test data.

    pip install cuid.py 