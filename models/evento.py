# -*- coding: utf-8 -*-

from odoo import models, fields, api

class evento(models.Model):
    _name = 'upopet.evento'
    _descripcion = 'Modelo para los distintos tipos de eventos'
    
    name = fields.Integer(string="Identificador", size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre del evento")
    fecha = fields.Datetime("Fecha", required=True, help="Fecha del evento")
    descripcion = fields.Char(string="Descripcion", required=True, size=50, help="Descripción del evento")
    url = fields.Char(string="URL", required=True, size=50, help="Enlace al evento")
    
    tipoevento_id = fields.Many2one("upopet.tipoevento", string="Evento del tipo", required=True)
    especie_ids = fields.many2many("upopet.especie","Especie")
    empresa_id = fields.Many2one("upopet.empresa",string="Evento")

