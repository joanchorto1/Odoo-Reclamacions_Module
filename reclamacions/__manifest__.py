{
    'name': "Reclamaciones",
    'version': '1.0',
    'depends': ['base', 'sale'],
    'author': "Grup2 Eric Ortega Joan Chortó",
    'category': 'Uncategorized',
    'description': """
        Módulo de gestión de reclamaciones
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/reclamacion_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

