import requests

# HEADER: Learning JSON and venv
# when?: if i want to extract data and import it into my site to reflect today's fashion trends

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

print(json)

print('The people currently in space are:')
for p in json['people']:
    print(p['name'])


