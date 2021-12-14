import requests
import config

key = config.API_KEY
baseURL = 'http://api.collegefootballdata.com/'
headers = {'Content-Type': 'application/json',
           'Authorization': key}

def search(term):
    url = baseURL + f'player/search?searchTerm={term}'
    response = requests.get(url, headers=headers)
    print(response.json())

search('Walker')