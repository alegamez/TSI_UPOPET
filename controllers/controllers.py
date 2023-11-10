# -*- coding: utf-8 -*-
# from odoo import http


# class TsiUpopet(http.Controller):
#     @http.route('/tsi_upopet/tsi_upopet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tsi_upopet/tsi_upopet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tsi_upopet.listing', {
#             'root': '/tsi_upopet/tsi_upopet',
#             'objects': http.request.env['tsi_upopet.tsi_upopet'].search([]),
#         })

#     @http.route('/tsi_upopet/tsi_upopet/objects/<model("tsi_upopet.tsi_upopet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tsi_upopet.object', {
#             'object': obj
#         })
