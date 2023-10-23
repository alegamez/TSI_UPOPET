class categoriaPregunta(models.Model):
    _name = 'upopet.categoriaPregunta'
    _descripcion = 'Modelo para las distintas categorías de las preguntas'
    
    name = fields.Integer(string="Identificador", size=9, required=True)    #id_categoria
    nombre = fields.Char(string="NombreCategoria", required=True, size=30)
    descripcion = fields.Char(string="Descripción categoria", required=True, size=50)

    ids_pregunta = fields.One2Many("upopet.pregunta", 'id_pregunta', "Categoria a la que pertenece la pregunta")
