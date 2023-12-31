from odoo import models, fields, api

class cuestionario(models.Model):
    _name = "upopet.cuestionario"
    _description = 'Modelo para el cuestionario de los usuarios'

    name = fields.Char(string="Identificador", required=True, help="Identificador del cuestionario")
    jardin = fields.Selection([('si', 'Si'), ('no', 'No')], string="¿Tiene jardín?", help="Indica si el usuario tiene jardín o no")
    espacioDisponible = fields.Float(string="Espacio disponible", help="Espacio disponible en la vivienda del usuario")
    experienciaPrevia = fields.Selection([('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], string="Experiencia previa", help="Nivel de experiencia previa del usuario con mascotas")
    exotico = fields.Selection([('si', 'Si'), ('no', 'No')], string="¿Le gustan los animales exóticos?", help="Indica si al usuario le gustan los animales exóticos o no")
    preferencia = fields.Selection([('perros', 'Perros'), ('gatos', 'Gatos'), ('peces', 'Peces'), ('pequeños mamíferos', 'Pequeños mamíferos'), ('insectos', 'Insectos'), ('reptiles exoticos', 'Reptiles exóticos'), ('indiferente', 'Indiferente')], string="Preferencia de mascota", help="Tipo de mascota preferida por el usuario")
    usuario_id = fields.Many2one("upopet.usuario", string='Usuario')
    
    @api.constrains('espacioDisponible')
    def _check_espacio_disponible(self):
        for cuestionario in self:
            if cuestionario.espacioDisponible < 0:
                raise ValueError("El espacio disponible no puede ser negativo.")
            
    @api.onchange('jardin')
    def _onchange_jardin(self):
        if self.jardin == 'si':
            self.espacioDisponible = 100  
        elif self.jardin == 'no':
            self.espacioDisponible = 50
            
    def btn_generate_report(self):
        return self.env.ref('upopet.report_cuestionario').report_action(self) 
