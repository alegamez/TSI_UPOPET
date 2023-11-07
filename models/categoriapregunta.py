from odoo import models, fields, api

class categoriapregunta(models.Model):
    _name = 'upopet.categoriapregunta'
    _description = 'Modelo para las distintas categorías de las preguntas'
    
    #name = fields.Integer(string="Nombre", size=9, required=True)    
    #nombre = fields.Char(string="Nombre Categoria", required=True, size=30)
    name = fields.Selection([('alimentacion','Alimentacion'),
                                     ('habitat','Habitat'),
                                     ('cuidados','Cuidados'),],
                                     'Nombre de la categoria', required=True)
    descripcion = fields.Char(string="Descripción categoria", required=True, size=50)

    pregunta_ids = fields.One2many("upopet.pregunta", 'categoriapregunta_id', "pregunta")