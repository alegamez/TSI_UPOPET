class pregunta(models.Model):
    _name = 'upopet.pregunta'
    _descripcion = 'Modelo para las preguntas realizadas por los usuarios'
    
    name = fields.Integer(string="Identificador", size=9, required=True)    #id_pregunta
    contenido = fields.Char(string="Contenido", required=True, size=50, help="Contenido de la pregunta")
    fechaPublicacion = fields.Datetime("Fecha Publicación", required=True)
    
    id_usuario = fields.Many2one("upopet.usuario", string= "Usuario que realiza la pregunta")
    id_categoriaPregunta = fields.Many2one("upopet.categoriaPregunta", string= "Categoria de la pregunta")
    ids_respuesta = fields.One2many("upopet.respuesta", string="Respuestas de una pregunta")