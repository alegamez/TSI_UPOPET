class Administrador(models.Model):
    _name = "upopet.administrador"
    _description = 'Modelo para los administradores'
    
    id_administrador = fields.Integer(string="Identificador", required=True, size=9, help="Identificador del administrador")
    nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre del administrador")
    apellidos = fields.Char(string="Apellidos",required=True, size=50, help="Apellidos del administrador")
    nombreUsuario = fields.Char(string="NombreUsuario", required=True, size=30, help="Nombre de usuario del administrador")
    contrasena = fields.Char(string="Contraseña",required=True, size=50, help="Contraseña del administrador")
    correo = fields.Char(string="Correo Electronico",required=True, size=50, help="Correo electronico del administrador")
    telefono = fields.Integer(string="Telefono", required=True, size=9, help="Número de teléfono móvil del administrador")
    cargo = fields.Char(string="Cargo", required=True, size=30, help="Cargo del administrador")
    
    
    id_evento=fields.one2Many("upopet.evento","id_administrador",string="Publicacion del evento",required=True)
    id_noticia=fields.One2many("upopet.noticia","id_administrador",string="Publicacion de la noticia")