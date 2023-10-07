class Seguro(models.Model):
    _name = "upopet.seguro"
    _descripcion = 'Modelo para los distintos tipos de seguros'
    
    id_seguro = fields.Integer(string="Identificador", size=9, required=True)
    nombreEmpresa = fields.Char(string="NombreEmpresa", required=True, size=50, help="Nombre de la empresa")
    precio = fields.Float(string="Precio", size=30, required=True)
    cobertura = fields.Char(string="Cobertura", required=True, size=100, help="Cobertura del seguro")
    categoria = fields.Char(string="Cateogria", required=False, size=20, help="Categoria del seguro")
    duracion = fields.Integer(string="Duración (en meses)", required=True, help="Duración de la cobertura en meses")

    id_especia = fields.many2many("upopet.especie","id_seguro", "Seguro tiene la especie")