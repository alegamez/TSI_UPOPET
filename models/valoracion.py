class Valoracion(models.Model):
    _name = "upopet.valoracion"
    _description = 'Modelo para la valoracion de las matriculas'


    id_valoracion = fields.Integer(string="Identificador", required=True, size=9, help="Identificador de la valoracion")
    calificacion = fields.Integer(string="Calificacion", required=True, size=5, help="Calificación del recurso educativo")
    comentario = fields.Char(string="Comentario", required=True, size=70, help="Comentario del recurso educativo")


    id_matricula = fields.One2One("upopet.matricula", "id_valoracion", string="Publicación de la valoración sobre",
                                 required=True)
