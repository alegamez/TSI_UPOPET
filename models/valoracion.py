from odoo import models, fields, api

class valoracion(models.Model):
    _name = "upopet.valoracion"
    _description = 'Modelo para la valoracion de las matriculas'

    name = fields.Integer(string="Identificador", required=True, size=9, help="Identificador de la valoracion")
    calificacion = fields.Integer(string="Calificacion", required=True, size=5, help="Calificación del recurso educativo")
    comentario = fields.Char(string="Comentario", required=True, size=70, help="Comentario del recurso educativo")
    matricula_id = fields.Many2one("upopet.matricula", string='Matricula Valorada', ondelete='cascade')

    _sql_constraints = [
        ('matricula_id_unique',
         'UNIQUE(matricula_id)',
         "La matricula ya tiene una valoracion."),
    ]

    @api.constrains('calificacion')
    def _check_calificacion(self):
        for record in self:
            if record.calificacion < 0 or record.calificacion > 10:
                raise ValidationError("La calificacion tiene que ser entre 0 y 10")
