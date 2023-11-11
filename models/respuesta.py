
from odoo import models, fields, api

class respuesta(models.Model):
    _name = 'upopet.respuesta'
    _description = 'Modelo para las respuestas de las preguntas'
    
    name = fields.Integer(string="Identificador", size=9, required=True)    #id_respuesta
    contenido = fields.Char(string="Contenido", required=True, size=50, help="Contenido de la respuesta")
    fechaPublicacion = fields.Datetime("Fecha Publicación", required=True)
    
    pregunta_id = fields.Many2one("upopet.pregunta", string="Pregunta a la que pertenece la respuesta")
    usuario_id = fields.Many2one("upopet.usuario", string="Usuario que realiza la respuesta")

