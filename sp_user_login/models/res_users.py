# coding: utf-8

from openerp import api, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.onchange('login')
    def on_change_login(self, cr, uid, ids, login, context=None):
        """
        Avoids res_users.email to take res_users.login value
        """
        return {}
