
class Session(Models.model):
	_name = 'openacademy.session'
	_description = 'This is a course of the Westeros Library.'

	name = fields.Char

	start_date = fields.Datetime()

	end_date = fields.Datetime()

	course_id = fields.Many2one ('openacademy.course')

	teacher_id = fields.Many2one ('openacademy.person')

	attendee_ids = fields.Many2many('openacademy.perons')

	room_capacity = fields.Integer()