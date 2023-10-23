class Valoracion(models.Model):
    _name = "upopet.valoracion"
    _description = 'Modelo para la valoracion de los recursos educativos'

    id_valoracion = fields.Integer(string="Identificador", required=True, size=9, help="Identificador de la valoracion")
    calificacion = fields.Integer(string="Calificacion", required=True, size=5, help="Calificación del recurso educativo")
    comentario = fields.Char(string="Comentario", required=True, size=70, help="Comentario del recurso educativo")


    id_usuario=fields.Many2One("upopet.usuario","id_valoracion",string="Publicación de la valoración por",required=True)
    id_recursoEducativo=fields.Many2One("upopet.recursoEducativo","id_administrador",string="Publicacion de la noticia")