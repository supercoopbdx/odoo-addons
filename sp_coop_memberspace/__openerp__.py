# coding: utf-8
{
    'name': "SP Coop Memberspace",
    'summary': "Supercoop - Modify original coop memberspace module",
    'description': """
        Inscription à un service (volant ou rattrapage) possible depuis la page planning
        Ajout de la page planning par Supercoop pour visualiser les prochains services confirmés avec le nombre de places disponibles
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
    'version': '9.0.2.0.0',
    # any module necessary for this one to work correctly
    'depends': [
        'coop_memberspace',
    ],
    # always loaded
    'data': [
        'views/templates.xml',

        'views/website/planning.xml',
        'views/website/sp_tmp_disable_programmer_un_extra.xml',
        'views/website/website_homepage.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}