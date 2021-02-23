# -*- coding: utf-8 -*-
# from odoo import http


# class TechCarriere(http.Controller):
#     @http.route('/tech_carriere/tech_carriere/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_carriere/tech_carriere/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_carriere.listing', {
#             'root': '/tech_carriere/tech_carriere',
#             'objects': http.request.env['tech_carriere.tech_carriere'].search([]),
#         })

#     @http.route('/tech_carriere/tech_carriere/objects/<model("tech_carriere.tech_carriere"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_carriere.object', {
#             'object': obj
#         })
