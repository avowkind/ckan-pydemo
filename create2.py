from ckan_api_client.high_level import CkanHighlevelClient
from ckan_api_client.objects import CkanDataset

API_Key = "cdc0284b-47c9-48ff-8a17-5861259c5a03"
# ckan_url = "https://demo.ckan.org"
ckan_url = "http://localhost:5000"
# ckan_url = "http://ckan.dev.pfe.co.nz"
ua = 'ckanapiexample/1.0 (+http://pfr.co.nz/)'

client = CkanHighlevelClient(ckan_url, api_key=API_Key)

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
  "name": "lure-dispenser-comparison-trial2",
  "title": "Lure Dispenser comparison trial, thrips, Australia, Perth",
  "notes": "Assess three thrips Lure delivery mechanisms:\n\n* P Paint pen\n* D Deer wick\n* C Control (no wick)",
  "private": False,
  "owner_org": "plant-and-food-research-nz",
  "author": "Mette Nielson",
}

dataset_dict2 = {
  "name": "lure-dispenser-comparison-trial",
  "title": "Lure Dispenser comparison trial, thrips, Australia, Perth",
  "notes": "Assess three thrips Lure delivery mechanisms:\n\n* P Paint pen\n* D Deer wick\n* C Control (no wick)",
  "private": False,
  "owner_org": "plant-and-food-research-nz",
  "state": "active",
  "project_code": "P/1234",
  "author": "Mette Nielson",
  "project_leader_email":	"Mette.Nielson@plantandfood.co.nz",
  "data_steward": "Mette Nielson",
  "data_steward_email": "Mette.Nielson@plantandfood.co.nz",
  "other_researcher":	"David Teulon",
  "biometrician": "Ruth Butler",
  "credits": "Mel Walker",
  "license_id" : "PFR Internal Use only"
}

new_dataset = client.create_dataset(CkanDataset(dataset_dict))

print(new_dataset)
