from odoo import models, fields, api

class categoriapregunta(models.Model):
    _name = 'upopet.categoriapregunta'
    _description = 'Modelo para las distintas categorías de las preguntas'
    _rec_name='nombre'
    
    name = fields.Integer(string="Identificador de la Categoria Pregunta", size=9, required=True)    
    nombre = fields.Char(string="Nombre Categoria", required=True, size=30)
    descripcion = fields.Char(string="Descripción categoria", required=True, size=50)

    pregunta_ids = fields.One2many("upopet.pregunta", 'categoriapregunta_id', string="Pregunta")
