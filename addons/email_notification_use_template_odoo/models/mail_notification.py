# -*- coding: utf-8 -*-
# © 2016 V8 Therp BV, @2017 V10 Wujun Wang,Haibin Zhou,Stella Fredö
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from lxml import etree
from odoo import api, fields, models


class MailNotification(models.Model):
    _inherit = 'mail.notification'

    record = fields.Reference(
        selection=lambda self: [
            (m.model, m.name) for m in self.env['ir.model'].search([])
        ],
        compute='_compute_record')
    record_access_link = fields.Char(compute='_compute_record')

    @api.multi
    def _compute_record(self):
        for this in self:
            if not this.mail_message_id.model or not this.mail_message_id.res_id:
                continue
            this.record = self.env[this.mail_message_id.model].browse(
                this.mail_message_id.res_id)
            this.record_access_link = self.env['mail.thread']._notification_link_helper('view',
                                                model=this.mail_message_id.model, res_id=this.mail_message_id.res_id)
