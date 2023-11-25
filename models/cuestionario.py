from odoo import models, fields, api

class cuestionario(models.Model):
    _name = "upopet.cuestionario"
    _description = 'Modelo para el cuestionario de los usuarios'

    name = fields.Char(string="Identificador", required=True, help="Identificador del cuestionario")
    jardin = fields.Selection([('si', 'Si'), ('no', 'No')], string="¿Tiene jardín?", help="Indica si el usuario tiene jardín o no")
    espacioDisponible = fields.Float(string="Espacio disponible", help="Espacio disponible en la vivienda del usuario")
    experienciaPrevia = fields.Selection([('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], string="Experiencia previa", help="Nivel de experiencia previa del usuario con mascotas")
    exotico = fields.Selection([('si', 'Si'), ('no', 'No')], string="¿Le gustan los animales exóticos?", help="Indica si al usuario le gustan los animales exóticos o no")
    preferencia = fields.Selection([('perros', 'Perros'), ('gatos', 'Gatos'), ('peces', 'Peces'), ('pequeños mamíferos', 'Pequeños mamíferos'), ('insectos', 'Insectos'), ('reptiles exoticos', 'Reptiles exóticos'), ('indiferente', 'Indiferente')], string="Preferencia de mascota", help="Tipo de mascota preferida por el usuario")
    usuario_id = fields.Many2one("upopet.usuario", string='Usuario')

    _sql_constraints = [
        ('cuestionario_usuario_unique',
         'UNIQUE(usuario_id)',
         "Un mismo cuestionario solo puede ser respondido por un único usuario."),
    ]
