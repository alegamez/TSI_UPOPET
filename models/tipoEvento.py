class tipoEvento(models.Model):
    _name = 'upopet.tipoEvento'
    _descripcion = 'Modelo para los tipos de eventos'
    
    name = fields.Integer(string="Identificador", size=9, required=True)   
    nombre = fields.Char(string="Nombre", required=True, size=50, help="Tipo de evento")
    
    ids_evento = fields.one2many("upopet.evento", string="Evento del tipo")