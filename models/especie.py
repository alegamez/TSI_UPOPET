from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Especie(models.Model):
    _name = 'upopet.especie'
    _description = 'Modelo para las especies de animales'
    _rec_name = 'nombre'

    name = fields.Integer(string="Especie ID", size=10, required=True)
    nombre = fields.Char(string="Nombre", required=True, size=50, help="Nombre de la especie")
    tamanyo = fields.Float(string="Tamaño (cm)", help="Tamaño promedio de la especie en centímetros")
    peso = fields.Float(string="Peso (kg)", help="Peso promedio de la especie en kilogramos")
    estado = fields.Selection([('permitido', 'Permitido'), ('prohibido', 'Prohibido')], string="Estado", default='activo', help="Estado de la especie")
    nombreCientifico = fields.Char(string="Nombre Científico", required=True, size=100, help="Nombre científico de la especie")

    tipoespecie_id = fields.Many2one("upopet.tipo", string="Tipo de animal")
    
    _sql_constraints = [('especie_nombreCientifico_unique','UNIQUE (nombreCientifico)','El nombre cientifico debe ser único')]

    count = fields.Integer(compute='_compute_count', store=True)

    #para la vista avanzada, contamos las especies
    @api.depends('name')
    def _compute_count(self):
        for record in self:
            record.count = 1

    def btn_generate_report(self):
        return self.env.ref('upopet.report_especies').report_action(self)

    @api.constrains('peso')
    def _check_peso(self):
        for record in self:
            if record.peso <= 0 or record.peso < 0.1:
                raise ValidationError("El peso no puede ser inferior a 0.1 ni mayor a 0")

    @api.constrains('tamanyo')
    def _check_tamanyo(self):
        for record in self:
            if record.tamanyo <= 0 or record.tamanyo < 0.1:
                raise ValidationError("El tamaño no puede ser inferior a 0.1 ni mayor a 0")

    @api.onchange('tamanyo')
    def _onchange_tamanyo(self):
        if self.tamanyo > 500:
            self.estado = 'prohibido'

    @api.onchange('estado')
    def _onchange_estado(self):
        if self.estado == 'permitido' and self.tamanyo > 500:
            self.estado = 'prohibido'
            return {
                'warning': {
                    'title': "Valor incorrecto",
                    'message': "No se puede cambiar el estado a permitido si el tamaño es mayor a 500 cm",
                },
            }

    