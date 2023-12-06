# -*- coding: utf-8 -*-
from odoo import models, fields, api

class tipo(models.Model):
    _name = 'upopet.tipo'
    _description = 'Modelo para los tipos de animales'
    _rec_name = 'nombre'
    
    name = fields.Integer(string="tipo ID", size=10, required=True, readonly=False)
    nombre = fields.Char(string="nombre", required=True, size=50, help="Nombre del tipo de animal")
    
    #para la vista
    imagentipo = fields.Binary('Photo')

    especie_ids = fields.One2many("upopet.especie", 'tipoespecie_id', "especie")
    