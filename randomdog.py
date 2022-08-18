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


def buttun():
    '''create button'''
    btn = [
        [{'text': 'random 🐶'}]
    ]
    return btn


def keyboard():
    '''create keyboard'''
    kbd = {
        'keyboard': buttun()
    }
    return kbd


def send_message(chat_id: int, text: str):
    '''send to someone a message with button.'''

    payload = dict([('chat_id', chat_id), ('text', text), ('reply_markup', keyboard())])

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    r = requests.post(url=url, json=payload)


chat_id = 1258594598
text = 'ok'

send_message(chat_id, text)