from odoo import models,fields,api

class Books(models.Model):
	_name = 'brussels.library.books'
	_description = 'This is a book of the brussels.library.'

	Title = fields.Char()

	Author = fields.Char()

	Editors = fields.Char()

	Year_of_Edition = fields.Integer()

	ISBN = fields.Char()

	Customer = fields.One2many("brussels.library.rentals", "Books")





