class respuesta(models.Model):
    _name = 'upopet.respuesta'
    _descripcion = 'Modelo para las respuestas de las preguntas'
    
    name = fields.Integer(string="Identificador", size=9, required=True)    #id_respuesta
    contenido = fields.Char(string="Titulo", required=True, size=50, help="Contenido de la respuesta")
    fechaPublicacion = fields.Datetime("Fecha Publicación", required=True)
    
    id_pregunta = fields.Many2one("upopet.pregunta", string="Pregunta a la que pertenece la respuesta")
    id_usuario = fields.Many2one("upopet.usuario", string="Usuario que realiza la respuesta")