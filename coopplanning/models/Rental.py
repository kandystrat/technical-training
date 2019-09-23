from odoo import models,fields,api

class Rentals(models.Model):
	_name = 'brussels.library.rentals'
	_description = 'This is a Rentals of the brussels library'

	Date = fields.Date()

	Books = fields.Many2one('brussels.library.customers')

	Customers = fields.Many2one('brussels.library.book')

