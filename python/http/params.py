import requests

url = 'https://icanhazdadjoke.com/search'
search_term = input('What do you want to search for? ')

response = requests.get(
    url,
    headers={
        'Accept': 'application/json'
    },
    params={
        'term': search_term,
        'limit': 1
    }
)

data = response.json()

print(data['results'])
