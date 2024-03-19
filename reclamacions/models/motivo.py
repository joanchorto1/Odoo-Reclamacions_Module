from odoo import models, fields

class Motivo(models.Model):
    _name = 'reclamacion.motivo'
    _description = 'Motivo de cierre o cancelación'

    name = fields.Char(string='Nombre', required=True)
