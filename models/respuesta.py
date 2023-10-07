class respuesta(models.Model):
    _name = 'upopet.respuesta'
    _descripcion = 'Modelo para las respuestas de las preguntas'
    
    id_respuesta = fields.Integer(string="Identificador", size=9, required=True)
    contenido = fields.Char(string="Titulo", required=True, size=50, help="Contenido de la respuesta")
    id_usuario = fields.Char(string="ID usuario", required=True, size=30, help="ID del usuario")
    fechaPublicacion = fields.Datetime("Fecha Publicación", required=True)
    
    id_pregunta = fields.many2one("upopet.pregunta","id_pregunta", "Pregunta a la que pertenece la respuesta")
    id_usuario = fields.many2one("upopet.usuario","id_usuario", "Usuario que realiza la respuesta")