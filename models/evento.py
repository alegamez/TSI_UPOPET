from odoo import models, fields, api

class evento(models.Model):
    _name = 'upopet.evento'
    _description = 'Modelo para los distintos tipos de eventos'
    _rec_name='nombre'
    
    name = fields.Integer(string="Identificador", size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True, size=50, help="Nombre del evento")
    fecha = fields.Datetime("Fecha", required=True, help="Fecha del evento")
    descripcion = fields.Char(string="Descripcion", required=True, size=100, help="Descripción del evento")
    url = fields.Char(string="URL", required=True, size=50, help="Enlace al evento")
    
    tipoevento_id = fields.Many2one("upopet.tipoevento", string="Tipo de Evento", required=True)
    especie_ids = fields.Many2many("upopet.especie")
    empresa_id = fields.Many2one("upopet.empresa",string="Evento")
