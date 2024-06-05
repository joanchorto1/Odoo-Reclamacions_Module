from odoo import fields, models, api

class Invoice(models.Model):
    _inherit = 'account.move'

    follow_up = fields.Boolean(string='Follow Up', default=False)

    # Campo calculado para nombre y correo del socio
    partner_name_mail = fields.Char(string='Customer Name and Email', compute='_compute_partner_name_mail')
    
    @api.depends('create_uid')
    def _compute_partner_name_mail(self):
          for record in self:
            if record.create_uid and record.create_uid.partner_id:
                partner = record.create_uid.partner_id
                record.partner_name_mail = f"{partner.name} - {partner.email}"
            else:
                record.partner_name_mail = ""