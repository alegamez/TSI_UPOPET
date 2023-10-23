# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Evento(models.Model):
    _name = 'upopet.evento'
    _descripcion = 'Modelo para los distintos tipos de eventos'
    
    name = fields.Integer(string="Identificador", size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre del evento")
    fecha = fields.Datetime("Fecha", required=True, help="Fecha del evento")
    descripcion = fields.Char(string="Descripcion", required=True, size=50, help="Descripción del evento")
    url = fields.Char(string="URL", required=True, size=50, help="Enlace al evento")
    
    id_tipo_evento = fields.many2one("upopet.tipoEvento", string="Evento del tipo", required=True)
    id_especies = fields.many2many("upopet.especie","Especie")
    id_empresa = fields.many2one("upopet.empresa",string="id_evento", required=True)

