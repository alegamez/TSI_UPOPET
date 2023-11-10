from odoo import models, fields, api

class Valoracion(models.Model):
    _name = "upopet.valoracion"
    _description = 'Modelo para la valoracion de las matriculas'


    id_valoracion = fields.Integer(string="Identificador", required=True, size=9, help="Identificador de la valoracion")
    calificacion = fields.Integer(string="Calificacion", required=True, size=5, help="Calificación del recurso educativo")
    comentario = fields.Char(string="Comentario", required=True, size=70, help="Comentario del recurso educativo")


    matricula_id = fields.Many2one("upopet.matricula", string="Publicación de la valoración sobre")
