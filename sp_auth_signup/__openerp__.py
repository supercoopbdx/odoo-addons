# -*- coding: utf-8 -*-
{
    'name': "SP Auth Signup",

    'summary': """Supercoop Auth Signup """,

    'description': """
        Surcharge le Auth Signup original:
            - Désactive les notifications par mail lors de la création/import d'un utilisateur
    """,

    'author': "Supercoop",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Supercoop',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'base_setup',
        'mail',
        'web',
        'auth_signup'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/templates.xml',
        # 'views/openacademy.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
