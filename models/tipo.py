# -*- coding: utf-8 -*-
from odoo import models, fields, api

class tipo(models.Model):
    _name = 'upopet.tipo'
    _description = 'Modelo para los tipos de animales'
    _rec_name = 'nombre'
    
    name = fields.Integer(string="tipo ID", size=10, required=True, readonly=False)
    nombre = fields.Char(string="nombre", required=True, size=50, help="Nombre del tipo de animal")
    
    #para la vista
    #imagentipo = fields.Binary('Photo')

    especie_ids = fields.One2many("upopet.especie", 'tipoespecie_id', "especie")
    
    _sql_constraints = [('tipo_nombre_unique','UNIQUE (nombre)','El nombre debe ser único')]

    
    def btn_desasociarEspecies(self):
        self.ensure_one()
        self.especie_ids.write({'tipoespecie_id': False})