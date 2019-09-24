# -*- coding: utf-8 -*-
from odoo import fields, models


class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')

    book_isbn = fields.Char(string='ISBN', related="book_id.isbn")
    book_author_ids = fields.Many2many("library.partner", string="Authors", related="book_id.author_ids")
    partner_email = fields.Char(string='Email', related="customer_id.email")
    parnter_address = fields.Text(string="Address", related="customer_id.address")

    rental_date = fields.Date()
    return_date = fields.Date()
