import requests

api_root = 'https://swapi.co/api'
ipstack_api_key = '31c096b05a1f4bf47496cf89d08f17ee'

def get_character_name(id):
    url = f'{api_root}/people/{id}'
    name = requests.get(url).json()['name']
    return name

def get_ip():
    my_ip = requests.get('https://api.ipify.org?format=json').json()['ip']
    return my_ip

def ip_info(info):
    my_ip = get_ip()
    response = requests.get(f'http://api.ipstack.com/{my_ip}?access_key={ipstack_api_key}').json()
    if info == 'flag':
        return response['location']['country_flag']
    return response[info]
