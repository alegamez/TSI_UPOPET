
from odoo import models, fields, api

class respuesta(models.Model):
    _name = 'upopet.respuesta'
    _description = 'Modelo para las respuestas de las preguntas'
    
    name = fields.Integer(string="Identificador", size=9, required=True)    #id_respuesta
    contenido = fields.Char(string="Contenido", required=True, size=50, help="Contenido de la respuesta")
    fechaPublicacion = fields.Datetime("Fecha Publicación", required=True)
    
    pregunta_id = fields.Many2one("upopet.pregunta", string="Pregunta a la que pertenece la respuesta")
    usuario_id = fields.Many2one("upopet.usuario", string="Usuario que realiza la respuesta")

    _sql_constraints = [('respuesta_name_unique','UNIQUE (name)','El name debe ser único')]

    def btn_eliminar_respuesta(self):
        self.unlink()

    def btn_duplicar_respuesta(self):
        for registro in self:
            nueva_respuesta = registro.copy(default={'name': -registro.name})

    @api.onchange('contenido')  
    def onchange_contenido(self):
        print(f'El contenido de la respuesta ha cambiado a: {self.contenido}')
