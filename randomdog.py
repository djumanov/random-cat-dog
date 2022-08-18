import requests

TOKEN = '2052338771:AAHWqySU9KeCy3P_7i-2cLm3Fn78dLKG2RY'


def get_update() -> dict:
    '''get last update message.'''

    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    r = requests.get(url=url)

    if r.status_code == 200:
        last_message = r.json()['result'][-1]

        return last_message
    return False

print(get_update())