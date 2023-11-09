from odoo import models, fields, api

class pago(models.Model):
    _name = 'upopet.pago'
    _description = 'Modelo para los pagos'

    name = fields.Integer(string="Pago ID", required=True, help="Identificador del pago")
    metodopago_id = fields.Many2one("upopet.metodopago", string="Método de Pago", required=True, help="Método de pago utilizado")
    #id_matricula = fields.Many2one("upopet.matricula", string="Matrícula", required=True, help="Matrícula relacionada al pago")
   
