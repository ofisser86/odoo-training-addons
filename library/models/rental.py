from odoo import models, fields


class Rental(models.Model):
    _name = 'library.rental'
    _description = 'library_rental'

    customer_id = fields.Many2one('library.partner')
    book_id = fields.Many2one('library.book')
    rental_date = fields.Date('Rental date')
    return_date = fields.Date('Return date')
