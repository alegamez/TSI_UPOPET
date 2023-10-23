# -*- coding: utf-8 -*-

from odoo import models, fields, api

Class Empresa(models.Model):
    _name = "upopet.evento"
    _descripcion = 'Modelo para los distintos tipos de empresas'
    
    name = fields.Integer(string="Identificador de la empresa", size=9, required=True)
    nombreEmpresa = fields.Char(string="Nombre", required=False, size=20, help="Nombre de la empresa")
    

    id_evento = fields.many2one("upopet.evento", "Evento")
    ids_seguro= fields.one2many("upopet.seguro","id_empresa", "Seguro")
