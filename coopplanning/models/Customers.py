from odoo import models,fields,api

class Customers(models.Model):
	_name = 'brussels.library.customers'
	_description = 'This is a Customers of the brussels.library.'

	Name = fields.Char()

	Address = fields.Char()

	Email = fields.Char()

	Books = fields.One2many("brussels.library.rentals", "customers")



