from odoo import models, fields, api

class metodopago(models.Model):
    _name = 'upopet.metodopago'
    _description = 'Modelo para los métodos de pago'
    _rec_name = 'nombre'
    
    name = fields.Integer(string="Método de Pago ID", size=10, required=True, help="Identificador del método de pago")
    nombre = fields.Char(string="Nombre", required=True, size=50, help="Nombre del método de pago")
    pago_id = fields.One2many("upopet.pago", 'metodopago_id', 'pago')