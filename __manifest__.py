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
        'security/security.xml',
        'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/pregunta_view.xml',
        'views/respuesta_view.xml',
        'views/categoriapregunta_view.xml',
        'views/tipoevento_view.xml',
        'views/empresa_view.xml',
        'views/evento_view.xml',
        'views/seguro_view.xml',
        'views/especie_view.xml',
        'views/pago_view.xml',
        'views/metodopago_view.xml',
        'views/tipo_view.xml',
        'views/usuario_view.xml',
        'views/valoracion_view.xml',
        'views/matricula_view.xml',
        'views/menu.xml',

    ],
    'css': ['static/src/css/style.css'],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
        'demo/upopet.tipo.csv',
        'demo/upopet.especie.csv',
        'demo/upopet.empresa.csv',
        'demo/upopet.tipoevento.csv',
        'demo/upopet.evento.csv',
        'demo/upopet.seguro.csv',
        'demo/upopet.matricula.csv',
        'demo/upopet.usuario.csv',
        'demo/upopet.metodopago.csv',
        'demo/upopet.pago.csv',
        'demo/upopet.categoriapregunta.csv',
        'demo/upopet.pregunta.csv',
        'demo/upopet.respuesta.csv',
        'demo/upopet.valoracion.csv',
    ],
    'application': True,
}

