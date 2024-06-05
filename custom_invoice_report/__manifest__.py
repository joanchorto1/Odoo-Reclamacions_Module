{
    'name': 'Custom Invoice Report',
    'version': '1.0',
    'summary': 'Adds a custom invoice report to Odoo',
    'description': 'This module adds a custom invoice report to Odoo for enhanced invoicing functionality.',
    'category': 'Invoicing',
    'author': 'Joan Chorto',
    'depends': ['base', 'account'],
    'data': [
        'reports/custom_report_template.xml',
        'security/ir.model.access.csv',
        'views/custom_report_menu.xml',
        'views/custom_report_view.xml',
        'views/invoice_extension_view.xml',
        'reports/invoice_report_extension.xml'

      
        



    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}