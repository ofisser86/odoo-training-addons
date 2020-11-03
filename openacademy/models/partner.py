from odoo import models, fields


class Partner(models.Model):
    _name = 'openacademy.partner'
    _description = 'Openacademy parrtner'

    name = fields.Char(string='Session', required=True)
    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many("openacademy.session", string="Attended Session", readonly=True)
