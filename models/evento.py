from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class evento(models.Model):
    _name = 'upopet.evento'
    _description = 'Modelo para los distintos tipos de eventos'
    _rec_name='nombre'
    
    name = fields.Integer(string="Identificador", size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True, size=50, help="Nombre del evento")
    fecha = fields.Datetime("Fecha", required=True, help="Fecha del evento")
    descripcion = fields.Char(string="Descripcion", required=True, size=100, help="Descripción del evento")
    url = fields.Char(string="URL", required=True, size=50, help="Enlace al evento")
    
    tipoevento_id = fields.Many2one("upopet.tipoevento", string="Tipo de Evento", required=True)
    especie_ids = fields.Many2many("upopet.especie")
    empresa_id = fields.Many2one("upopet.empresa",string="Empresa organizadora")
    
    _sql_constraints = [
        ('evento_tipoempresa_unique',
         'UNIQUE(name, empresa_id)',
         "El evento ya está gestionado por una empresa."),
        ('evento_tipoevento_unique',
         'UNIQUE(name, tipoevento_id)',
         "El evento ya tiene un tipo."),
    ]
    
    #Validar que la fecha del evento sea posterior a la actual
    @api.constrains('fecha')
    def _check_fecha_futura(self):
       for evento in self:
            if evento.fecha and evento.fecha < fields.Datetime.now():
                raise ValidationError("La fecha del evento debe ser en el futuro.")

    #Validar que el nombre es unico para cada evento
    @api.constrains('nombre')
    def _check_nombre_unico(self):
        for evento in self:
            if self.env['upopet.evento'].search([('nombre', '=', evento.nombre), ('id', '!=', evento.id)]):
                raise ValidationError("El nombre del evento debe ser único.")
      
    #Actualizacion de la descripcion basandome en el tipo de evento      
    @api.onchange('tipoevento_id')
    def _onchange_tipoevento_id(self):
        if self.tipoevento_id:
            self.descripcion = f"Evento de tipo {self.tipoevento_id.name}"

    #Actualizacion de la URL del evento basada en el nombre
    @api.onchange('nombre')
    def _onchange_nombre(self):
        if self.nombre:
            nueva_url = f"Evento-{self.url}"
            self.write({'url': nueva_url})
    
    def button_update_description(self):
        self.ensure_one()
        self._onchange_tipoevento_id()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'upopet.evento',
            'view_mode': 'form',
            'view_id': self.env.ref('tsi_upopet.upopet_evento_form_view').id,
            'res_id': self.id,
            'target': 'current',
        }

    def button_update_url(self):
        self.ensure_one()
        self._onchange_nombre()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'upopet.evento',
            'view_mode': 'form',
            'view_id': self.env.ref('tsi_upopet.upopet_evento_form_view').id,
            'res_id': self.id,
            'target': 'current',
        } 

