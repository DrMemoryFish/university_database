import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '07788237363',
        'message': 'Hello world',
        'key': '03cfca22462f6552c384b2dceb111952f32bd2baxb6wOawYdyRPbntFeOJsWLhfc',
    })
    print(resp.json())

schedule.every().day.at("04.00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)