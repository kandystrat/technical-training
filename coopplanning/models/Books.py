from odoo import models,fields,api

class Books(models.Model):
	_name = 'Brussels_Library.Books'
	_description = 'This is a book of the Brussels_Library.'

	Title = fields.Char()

	Author = fields.Char()

	Editors = fields.Char()

	Year_of_Edition = fields.Integar()

	ISBN = fields.Char()

	Customer = fields.One2many("Brussels_Library.Rentals", "Books")





