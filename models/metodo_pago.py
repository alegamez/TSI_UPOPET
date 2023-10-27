from odoo import models, fields

class MetodoPago(models.Model):
    _name = 'upopet.metodo_pago'
    _description = 'Modelo para los métodos de pago'

    id_metodoPago = fields.Char(string="Método de Pago ID", required=True, help="Identificador del método de pago")
    nombre = fields.Char(string="Nombre", required=True, help="Nombre del método de pago")

   

