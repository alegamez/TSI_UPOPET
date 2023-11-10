from odoo import models, fields, api

class Matricula(models.Model):
    _name = "upopet.matricula"
    _description = 'Modelo para las matriculas'


    id_matricula = fields.Integer(string="Identificador", required=True, size=9, help="Identificador de matricula")
    precio = fields.Float(string="Precio", required = True, size = (6,3), help="Precio de matricula")
    fecha = fields.Date(string="Fecha de matricula", required=True)


    pago_ids = fields.One2many("upopet.pago", 'pago_id')
    usuario_id = fields.Many2one("upopet.usuario", string="Usuario de matricula")
    evento_id = fields.Many2one("upopet.evento",  string="Evento de matricula")
