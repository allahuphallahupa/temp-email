import requests
import json

'''
Class that creates temp e-mail an receives mails (letters) from it.
After getting mails you should delete e-mail via function delete_mail(), because  "post-shift" has e-mail count limit.
'''


class TempMail(object):
    url = "https://post-shift.ru/api.php"

    def __init__(self):
        params = {
            'action': 'new',
            'type': 'json'}
        response = requests.get(self.url, params=params)            # creates email
        json_text = json.loads(response.text)
        try:
            self.email = json_text['email']
            self.key = json_text['key']
            print("Email created")
        except Exception:
            raise SystemExit(json_text['error'])

    def get_email_address(self):
        return self.email

    def get_mails(self):
        """
        requests list of mails and returns it
        :return: str
        """
        params = {
            'action': 'getlist',
            'key': self.key,
            'type': 'json'
        }
        response = requests.get(self.url, params=params)
        letters = json.loads(response.text)
        print("got list of letters")
        return letters

    def delete_email(self):
        params = {
            "key": self.key,
            "delete": "ok"
        }
        response = requests.get(self.url, params=params)
        print("email deleted")
