from odoo import models, fields, api

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
            self.nombreEmpresa = f"Empresa-{self.name}"

    #Verifica si hay evento anteriores organizados por esa empresa y lanza una excepción si existen
    @api.constrains('evento_ids')
    def _check_eventos_pasados(self):
        for empresa in self:
            for evento in empresa.evento_ids:
                if evento.fecha and datetime.strptime(evento.fecha, '%Y-%m-%d %H:%M:%S') < datetime.now():
                    raise ValidationError("No se pueden asociar eventos pasados a la empresa.")
