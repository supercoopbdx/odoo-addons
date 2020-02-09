# -*- coding: utf-8 -*-
from openerp import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.multi
    def _get_supplier_codes(self):
        product_supplier_info_obj = self.env['product.supplierinfo']
        for line in self:
            purchase_order = line.order_id
            supplier_info = product_supplier_info_obj.search([('product_tmpl_id','=',line.product_id.product_tmpl_id.id),('name','=',purchase_order.partner_id.id)],limit=1)
            line.sp_product_code = supplier_info.product_code

    @api.multi
    def _get_supplier_names(self):
        product_supplier_info_obj = self.env['product.supplierinfo']
        for line in self:
            purchase_order = line.order_id
            supplier_info = product_supplier_info_obj.search([('product_tmpl_id','=',line.product_id.product_tmpl_id.id),('name','=',purchase_order.partner_id.id)],limit=1)
            line.sp_product_name = supplier_info.product_name

    @api.depends('order_id.partner_id')
    def _get_supplier_name(self):
        product_supplier_info_obj = self.env['product.supplierinfo']
        for line in self:
            supplier_info = product_supplier_info_obj.search([('product_tmpl_id','=',line.product_id.product_tmpl_id.id),('name','=',line.order_id.partner_id.id)],limit=1)
            line.sp_product_name = supplier_info.product_name

    @api.depends('order_id.partner_id')
    def _get_supplier_code(self):
        product_supplier_info_obj = self.env['product.supplierinfo']
        for line in self:
            supplier_info = product_supplier_info_obj.search([('product_tmpl_id','=',line.product_id.product_tmpl_id.id),('name','=',line.order_id.partner_id.id)],limit=1)
            line.sp_product_code = supplier_info.product_code

    sp_product_code = fields.Char(compute="_get_supplier_code", store=False, string="Supplierinfo Product Code")
    sp_product_name = fields.Char(compute="_get_supplier_name", store=False, string="Supplierinfo Product Name")
