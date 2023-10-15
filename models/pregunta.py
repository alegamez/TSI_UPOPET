class pregunta(models.Model):
    _name = 'upopet.pregunta'
    _descripcion = 'Modelo para las preguntas realizadas por los usuarios'
    
    name = fields.Integer(string="Identificador", size=9, required=True)    #id_pregunta
    titulo = fields.Char(string="Titulo", required=True, size=30, help="Titulo de la pregunta")
    contenido = fields.Char(string="Contenido", required=True, size=50, help="Contenido de la pregunta")
    fechaPublicacion = fields.Datetime("Fecha Publicación", required=True)
    
    id_usuario = fields.many2one("upopet.usuario","id_usuario", "Usuario que realiza la pregunta")