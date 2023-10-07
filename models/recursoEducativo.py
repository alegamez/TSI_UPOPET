# -*- coding: utf-8 -*-

from odoo import models, fields

class RecursoEducativo(models.Model):
    _name = 'upopet.recurso_educativo'
    _description = 'Modelo para Recursos Educativos'

    id_recursoEducativo = fields.Char(string="Recurso Educativo ID", required=True, help="Identificador del Recurso Educativo")
    titulo = fields.Char(string="Título", required=True, help="Título del Recurso Educativo")
    descripcion = fields.Text(string="Descripción", help="Descripción del Recurso Educativo")
    tipo = fields.Selection([
        ('video', 'Video'),
        ('articulo', 'Artículo'),
        ('libro', 'Libro'),
        ('otros', 'Otros')
    ], string="Tipo", required=True, default='otros', help="Tipo del Recurso Educativo")
    fechaPublicacion = fields.Date(string="Fecha de Publicación", help="Fecha de Publicación del Recurso Educativo")
    link = fields.Char(string="Enlace", help="Enlace al Recurso Educativo")
    id_especie = fields.Many2one('upopet.especie', string="Especie", help="Especie relacionada con el Recurso Educativo")

    # Añadimos restricciones para que el id sea único
    _sql_constraints = [('recurso_educativo_id_unique', 'UNIQUE (id_recursoEducativo)', 'Compruebe el ID del Recurso Educativo, debe ser único.')]
