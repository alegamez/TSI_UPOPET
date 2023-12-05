from odoo import models, fields, api

class tipoevento(models.Model):
    _name = 'upopet.tipoevento'
    _description = 'Modelo para los tipos de eventos'
    _rec_name = 'nombre'

    name = fields.Integer(string="tipo ID", size=10, required=True, readonly=False)
    nombre = fields.Char(string="nombre", required=True, size=50, help="Nombre del tipo de evento") 
    evento_ids = fields.One2many("upopet.evento", 'tipoevento_id', string="Eventos")

    _sql_constraints = [('tipoevento_name_unique','UNIQUE (name)','El name debe ser único')]

    @api.onchange('nombre')
    def onchange_nombre(self):
        if self.nombre:
            nuevo_nombre = f"Tipo Evento-{self.nombre}"
            self.write({'nombre': nuevo_nombre})  
    
    def btn_eliminarEventos(self):
        self.write({'evento_ids':[(5,)]})

    def btn_generate_report(self):
        return self.env.ref('upopet.report_tipoeventos').report_action(self)
