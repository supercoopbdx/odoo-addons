# coding: utf-8
{
    'name': "SP Coop Memberspace",
    'summary': "Supercoop - Modify original coop memberspace module",
    'description': """
        Customise le module coop memberspace de La Louve :
            - ajout du numéro de semaine correspondant au prochain service sur la homepage
            - ajout d'un warning si pas de prochain service programmé sur la homepage
    """,
    'author': "Supercoop",
    'website': "http://www.supercoop.fr",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Supercoop',
    'version': '9.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': [
        'coop_memberspace',
    ],
    # always loaded
    'data': [
        'views/website/website_homepage.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}