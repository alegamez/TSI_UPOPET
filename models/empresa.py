from odoo import models, fields, api

class empresa(models.Model):
    _name = "upopet.empresa"
    _descripcion = 'Modelo para los distintos tipos de empresas'
    
    name = fields.Integer(string="Identificador de la empresa", size=9, required=True)
    nombreEmpresa = fields.Char(string="Nombre", required=False, size=20, help="Nombre de la empresa")
    

    evento_ids = fields.One2many("upopet.evento", 'empresa_id', string="Evento")
    seguro_ids= fields.One2many("upopet.seguro","empresa_id", string="Seguro")