from odoo import models, fields, api

class Usuario(models.Model):
    _name = "upopet.usuario"
    _description = 'Modelo para los clientes'

    id_usuario = fields.Integer(string="Identificador", required=True, size=9, help="Identificador de usuario")
    nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre del Usuario")
    apellidos = fields.Char(string="Apellidos",required=True, size=50, help="Apellidos del Usuario")
    nombreUsuario = fields.Char(string="NombreUsuario", required=True, size=30, help="Nombre de usuario del usuario")
    contraseña = fields.Char(string="Contraseña",required=True, size=50, help="Contraseña del usuario")
    correo = fields.Char(string="Correo Electronico",required=True, size=50, help="Correo electronico del usuario")


    matricula_ids = fields.One2many("upopet.matricula", "id_usuario", string="Su matricula es",
                                 required=True)
    
