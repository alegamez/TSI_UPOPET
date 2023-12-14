from odoo import models, fields, api

class pago(models.Model):
    _name = 'upopet.pago'
    _description = 'Modelo para los pagos'

    name = fields.Integer(string="Pago ID", required=True, help="Identificador del pago")
    metodopago_id = fields.Many2one("upopet.metodopago", string="Método de Pago", required=True, help="Método de pago utilizado")
    matricula_id = fields.Many2one("upopet.matricula", string="Matrícula", required=True, help="Matrícula relacionada al pago")

    _sql_constraints = [('pago_name_unique','UNIQUE (name)','El id del pago (name) debe ser único')]

    def btn_generate_report(self):
          return self.env.ref('upopet.report_pagos').report_action(self)