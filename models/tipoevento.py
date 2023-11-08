from odoo import models, fields, api

class tipoevento(models.Model):
    _name = 'upopet.tipoevento'
    _description = 'Modelo para los tipos de eventos'
    
    name = fields.Integer(string="Identificador", size=9, required=True)   
    nombre = fields.Char(string="Nombre", required=True, size=50, help="Tipo de evento")
    
    evento_ids = fields.One2many("upopet.evento", 'tipoevento_id', string="Eventos")
