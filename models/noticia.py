class Noticia(models.Model):
    _name = 'upopet.noticia'
    _descripcion = 'Modelo para los distintos tipos de noticias'
    
    id_noticia = fields.Integer(string="Identificador", size=9, required=True)
    titulo = fields.Char(string="Titulo", required=True, size=50, help="Titulo de la noticia")
    nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre del autor")
    fecha = fields.Datetime("Fecha", required=True)
    hora = fields.Datetime("Hora", required=True)
    descripcion = fields.Char(string="Descripcion", required=False, size=30, help="Descripcion del evento")
    
    id_administrador = fields.many2one("upopet.administrador","id_noticia", "Noticias publicadas por el administrador")
