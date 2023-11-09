class Matricula(models.Model):
    _name = "upopet.matricula"
    _description = 'Modelo para las matriculas'


    id_matricula = fields.Integer(string="Identificador", required=True, size=9, help="Identificador de matricula")
    precio = fields.Float(string="Precio", required = True, size = (6,3), help="Precio de matricula")
    fecha = fields.Date(string="Fecha de matricula", required=True)


    id_pago = fields.One2One("upopet.pago", "id_matricula", string="El pago de su matricula es",
                                 required=True)
    id_usuario = fields.Many2One("upopet.usuario", "id_matricula", string="Usuario de matricula",
                                 required=True)
    id_evento = fields.Many2One("upopet.evento", "id_matricula", string="Evento de matricula",
                                 required=True)