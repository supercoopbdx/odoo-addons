# -*- coding: utf-8 -*-
from openerp import api, models

class ReportPricetagNoPrice(models.AbstractModel):
    _name = 'report.sp_product_pricetag.report_pricetag_no_price'
    _inherit = 'report.sp_product_pricetag.report_pricetag'
