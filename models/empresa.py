from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class empresa(models.Model):
    _name = "upopet.empresa"
    _descripcion = 'Modelo para los distintos tipos de empresas'
    _rec_name = 'nombreEmpresa'
    
    name = fields.Integer(string="Identificador de la empresa", size=9, required=True)
    nombreEmpresa = fields.Char(string="Nombre", required=False, size=20, help="Nombre de la empresa")
    

    evento_ids = fields.One2many("upopet.evento", 'empresa_id', string="Eventos")
    seguro_ids= fields.One2many("upopet.seguro","empresa_id", string="Seguros")

    #Asegurar que el nombre de la empresa es única
    @api.constrains('nombreEmpresa')
    def _check_nombre_empresa_unico(self):
        for empresa in self:
            if self.env['upopet.empresa'].search([('nombreEmpresa', '=', empresa.nombreEmpresa), ('id', '!=', empresa.id)]):
                raise ValidationError("El nombre de la empresa debe ser único.")
    
    #Actualizar el id de la empresa basandome en su nombre       
    @api.onchange('nombreEmpresa')
    def _onchange_nombre_empresa(self):
        if self.nombreEmpresa:
            self.name = hash(self.nombreEmpresa) % (10 ** 9)
    
    #Actualizar el nombre  de la empresa de manera automatico con un formato dado
    def _onchange_name(self):
        if self.name:
            nuevo_nombre = f"Empresa-{self.name}"
            self.write({'nombreEmpresa': nuevo_nombre})


    #Verifica si hay evento anteriores organizados por esa empresa y lanza una excepción si existen
    @api.constrains('evento_ids')
    def _check_eventos_pasados(self):
        for empresa in self:
            for evento in empresa.evento_ids:
                if evento.fecha and evento.fecha < datetime.now():
                    raise ValidationError("No se pueden asociar eventos pasados a la empresa.")
    
    def btn_create_evento(self):
        return {
            'name': 'Crear Evento',
            'type': 'ir.actions.act_window',
            'res_model': 'upopet.evento',
            'view_mode': 'form',
            'view_id': self.env.ref('tsi_upopet.upopet_evento_form_view').id,
            'target': 'new',
        }

    def btn_create_seguro(self):
        return {
            'name': 'Crear Seguro',
            'type': 'ir.actions.act_window',
            'res_model': 'upopet.seguro',
            'view_mode': 'form',
            'view_id': self.env.ref('tsi_upopet.upopet_seguro_form_view').id,
            'target': 'new',
        }
    
    def button_update_name(self):
        for empresa in self:
            empresa._onchange_name()
        return {
            'name': 'Actualizar Nombre de Empresa',
            'type': 'ir.actions.act_window',
            'res_model': 'upopet.empresa',
            'view_mode': 'form',
            'view_id': self.env.ref('tsi_upopet.upopet_empresa_form_view').id,  
            'res_id': self.id,  
            'target': 'new',
    }

