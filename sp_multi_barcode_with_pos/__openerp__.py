# -*- coding: utf-8 -*-
# Copyright (C) 2016-Today: La Louve (<http://www.lalouve.fr/>)
# @author: La Louve
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html


{
    'name': 'Multi code barre Supercoop',
    'version': '9.0.1.0.0',
    'category': 'Point Of Sale',
    'summary': 'Un module pour avoir plusieurs codes barre pour un produit, avec reconnaissances depuis la caisse. fork du module sp_multi_barcode_with_pos',
    'author': 'La Louve et supercoop',
    'website': 'http://supercoop.fr',
    'depends': [
        'point_of_sale', 'product'
    ],
    'data': [
        # security
        'security/ir.model.access.csv',
        'views/product_product_view.xml',
        'static/src/xml/templates.xml',
    ],
    'installable': True,
}
