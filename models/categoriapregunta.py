from odoo import models, fields, api

class categoriapregunta(models.Model):
    _name = 'upopet.categoriapregunta'
    _description = 'Modelo para las distintas categorías de las preguntas'
      
    name = fields.Char(string="Nombre Categoria", required=True, size=30)
    descripcion = fields.Char(string="Descripción categoria", required=True, size=150)

    pregunta_ids = fields.One2many("upopet.pregunta", 'categoriapregunta_id', "Preguntas")

    _sql_constraints = [('categoriapregunta_name_unique','UNIQUE (name)','El name debe ser único')]

    @api.onchange('descripcion')  
    def onchange_descripcion(self):
        print(f'La descripcion de la categoria ha cambiado a: {self.descripcion}')

    def btn_unlink(self):
        if self.pregunta_ids and self.pregunta_ids.exists():
            raise Warning("No se puede eliminar una categoria que tenga asociadas preguntas.")
        else:
            self.unlink()

    def btn_generate_report(self):
        return self.env.ref('upopet.report_categoriapreguntas').report_action(self)
