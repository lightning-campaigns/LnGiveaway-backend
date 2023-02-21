
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import requests
import json

from api.helper.application_configs import ApplicationConstant


class LNbits():

    def ln_url_parser(self, ln_url):
        parse_result = urlparse(ln_url)
        dict_parse_result = parse_qs(parse_result.query)
        user = dict_parse_result["usr"][0]
        wallet_id = dict_parse_result["wal"][0]
        return {user: user, wallet_id: wallet_id}

    def get_new_wallet_url(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        q_card_section = soup.find('q-card-section', attrs = {'class':'text-center'})
        qrcode = q_card_section.find('qrcode')
        ln_url = qrcode.attrs[':value'].replace("'", "").replace("+", "").replace(" ", "")
        result = {}
        q_expansion_item = soup.find('q-expansion-item')
        find_all = q_expansion_item.find_all('em')
        key_list = []
        for q_card in find_all:
            key_list.append(q_card.text)
        result['wallet_id'] = key_list[0]
        result['admin_key'] = key_list[1]
        result['invoice_key'] = key_list[2]
        result['ln_url'] = ln_url
        return result

    def create_ln_url(self, username):
        headers = {"Content-Type": "application/json"}
        response = requests.get(ApplicationConstant.ln_instant_wallet_url+username, headers=headers)
        html_content = response.__dict__['_content']
        return self.get_new_wallet_url(html_content)

    def create_ln_invoice(self, username, new_wallet):
        headers = {"Content-Type": "application/json", "X-Api-Key": new_wallet.get('invoice_key')}
        payload = {
            "out": False,
            "amount": ApplicationConstant.amount_to_disburse,
            "memo": ApplicationConstant.payment_narration,
        }
        response = requests.post(ApplicationConstant.ln_invoice_url, json=payload, headers=headers)
        if (response.status_code == 201):
            return json.loads(response.text).get('payment_request')
        else:
            raise Exception("Error Creating Invoice")

    def pay_ln_invoice(self, payment_request, access_token):
        print("+++++++", payment_request)
        print("+++++++", access_token)
        headers = {"Content-Type": "application/json", "X-Api-Key": access_token}
        payload = {"out": True, "bolt11": payment_request}
        response = requests.post(ApplicationConstant.ln_invoice_url, json=payload, headers=headers)
        print(response)
        if (response.status_code == 201):
            print("+++++++++++++ ", json.loads(response.text))
        else:
            raise Exception("Error Paying Invoice")

    def create_withdrawal(self, access_token):
        headers = {"Content-Type": "application/json", "X-Api-Key": access_token}
        payload = {
            "title": ApplicationConstant.payment_narration,
            "min_withdrawable": ApplicationConstant.amount_to_disburse,
            "max_withdrawable": ApplicationConstant.amount_to_disburse,
            "uses": 1,
            "wait_time": 600000,
            "is_unique": True
        }
        response = requests.post(ApplicationConstant.ln_withdraw_url, json=payload, headers=headers)
        print(">>>>1 ", access_token)
        print(">>>>2 ", payload)
        if (response.status_code == 201):
            return json.loads(response.text).get('lnurl')
        else:
            raise Exception("Error Creating Withdrawal")



