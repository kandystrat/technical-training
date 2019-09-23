from odoo import models,fields,api

class Rentals(models.Model):
	_name = 'Brussels_Library.Rentals'
	_description = 'This is a Rentals of the Brussels_Library

	Date = fields.date()

	Books = fields.Many2one('Brussels_Library.Customers')

	Customers = fields.Many2one('Brussels_Library_Book')

