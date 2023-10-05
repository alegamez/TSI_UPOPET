# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloUpopet(http.Controller):
#     @http.route('/modulo_upopet/modulo_upopet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_upopet/modulo_upopet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_upopet.listing', {
#             'root': '/modulo_upopet/modulo_upopet',
#             'objects': http.request.env['modulo_upopet.modulo_upopet'].search([]),
#         })

#     @http.route('/modulo_upopet/modulo_upopet/objects/<model("modulo_upopet.modulo_upopet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_upopet.object', {
#             'object': obj
#         })
