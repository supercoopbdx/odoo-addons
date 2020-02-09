# -*- coding: utf-8 -*-

from openerp import models, fields, api

import logging
import openerp.addons.decimal_precision as dp

_logger = logging.getLogger(__name__)

class StockPackOperation(models.Model):
    _inherit = 'stock.pack.operation'

    @api.depends('product_id.seller_ids')
    def _get_product_supplierinfo_base_price(self):
        # self is multiple (records not a single record)
        for spo in self:
          # seller2 = spo.product_id.seller_ids[0]
          seller = spo.product_id._select_seller(product_id=spo.product_id)
          if seller:
            spo.sp_price = seller.price

    # sp_price = fields.Float(string="Product Base Price", store=False, readonly=False, related="product_id.seller_ids.ids[0].price")
    # sp_price = fields.Float(compute='_get_product_supplierinfo_base_price', string='Product Base Price', store=False, readonly=True)
    sp_price = fields.Float(compute='_get_product_supplierinfo_base_price', string='Product Seller Price', store=False, copy=False)
