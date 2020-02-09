# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def write(self, vals):
        # store original related users login
        users_login = {}
        if 'email' in vals:
            for partner in self:
                if partner.email:
                    user_related = self.env['res.users'].search([
                        ('partner_id', '=', partner.id)
                    ])
                    users_login[partner.id] = user_related.login

        res = super(ResPartner, self).write(vals)

        # restore related users email after update done by email_validation_check (parent) module
        for partner_id, user_login in users_login.items():
            user_related = self.env['res.users'].search([
                ('partner_id', '=', partner_id)
            ])
            user_related.write({
                'login': user_login
            })

        return res