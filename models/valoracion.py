from odoo import models, fields, api

class valoracion(models.Model):
    _name = "upopet.valoracion"
    _description = 'Modelo para la valoracion de las matriculas'


    name = fields.Integer(string="Identificador", required=True, size=9, help="Identificador de la valoracion")
    calificacion = fields.Integer(string="Calificacion", required=True, size=5, help="Calificación del recurso educativo")
    comentario = fields.Char(string="Comentario", required=True, size=70, help="Comentario del recurso educativo")


    #matricula_id = fields.One2one("upopet.matricula", "id_valoracion", string="Publicación de la valoración sobre",required=True)
