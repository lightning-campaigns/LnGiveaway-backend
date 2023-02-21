import tweepy

from api.helper.application_configs import ApplicationConstant
from helper import Helper
from lnbit import LNbits



class Bot():

    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, LN_ACCESS_KEY):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.ACCESS_KEY = ACCESS_KEY
        self.ACCESS_SECRET = ACCESS_SECRET
        self.LN_ACCESS_KEY = LN_ACCESS_KEY

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

        self.lnbits = LNbits()

    def get_retweets_list(self):
        tweetObj = self.api.get_retweets_of_me()[0].__dict__
        tweetObjJson = tweetObj['_json']
        tweetId = tweetObjJson['id']
        return self.api.get_retweets(tweetId)

    def generate_retweeter_invoice(self, username, new_wallet):
        return self.lnbits.create_ln_invoice(username, new_wallet)

    def pay_retweeter_invoice(self, payment_request, access_token):
        self.lnbits.pay_ln_invoice(payment_request, access_token)

    def create_retweeter_withdraw(self, access_token):
        return self.lnbits.create_withdrawal(access_token)

    def send_retweeters_dm(self):
        for retweet in self.get_retweets_list():
            screen_name = retweet.user.screen_name #the screen names of the retweeters
            print(screen_name)
            retweeterId = retweet.user.id  # the ID of the tweeter
            if not retweeterId == 1579128080483991552:
                # new_wallet = self.lnbits.create_ln_url(screen_name)
                new_wallet ={'wallet_id': '37c42f29847c450680d3df9ae4d8c550', 'admin_key': 'ae45caafca574f61bc2d0cc93a2a21ff', 'invoice_key': 'ee48570ce1b84384a68c94642cadea4b', 'ln_url': 'https://legend.lnbits.com/wallet?usr=4898944ccce64cb8be2189fa9fd14cf6&wal=37c42f29847c450680d3df9ae4d8c550'}
                # retweeter_invoice = self.generate_retweeter_invoice(screen_name, new_wallet)
                # retweeter_invoice = self.pay_retweeter_invoice(payment_request=retweeter_invoice, access_token=self.LN_ACCESS_KEY)
                if ApplicationConstant.send_withdrawal_link:
                    withdrawal_invoice = self.create_retweeter_withdraw(new_wallet['admin_key'])
                    helper = Helper()
                    helper.generateQR(screen_name, withdrawal_invoice)
                    # direct_message = self.api.send_direct_message(retweeterId, new_wallet.get("ln_url"))
                # elif ApplicationConstant.send_withdrawal_photo:
                    # direct_message = self.api.send_direct_message(retweeterId, new_wallet.get("ln_url"))

                # print("<<<<<< new_wallet_url>>>>>>", retweeter_invoice)
                # print(direct_message)
