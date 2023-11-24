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
    empresa_id = fields.Many2one("upopet.empresa",string="Evento")
    
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
            self.url = f"/evento/{self.nombre.replace(' ', '-').lower()}"
