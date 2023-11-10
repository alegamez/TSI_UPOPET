from odoo import models, fields, api

class tipoevento(models.Model):
    _name = 'upopet.tipoevento'
    _description = 'Modelo para los tipos de eventos'
    _rec_name = 'nombre'

    name = fields.Integer(string="tipo ID", size=10, required=True, readonly=False)
    nombre = fields.Char(string="nombre", required=True, size=50, help="Nombre del tipo de evento") 
    evento_ids = fields.One2many("upopet.evento", 'tipoevento_id', string="Eventos")