from odoo import models, fields

class Pago(models.Model):
    _name = 'upopet.pago'
    _description = 'Modelo para los pagos'

    id_pago = fields.Char(string="Pago ID", required=True, help="Identificador del pago")
    id_metodoPago = fields.Many2one("upopet.metodo_pago", string="Método de Pago", required=True, help="Método de pago utilizado")
    id_matricula = fields.Many2one("upopet.matricula", string="Matrícula", required=True, help="Matrícula relacionada al pago")
    

  

