# -*- coding: utf-8 -*-
# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'POS Margin',
    'version': '9.0.2.0.0',
    'category': 'Point Of Sale',
    'sequence': 1,
    'author': "Adaptation pour Supercoop (basée sur la v12),"
              "GRAP,"
              "Odoo Community Association (OCA)",
    'summary': 'Margin on PoS Order',
    'depends': [
        'point_of_sale',
        'sale_margin',
    ],
    'data': [
        'views/view_pos_order.xml',
        'report/report_pos_order_margin.xml',
    ],
    'installable': True,
}
