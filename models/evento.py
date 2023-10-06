# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Evento(models.Model):
    _name = 'upopet.evento'
    _descripcion = 'Modelo para los distintos tipos de eventos'
    
    id_evento = fields.Integer(string="Identificador", size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre del evento")
    lugar = fields.Char(string="Lugar", required=True, size=50, help="Lugar del evento")
    fecha = fields.Datetime("Fecha", required=True)
    hora = fields.Datetime("Hora", required=True)
    descripcion = fields.Char(string="Descripcion", required=False, size=30, help="Descripcion del evento")
    
    id_administrador = fields.many2one("upopet.administrador","id_evento","Eventos creados por el administrador")
