from odoo import models, fields, api

class Mensaje(models.Model):
    _name = 'reclamacion.mensaje'
    _description = 'Mensaje'

    author_id = fields.Many2one('res.users', string='Autor')
    date = fields.Date(string='Fecha', default=fields.Date.today)
    text = fields.Text(string='Texto del mensaje')
    reclamacion_id = fields.Many2one('reclamacion.reclamacion', string='Reclamación')
