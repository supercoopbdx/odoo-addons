# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ResetPassword(models.TransientModel):
    _name = "reset.password"


    @api.multi
    def multi_reset_password(self):
        if self._context.get('active_ids',False):
            user_ids = self.env['res.users'].browse(self._context.get('active_ids'))
            for user in user_ids:
            	if user.active:
                	user.action_reset_password()
