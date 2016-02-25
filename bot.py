"""
Simple Telegram bot class
Written by Dallas Johnson
This simple bot supports most of the methods of Telegram's bot API.
Bad requests sent return a value of -1, and any successful requests return the value of the request that was sent.
This is a barebones bot API. To use it, simply run getupdates() in your script's main loop.
"""

import requests


class Bot:
    api_token = None
    requrl = 'https://api.telegram.org/bot{0}'.format(api_token)
    botname = ""

    def __init__(self, api_key, botname="GenericBot"):
        self.api_token = api_key
        self.requrl = 'https://api.telegram.org/bot{0}'.format(self.api_token)
        self.botname = botname

    def getupdates(self):
        r = requests.post(self.requrl + 'getUpdates').json()
        if not r['ok']:
            return -1
        if r['result'] == []:
            return 0
        update_id = r['result'][len(r['result']) - 1]['update_id']
        requests.post(self.requrl + 'getUpdates', data={'offset': update_id + 1})
        return r

    def sendmessage(self, chat_id, message_text):
        r = requests.post(self.requrl + 'sendMessage', data={'chat_id': chat_id, 'text': message_text}).json()
        if not r['ok']:
            return -1
        return r

    def forwardmessage(self, chat_id, from_id, message_text, silent=False):
        r = requests.post(self.requrl + 'forwardMessage', data={'chat_id': chat_id,
                                                                'from_chat_id': from_id,
                                                                'disable_notification': silent,
                                                                'message_id': message_text}).json()
        if not r['ok']:
            return -1
        return r

    def sendreply(self, chat_id, message_text, user_id):
        r = requests.post(self.requrl + 'sendMessage',
                          data={'chat_id': chat_id,
                                'text': message_text,
                                'reply_to_message_id': user_id}).json()
        if not r['ok']:
            return -1
        return r

    def sendphoto(self, chat_id, photo, caption_text=""):
        r = requests.post(self.requrl + 'sendPhoto', data = {'chat_id': chat_id,
                                                             'photo': photo,
                                                             'caption': caption_text}).json()
        if not r['ok']:
            return -1
        return r

    def sendaudio(self, chat_id, audio, caption_text=""):
        r = requests.post(self.requrl + 'sendAudio',data = {'chat_id': chat_id,
                                                            'audio': audio,
                                                            'caption': caption_text}).json()
        if not r['ok']:
            return -1
        return r

    def sendfile(self, chat_id, file, caption_text=""):
        r = requests.post(self.requrl + 'sendDocument', data={'chat_id': chat_id,
                                                              'file': file,
                                                              'caption': caption_text}).json()
        if not r['ok']:
            return -1
        return r

    def sendsticker(self, chat_id, sticker, caption_text=""):
        r = requests.post(self.requrl + 'sendSticker', data={'chat_id': chat_id,
                                                             'sticker': sticker,
                                                             'caption': caption_text}).json()
        if not r['ok']:
            return -1
        return r

    def sendvideo(self, chat_id, video, caption_text=""):
        r = requests.post(self.requrl + 'sendVideo', data={'chat_id': chat_id,
                                                           'video': video,
                                                           'caption': caption_text}).json()
        if not r['ok']:
            return -1
        return r

    def getprofilephotos(self, user_id):
        r = requests.post(self.requrl + 'getUserProfilePhotos', data={'user_id': user_id}).json()
        if not r['ok']:
            return -1
        return r

    def getme(self):
        r = requests.post(self.requrl + 'getMe').json()
        if not r['ok']:
            return -1
        return r
