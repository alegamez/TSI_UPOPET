# -*- coding: utf-8 -*-
{
    'name': "tsi_upopet",

    'summary': """Gestion del modulo UPOPET""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

        'views/pregunta_view.xml',
        'views/respuesta_view.xml',
        'views/categoriapregunta_view.xml',
        'views/tipoevento_view.xml',
        'views/empresa_view.xml',
        'views/evento_view.xml',
        'views/seguro_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
        'demo/upopet.evento.csv',
    ],
    'application': True,
}
