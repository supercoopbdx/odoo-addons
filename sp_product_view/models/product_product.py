from openerp.osv import osv

class product_product(osv.osv):
    _inherit = 'product.product'

    def open_to_form_view(self, cr, uid, ids, context=None):
        if not context:
            context = {}

        name = 'product'
        res_model = 'product.product'
        view_name = 'product_normal_form_view'

        document_id = self.browse(cr, uid, ids[0]).id
        view = self.pool.get('ir.model.data').get_object_reference(cr, uid, name, view_name)
        view_id = view and view[1] or False

        return {
            'name': (name),
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': [view_id],
            'res_model': res_model,
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'current',
            'res_id': document_id,
        }
