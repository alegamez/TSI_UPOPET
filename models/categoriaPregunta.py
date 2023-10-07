class categoriaPregunta(models.Model):
    _name = 'upopet.categoriaPregunta'
    _descripcion = 'Modelo para las distintas categorías de las preguntas'
    
    id_categoria = fields.Integer(string="Identificador", size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre de la categoria")
    descripcion = fields.Char(string="Descripción categoria", required=True, size=50)
    