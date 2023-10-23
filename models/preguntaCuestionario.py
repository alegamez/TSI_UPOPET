# -*- coding: utf-8 -*-

from odoo import models, fields

class PreguntaCuestionario(models.Model):
    _name = 'tu_modulo.pregunta_cuestionario'
    _description = 'Modelo para Preguntas de Cuestionario'

    id_pregunta = fields.Char(string="Pregunta ID", required=True, help="Identificador de la Pregunta")
    texto = fields.Text(string="Texto de la Pregunta", required=True, help="Texto de la Pregunta")
    tipoRespuesta = fields.Selection([
        ('opcion_simple', 'Opción Simple'),
        ('opcion_multiple', 'Opción Múltiple'),
        ('texto_libre', 'Texto Libre')
    ], string="Tipo de Respuesta", required=True, default='texto_libre', help="Tipo de Respuesta para la Pregunta")
    categoria = fields.Char(string="Categoría", help="Categoría de la Pregunta")
    
    
    # Añadimos restricciones para que el id sea único
    _sql_constraints = [('pregunta_id_unique', 'UNIQUE (id_pregunta)', 'Compruebe el ID de la Pregunta, debe ser único.')]
