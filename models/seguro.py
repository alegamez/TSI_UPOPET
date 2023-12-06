from odoo import models, fields, api

class seguro(models.Model):
    _name = "upopet.seguro"
    _description = 'Modelo para los distintos tipos de seguros'
    
    name = fields.Integer(string="Identificador del seguro", size=9, required=True)
    precio = fields.Float(string="Precio", size=30, required=True)
    cobertura = fields.Char(string="Cobertura", required=True, size=100, help="Cobertura del seguro")
    categoria = fields.Char(string="Categoria", required=False, size=20, help="Categoria del seguro")
    duracion = fields.Integer(string="Duracion", size=9, required=True, help="Duración del seguro")
    
    especie_id = fields.Many2one("upopet.especie", "Especie asegurada")
    empresa_id= fields.Many2one("upopet.empresa", "Empresa gestora")

    _sql_constraints = [
        ('seguro_especie_unique',
         'UNIQUE(especie_id)',
         "Un seguro solo puede pertenecer a una única especie."),
    ]
    

    @api.model
    def write(self, values):
        if 'duracion' in values and values['duracion'] <= 0:
            raise Warning("La duración del seguro debe ser mayor que cero.")
        super(seguro, self).write(values)

    @api.model
    def unlink(self):
        seguros_duracion_cero = self.filtered(lambda s: s.duracion <= 0)
        if seguros_duracion_cero:
            raise Warning("No se puede eliminar un seguro con duración menor o igual a cero.")
        if self.empresa_id and self.empresa_id.exists():
            raise Warning("No se puede eliminar un seguro asociado a una empresa existente.")
        super(seguro, seguros_duracion_cero).unlink()
    
    @api.onchange('especie_id')
    def _onchange_especie_id(self):
        if self.especie_id:
            especie = self.especie_id
            self.categoria = especie.default_categoria
            self.cobertura = f"Cobertura para {especie.name}"
            self._check_duration()

    @api.model
    def validar_especie(self):
        if self.especie_id.name == 'Gato' and self.precio > 100:
            raise Warning("¡El precio para seguros de gatos no debería ser mayor a 100!")
        elif self.especie_id.name == 'Perro' and self.precio > 500:
            raise Warning("¡El precio para seguros de gatos no debería ser mayor a 500!")
        elif self.especie_id.name == 'Conejo' and (self.precio < 500 or self.precio > 5000):
            raise Warning("¡El precio para seguros de conejos no debe ser menor de 500 ni mayor que 5000!")

    @api.constrains('duracion')
    def _check_duration(self):
        for seguro in self:
            if seguro.duracion <= 0:
                raise ValidationError("La duración del seguro debe ser mayor que cero.")

    def btn_generate_report(self):
          return self.env.ref('upopet.report_seguro').report_action(self)
    
    def button_validate_species(self):
        self.ensure_one()
        try:
            self._onchange_especie_id()
        except Exception:
            pass 
        return {'type': 'ir.actions.act_window_close'}

    
    def btn_unlink_seguro(self):
        self.unlink()
