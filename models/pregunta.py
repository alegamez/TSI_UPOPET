
from odoo import models, fields, api

class pregunta(models.Model):
    _name = 'upopet.pregunta'
    _description = 'Modelo para las preguntas realizadas por los usuarios'
    _rec_name='contenido'
    
    name = fields.Integer(string="Identificador de la pregunta", size=9, required=True)
    contenido = fields.Char(string="Contenido", required=True, size=150, help="Contenido de la pregunta")
    fechaPublicacion = fields.Datetime("Fecha Publicación", required=True)

    usuario_id = fields.Many2one("upopet.usuario", string= "Usuario que realiza la pregunta")
    categoriapregunta_id = fields.Many2one("upopet.categoriapregunta", string= "Categoria pregunta")
    respuesta_ids = fields.One2many("upopet.respuesta", 'pregunta_id', string="Respuestas")

    _sql_constraints = [('pregunta_name_unique','UNIQUE (name)','El name debe ser único')]

    count = fields.Integer(compute='_compute_count', store=True)

    @api.depends('name')
    def _compute_count(self):
        for record in self:
            record.count = 1

    def btn_eliminarRespuesta(self):
        self.write({'respuesta_ids':[(5,)]})

    @api.onchange('contenido')
    def onchange_contenido(self):
        #Actualizar la fecha de publicación cada vez que el contenido cambie
        self.fechaPublicacion = fields.Datetime.now()