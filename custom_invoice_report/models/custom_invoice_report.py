from odoo import models, fields, api

class CustomInvoiceReport(models.Model):
    _name = 'custom.invoice.report'
    _description = 'Custom Invoice Report'
    _auto = False 

    partner_name = fields.Char(string='Salesman Name')
    partner_mail = fields.Char(string='Salesman Email')
    payment_state = fields.Selection([
        ('not_paid', 'Not Paid'),
        ('in_payment', 'In Payment'),
        ('paid', 'Paid'),
        ('partial', 'Partial')
    ], string='State of Payment')
    total_amount = fields.Float(string='Total Amount')
    payment_state_count = fields.Integer(string='Payment State Count' )  

   
    def init(self):
        self.env.cr.execute("""
            DROP VIEW IF EXISTS custom_invoice_report;
            CREATE OR REPLACE VIEW custom_invoice_report AS 
                SELECT
                    row_number() OVER () AS id,
                    SUM(ai.amount_total) AS total_amount,
                    ai.payment_state,
                    COUNT(ai.payment_state) AS payment_state_count,
                    rp.name AS partner_name,
                    rp.email AS partner_mail
                FROM
                    account_move ai
                JOIN
                    res_users ru ON ai.create_uid = ru.id
                JOIN
                    res_partner rp ON ru.partner_id = rp.id
                WHERE
                    ai.move_type = 'out_invoice' AND ai.state = 'posted'
                GROUP BY
                    ai.payment_state, rp.name, rp.email;
                
    """)




