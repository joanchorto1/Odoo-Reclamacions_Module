from odoo import models, fields, api

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
    delivery_count = fields.Integer(compute='_compute_delivery_count', string='Número de envíos')
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