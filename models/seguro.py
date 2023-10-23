class Seguro(models.Model):
    _name = "upopet.seguro"
    _descripcion = 'Modelo para los distintos tipos de seguros'
    
    name = fields.Integer(string="Identificador del seguro", size=9, required=True)
    precio = fields.Float(string="Precio", size=30, required=True)
    cobertura = fields.Char(string="Cobertura", required=True, size=100, help="Cobertura del seguro")
    categoria = fields.Char(string="Cateogria", required=False, size=20, help="Categoria del seguro")
    duracion = fields.Integer(string="Duracion", size=9, required=True, help="Duración del seguro")
    
    id_especie = fields.many2one("upopet.especie","id_espeice", "Seguro tiene la especie")
    id_empresa= fields.many2one("upopet.empresa","id_empresa", "Empresa del seguro")
