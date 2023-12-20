from odoo import models, fields, api

class matricula(models.Model):
    _name = "upopet.matricula"
    _description = 'Modelo para las matriculas'

    name = fields.Integer(string="Identificador", required=True, size=9, help="Identificador de matricula")
    precio = fields.Float(string="Precio", required = True, digits = (6,2), help="Precio de matricula")
    fecha = fields.Date(string="Fecha de matricula", required=True)


    pago_ids = fields.One2many("upopet.pago", "matricula_id", 'El pago de su matricula es')
    usuario_id = fields.Many2one("upopet.usuario", string='Usuario Matriculado')
    evento_id = fields.Many2one("upopet.evento", 'Matriculado en Evento',required=True)
    valoracion_id = fields.One2many("upopet.valoracion", "matricula_id", 'Valoracion de la matricula')


    #Validar que la fecha de la matricula sea posterior a la actual
    @api.constrains('fecha')
    def _check_fecha_futura(self):
       for matricula in self:
            if matricula.fecha and matricula.fecha < fields.Datetime.now():
                raise ValidationError("La fecha de la matricula debe ser en el futuro.")

    #Validar que el nombre es unico para cada matricula
    @api.constrains('nombre')
    def _check_nombre_unico(self):
        for matricula in self:
            if self.env['upopet.matricula'].search([('nombre', '=', matricula.nombre), ('id', '!=', matricula.id)]):
                raise ValidationError("El nombre de la matricula debe ser único.")
