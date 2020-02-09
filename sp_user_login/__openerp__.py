# coding: utf-8
{
    'name': "SP Preserve User Login",

    'summary': """Supercoop Preserve User Login """,

    'description': """
        Surcharge le Email Validation Check de La Louve :
            - n'update pas le login du res_users associé au res_partner lorsque l'email du res_partner est modifié (car le login supercoop doit être conservé pour l'authentification Google)
            - Lorsque res_users.login est édité via le formulaire, res_users.email ne prend pas sa valeur.
    """,

    'author': "Supercoop",
    'website': "http://www.supercoop.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Supercoop',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': [
        'email_validation_check',
    ],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
