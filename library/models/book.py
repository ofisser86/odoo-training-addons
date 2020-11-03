from odoo import models, fields


class Book(models.Model):
    _name = 'library.book'
    _description = 'library_book'

    name = fields.Char()
    author_ids = fields.Many2many('library.partner')
    edition_date = fields.Date('Edition date')
    isbn = fields.Char()
    publisher_id = fields.Many2one('library.publisher')
    rental_ids = fields.One2many('library.rental', inverse_name='book_id')
