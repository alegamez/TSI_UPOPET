from odoo import models, fields, api

class Especie(models.Model):
    _name = 'upopet.especie'
    _description = 'Modelo para las especies de animales'
    _rec_name = 'nombre'

    name = fields.Integer(string="Especie ID", size=10, required=True)
    nombre = fields.Char(string="Nombre", required=True, size=50, help="Nombre de la especie")
    tamanyo = fields.Float(string="Tamaño (cm)", help="Tamaño promedio de la especie en centímetros")
    peso = fields.Float(string="Peso (kg)", help="Peso promedio de la especie en kilogramos")
    estado = fields.Selection([('permitido', 'Permitido'), ('prohibido', 'Prohibido')], string="Estado", default='activo', help="Estado de la especie")
    nombreCientifico = fields.Char(string="Nombre Científico", required=True, size=100, help="Nombre científico de la especie")

    tipoespecie_id = fields.Many2one("upopet.tipo", string="Tipo de animal")
    banner_image = fields.Binary("Banner Image")

    
