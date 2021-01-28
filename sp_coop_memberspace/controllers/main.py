# coding: utf-8

from datetime import date, datetime

import openerp
from openerp import fields
from openerp.addons.web import http
from openerp.http import request


class Website(openerp.addons.coop_memberspace.controllers.main.Website):

    @http.route()
    def index(self, **kwargs):
        user = request.env.user

        # Get next shift
        shift_registration_env = request.env['shift.registration']
        today = date.today()
        shift_registration = shift_registration_env.sudo().search([
            ('shift_id.shift_template_id.is_technical', '=', False),
            ('partner_id', '=', user.partner_id.id),
            ('state', '!=', 'cancel'),
            ('date_begin', '>=', datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'))
        ], order="date_begin", limit=1)

        # Get next shift week number
        if shift_registration:
            weekA_date = fields.Date.from_string(request.env.ref('coop_shift.config_parameter_weekA').value)
            next_shift_date = fields.Date.from_string(shift_registration.date_begin)
            week_number = 1 + (((next_shift_date - weekA_date).days // 7) % 4)
            week_number_chr = chr(week_number + 64)
        else:
            week_number_chr = False

        result = super(Website, self).index(**kwargs)
        result.qcontext['next_shift_week_number'] = week_number_chr
        return result

    @http.route('/planning', type='http', auth='user', website=True)
    def page_planning(self, **kwargs):
        user = request.env.user
        upcoming_shifts = request.env['shift.shift'].sudo().search([
            ('shift_template_id.is_technical', '=', False),
            ('date_begin', '>=', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            ('state', '=', 'confirm'),
        ], order="date_begin") or []
        return request.render(
            'coop_memberspace.planning',
            {
                'user': user,
                'shift_type': user.partner_id.shift_type,
                'upcoming_shifts': upcoming_shifts,
            }
        )
