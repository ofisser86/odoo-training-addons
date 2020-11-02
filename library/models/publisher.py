
from odoo import models, fields


class Publisher(models.Model):
    _name = 'library.publisher'
    _description = 'library.publisher'

    name = fields.Char()
