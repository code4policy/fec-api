import requests
import json
import os


# 
base_url = 'https://api.open.fec.gov/v1/'

# 
operation = 'candidate'

# 
key = os.environ['FECKEY']

#
api_parameters = {'api_key': key, 'office':'H', 'sort':'name', 'state':'MA', 'election_year':[2022]}

# 
response = requests.get(base_url + operation, params = api_parameters)

# 
print('Response Code: {0}\n'.format(response.status_code))
data = json.loads(response.text)

# 
with open('fec_api_results.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)

# 
for candidate in data['results']:
    print(candidate['name'])
