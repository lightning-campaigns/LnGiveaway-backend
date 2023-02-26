import os
from dotenv import load_dotenv

load_dotenv()

class ApplicationConstant:
    min_amount_to_disburse = os.environ['MIN_AMOUNT_TO_DISBURSE']
    max_amount_to_disburse = os.environ['MAX_AMOUNT_TO_DISBURSE']
    amount_to_disburse = os.environ['AMOUNT_TO_DISBURSE_IN_SAT']
    payment_narration = os.environ['PAYMENT_NARRATION']
    ln_instant_wallet_url = os.environ['CREATE_LN_INSTA_WALLET_URL']
    ln_invoice_url = os.environ['CREATE_LN_INVOICE_URL']
    ln_withdraw_url = os.environ['CREATE_LN_WITHDRAW_URL']
    send_withdrawal_link = os.environ['SEND_WITHDRAWAL_AS_LINK']
    send_withdrawal_photo = os.environ['SEND_WITHDRAWAL_AS_PHOTO']
    port = os.environ['PORT']
    sqlalchemy_database_uri = os.environ['SQLALCHEMY_DATABASE_URI']
    sqlalchemy_track_modifications = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
    app_secret_key = os.environ['APP_SECRET_KEY']
    twitter_consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    twitter_consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    twitter_access_key = os.environ['TWITTER_ACCESS_KEY']
    twitter_access_secret = os.environ['TWITTER_ACCESS_SECRET']
    ln_api_key = os.environ['LN_API_KEY']