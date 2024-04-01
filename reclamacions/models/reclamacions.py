from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Reclamacion(models.Model):
    _name = 'reclamacion.reclamacion'
    _description = 'Reclamacion'

    name = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción inicial')
    resolution = fields.Text(string='Resolución final')
    customer_id = fields.Many2one('res.partner', string='Cliente')
    user_id = fields.Many2one('res.users', string='Usuario')
    creation_date = fields.Date(string='Fecha de creación', default=fields.Date.today)
    modification_date = fields.Date(string='Fecha de modificación')
    closing_date = fields.Date(string='Fecha de cierre')
    sale_order_id = fields.Many2one('sale.order', string='Comanda de venta')
    message_ids = fields.One2many('reclamacion.mensaje', 'reclamacion_id', string='Mensajes')
    invoice_count = fields.Integer(compute='_compute_invoice_count', string='Número de facturas')
    # delivery_count = fields.Integer(compute='_compute_delivery_count', string='Número de envíos')
    state = fields.Selection([
        ('nueva', 'Nueva'),
        ('en_proceso', 'En Proceso'),
        ('resuelta', 'Resuelta'),
        ('cancelada', 'Cancelada'),
    ], default='nueva')
    closing_reason_id = fields.Many2one('reclamacion.motivo', string='Motivo de cierre o cancelación')

    @api.depends('sale_order_id.invoice_ids')
    def _compute_invoice_count(self):
        for rec in self:
            rec.invoice_count = len(rec.sale_order_id.invoice_ids)
    
    def button_cancel_sale_order(self):
        for rec in self:
            sale_order = rec.sale_order_id
            if sale_order.state not in ['cancel']:
                if rec.invoice_count > 0:
                    for invoice in sale_order.invoice_ids:
                        if invoice.state == 'posted':
                            raise UserError(_('La comanda de venta no puede ser cancelada porque tiene facturas contabilizadas'))
                            break
                        else:
                            sale_order._action_cancel()
                            rec.write({'state': 'resuelta'})
                            raise UserError(_('La comanda de venta ha sido cancelada y la reclamación resuelta, pero se ha cancelado una factura pendiente de contabilizar'))
                else:
                    sale_order._action_cancel()
                    rec.write({'state': 'resuelta'})
                    UserError(_('La comanda de venta ha sido cancelada y la reclamación resuelta'))


    @api.model
    def create(self, vals):
        if 'sale_order_id' in vals:
            sale_order = self.env['sale.order'].browse(vals['sale_order_id'])
            vals['customer_id'] = sale_order.partner_id.id
            vals['user_id'] = sale_order.user_id.id
        if 'comment' in vals and vals['comment']:
            vals['state'] = 'en_proceso'
        return super(Reclamacion, self).create(vals)

    def write(self, vals):
        if 'sale_order_id' in vals:
            sale_order = self.env['sale.order'].browse(vals['sale_order_id'])
            vals['customer_id'] = sale_order.partner_id.id
            vals['user_id'] = sale_order.user_id.id
        if 'comment' in vals and vals['comment']:
            vals['state'] = 'en_proceso'
        return super(Reclamacion, self).write(vals)

    
    

    # @api.depends('sale_order_id.picking_ids')
    # def _compute_delivery_count(self):
    #     for rec in self:
    #         rec.delivery_count = len(rec.sale_order_id.picking_ids)

    # def button_return_stock(self):
    #     for rec in self:
    #         pickings = rec.sale_order_id.picking_ids
    #         for picking in pickings:
    #             if picking.state == 'done':
    #                 picking.action_cancel()
    #                 for move in picking.move_lines:
    #                     move.product_id.qty_available += move.product_uom_qty