# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Especie(models.Model):
    _name = 'upopet.especie'
    _description = 'Modelo para las especies de animales'

    id_especie = fields.Char(string="Especie ID", required=True, help="Identificador de la especie")
    nombre = fields.Char(string="Nombre", required=True, size=50, help="Nombre de la especie")
    tamaño = fields.Float(string="Tamaño (cm)", help="Tamaño promedio de la especie en centímetros")
    peso = fields.Float(string="Peso (kg)", help="Peso promedio de la especie en kilogramos")
    estado = fields.Selection([('permitido', 'Permitido'), ('prohibido', 'Prohibido')], string="Estado", default='activo', help="Estado de la especie")
    clase = fields.Char(string="Clase", required=True, size=50, help="Clase de la especie")
    nombreCientifico = fields.Char(string="Nombre Científico", required=True, size=100, help="Nombre científico de la especie")

    _sql_constraints = [('especie_id_unique', 'UNIQUE (id_especie)', 'Compruebe el ID de la especie, debe ser único.')]