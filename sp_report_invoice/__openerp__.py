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
    'name': 'Supercoop - Report Invoice',
    'version': '9.0.0.0.0',
    'category': 'Custom',
    'author': "FJG - Supercoop",
    'website': 'https://www.supercoop.fr',
    'license': 'AGPL-3',
    'summary': 'Custom report invoice',
    'depends': [
        'account',
        'product',
        'report',
        'point_of_sale'
    ],
    'data': [
        'report/sp_account_report.xml',
        'report/sp_invoice_layout_footer.xml',
        'report/sp_report_invoice.xml',
    ],
}
