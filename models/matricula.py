from odoo import models, fields, api

class matricula(models.Model):
    _name = "upopet.matricula"
    _description = 'Modelo para las matriculas'

    name = fields.Integer(string="Identificador", required=True, size=9, help="Identificador de matricula")
    precio = fields.Float(string="Precio", required = True, digits = (6,2), help="Precio de matricula")
    fecha = fields.Date(string="Fecha de matricula", required=True)


    pago_ids = fields.One2many("upopet.pago", "matricula_id", 'El pago de su matricula es')
    usuario_id = fields.One2many("upopet.usuario", 'matricula_ids', string='Usuario')
    evento_id = fields.Many2one("upopet.evento", 'Evento de matricula',required=True)