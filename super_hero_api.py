import requests
import json
from pprint import pprint
from logger2 import logger

@logger('superhero.log')
def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    heroes_names = ['Hulk', 'Captain America', 'Thanos']
    url_hero = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url_hero)
    intellegent = 0
    for hero in response.json():
        if hero.get('name', '') in heroes_names:
            if hero.get('powerstats', {}).get('intelligence') > intellegent:
                intellegent = hero.get('powerstats', {}).get('intelligence')
                the_smartest_superhero = hero.get('name', '')       
    return the_smartest_superhero


def get_the_smartest_superhero1(superheros:list)-> str:
    the_smartest_superhero = ''
    base_url = 'https://akabab.github.io/superhero-api/api'
    max_intellegent = 0
    for superhero_id in superheros:
        url = f"{base_url}/id/{superhero_id}.json"
        response = requests.get(url)
        info = response.json()
        if info.get('powerstats', {}).get('intelligence') > max_intellegent:
            max_intellegent = info.get('powerstats', {}).get('intelligence')
            the_smartest_superhero = info.get('name', '')    
    return the_smartest_superhero

print(get_the_smartest_superhero())
print(get_the_smartest_superhero1([332, 149, 655]))