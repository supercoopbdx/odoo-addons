# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2012 Agile Business Group sagl (<http://www.agilebg.com>)
#    Copyright (C) 2012 Domsense srl (<http://www.domsense.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Supercoop - Pricetags',
    'version': '9.0.0.0.7',
    'category': 'Custom',
    'author': "FJG - Supercoop",
    'website': 'https://www.supercoop.fr',
    'license': 'AGPL-3',
    'summary': 'Custom pricetag reports for products',
    'depends': [
        'product',
        'product_to_print',
        'report',
        'coop_default_pricetag'
    ],
    'data': [
        'data/report_paperformat.xml',
        'data/pricetag_model.xml',
        'report/report.xml',
        'report/report_pricetag.xml',
        'report/report_pricetag_no_price.xml',
        'report/report_pricetag_vegetables.xml'
    ],
    'css': [
        'static/src/css/sp_pricetag.css',
        'static/src/css/sp_pricetag_vegetables.css',
    ],
}
