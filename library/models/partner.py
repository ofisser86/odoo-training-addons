from odoo import models, fields


class Partner(models.Model):
    _name = 'library.partner'
    _description = 'library_partner'

    name = fields.Char()
    email = fields.Char()
    address = fields.Text()
    partner_type = fields.Selection([('customer', 'Customer'), ('author', 'Author')])
    rental_ids = fields.One2many('library.rental', inverse_name='customer_id')
