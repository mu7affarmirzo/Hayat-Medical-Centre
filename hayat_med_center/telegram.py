import urllib.parse

import requests

token = '7021329823:AAET3UFXbvACrlGoRMg0snUx8_1avvDSq1M'
procedures_bot_token = '7859364799:AAHHN5C-sPb5FaB0-WuXZ9cDRkY9W5gaq2U'

destinations = {
        'procedures': {
            'bot_token': procedures_bot_token,
            # 'chat_id': '-1002442945666',
            'chat_id': '-1001583913039',
        },
        'pills': {
            'bot_token': '',
            'chat_id': '-4558791978',
        },
        'food': {
            'bot_token': '',
            'chat_id': '-4558791978',
        },
        'labs': {
            'bot_token': '',
            'chat_id': '-4558791978',
        }
    }


def notify(msg, address, chat_id='-4558791978', parse_mode='HTML', encode=False):
    if encode:
        msg = urllib.parse.urlencode({'!!! NOTIFY\n': msg})

    chat_id = destinations.get(address).get('chat_id')
    target_token = destinations.get(address).get('bot_token')

    url = f'https://api.telegram.org/bot{target_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': msg,
        'parse_mode': parse_mode
    }

    try:
        requests.get(url, params=params)
    except:
        pass


def get_update():
    payload = f'https://api.telegram.org/bot{token}/getUpdates'
    response = requests.get(payload).json()

    update_id = 0
    if response['ok']:
        for update in response['result']:
            update_id = update['update_id']

    payload = f'https://api.telegram.org/bot{token}/getUpdates?offset={update_id}'
    requests.get(payload).json()

    return response

