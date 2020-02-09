# -*- coding: utf-8 -*-

from openerp import models, fields, api

import openerp.addons.decimal_precision as dp

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    price_subtotal_tax = fields.Monetary(string=' Total including tax',
                                         compute='_compute_price_tax',
                                         readonly= True,
                                         store=True)

    @api.one
    @api.depends('price_unit', 'discount', 'invoice_line_tax_ids', 'quantity',
                 'product_id', 'invoice_id.partner_id',
                 'invoice_id.currency_id', 'invoice_id.company_id')
    def _compute_price_tax(self):
        currency = self.invoice_id and self.invoice_id.currency_id or None
        price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)

        taxes = False
        if self.invoice_line_tax_ids:
          taxes = self.invoice_line_tax_ids.compute_all(
            price,
            currency,
            self.quantity,
            product=self.product_id,
            partner=self.invoice_id.partner_id
          )

        self.price_subtotal_tax = taxes['total_included'] if taxes else self.quantity * price

        # if self.invoice_id:
        #     self.price_subtotal_tax = self.invoice_id.currency_id.round(
        #       self.price_subtotal_tax
        #     )
