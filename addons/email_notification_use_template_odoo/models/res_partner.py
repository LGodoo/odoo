# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def _notify_by_email(self, message, force_send=False, send_after_commit=True, user_signature=True):
        if not message.mapped('subtype_id.template_id'):
            return super(Partner, self)._notify_by_email(message, force_send=force_send,
                                                         send_after_commit=send_after_commit,
                                                         user_signature=user_signature)
        message_ids = []
        for me in message:
            if not me.subtype_id.template_id:
                super(Partner, self)._notify_by_email(me, force_send=force_send, send_after_commit=send_after_commit,
                                                      user_signature=user_signature)
                continue
            for this in me.notification_ids:
                custom_values = {
                    'references': me.parent_id.message_id,
                    'author_id': me.author_id.id
                }
            message_id = me.subtype_id.template_id.send_mail(this.id, force_send=True)
            message_ids.append(message_id)

        return True
