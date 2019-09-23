from odoo import models,fields,api

class Customers(models.Model):
	_name = 'Brussels_Library.Customers'
	_description = 'This is a Customers of the Brussels_Library.'

	Name = fields.Char()

	Address = fields.Char()

	Email = fields.Char()

	Books = fields.One2many("Brussels_Library.Rentals", "Customers")



