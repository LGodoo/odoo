# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import time
import calendar
import logging
_logger = logging.getLogger(__name__)

class AccountBankStatement(models.Model):
    _inherit = 'account.bank.statement'

    def update_statement_lines(self):
        url = "https://sandbox-apis.bankofcyprus.com/df-boc-org-sb/sb/psd2/oauth2/token"
        payload = "grant_type=client_credentials&client_id=3e69aa6f-0245-4e11-8aa0-5ed162b1fe84&client_secret=N1aL2kL0sH6hG4tP3uS0vV6rF2fM6bR5aD0nM8gQ0kV7nN6xP6&scope=TPPOAuth2Security"
        urlstate = "https://sandbox-apis.bankofcyprus.com/df-boc-org-sb/sb/psd2/v1/accounts/351012345671/statement?client_id=3e69aa6f-0245-4e11-8aa0-5ed162b1fe84&client_secret=N1aL2kL0sH6hG4tP3uS0vV6rF2fM6bR5aD0nM8gQ0kV7nN6xP6&startDate=20/11/2017&endDate=21/11/2017&maxCount=1"
        timestamp = str(calendar.timegm(time.gmtime()))
        headers = {
            'content-Type': "application/x-www-form-urlencoded",
            'accept': "application/json",

        }

        response = requests.post(url, payload, headers=headers)
        bearer_token = "Bearer " + response.json()['access_token']
        print('token :' + bearer_token)
        print(response.json())
        error_msg = 'BoC API response: %s' % (response.json())
        _logger.info(error_msg)


        headersstate = {
            'authorization': bearer_token,
            'subscriptionId': 'Subid000001-1564047081590',
            'content-type': "application/json",
            'journeyid': "LGT",
            'originuserid': "1234",
            'timestamp': timestamp,
            'tppid': "singpaymentdata"

        }
        response4 = requests.get(urlstate, headers=headersstate)
        print('Statement of account:')
        print(response4.json())
        error_msg = 'BoC API response: %s' % (response4.json())
        _logger.info(error_msg)

        if response4.status_code == 200:
            bs_model = self.env['account.bank.statement']
            bsl_model = self.env['account.bank.statement.line']
            line_env = self.env['account.bank.statement.line']
            for wizard in self:
                    for what in wizard.entries:
                        new_line = line_env.create({
                            'name': what.name.id,
                            'order_id': what.sale_order_id.id,
                            'product_uom': what.product_id.uom_id.id})
                        new_line.product_id_change()  # Calling an onchange method to update the record


        else:
            error_msg = 'Failed to retrieve bank statement data'
            _logger.info(error_msg)
