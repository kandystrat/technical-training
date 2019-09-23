class Person(Models.model):
	_name = 'openacademy.person'
	_description = 'This is a course of the Westeros Library.'

	name = fields.char()

	is_teacher = fields.Boolean()

	session_ids = fields.Many2many("openacademy.session")

