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
        [{'text': 'cat 😺'}],
        [{'text': 'random 🐶'}],
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


def get_dog():
    '''get random dog.'''

    url = 'https://random.dog/woof.json'
    r = requests.get(url=url)

    if r.status_code == 200:
        dog = r.json()['url']

        return dog


def get_cat():
    '''get cat's photo url'''

    url = 'https://aws.random.cat/meow'
    r = requests.get(url=url)

    if r.status_code == 200:
        cat = r.json()['file']

        return cat


def send_photo(chat_id: int, text: str):
    '''send to someone a photo.'''
    if text == 'cat 😺':
        photo = get_cat()
    else:
        photo = get_dog()

    payload = dict([('chat_id', chat_id), ('photo', photo)])

    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    r = requests.post(url=url, json=payload)


def main():
    update_id = get_update()['update_id']
    while True:
        curr_msg = get_update()
        curr_update_id = curr_msg['update_id']
        
        if update_id != curr_update_id:
            chat_id = curr_msg['message']['from']['id']
            text = curr_msg['message']['text']

            if text == '/start':
                send_message(chat_id, "welcome!, press the buttun.")
            elif text == 'cat 😺':
                send_photo(chat_id, text)
            elif text == 'random 🐶':
                send_photo(chat_id, text)
            
            update_id = curr_update_id

main()