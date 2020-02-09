# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
# import openerp.addons.auth_signup.res_users as resUsers


class res_users(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        # TODO Permettre la configuration du parametre depuis l'interface d'administration
        user = super(res_users, self.with_context(no_reset_password=True)).create(vals)

        return user
