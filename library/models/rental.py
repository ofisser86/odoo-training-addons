from odoo import models, fields


class Rental(models.Model):
    _name = 'library.rental'
    _description = 'library_rental'

    customer_id = fields.Many2one('library.partner')
    book_id = fields.Many2one('library.book')
    rental_date = fields.Date('Rental date')
    return_date = fields.Date('Return date')

    # customer_address = fields.Many2one('partner.address')
    # customer_email = fields.Many2one('partner.email')
    # book_authors = fields.Many2many('book.author_ids')
    # book_edition_date = fields.Many2one('book.edition_date')
    # book_publisher = fields.Many2one('publisher.name')
