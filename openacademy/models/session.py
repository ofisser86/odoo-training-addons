from odoo import models, fields


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Openacademy Session'

    name = fields.Char(string='Session', required=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done')], default='draft')
    start_date = fields.Date("Start Date", default=fields.Date.today)
    stop_date = fields.Date("Stop Date", default=fields.Date.today)
    duration = fields.Float(string="Duration", default=1.0, help="Duration in days")
    instructor_id = fields.Many2one(comodel_name='openacademy.partner')
    course_id = fields.Many2one(comodel_name='openacademy.course',  ondelete="cascade", string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    active = fields.Boolean(default=True)
    seats = fields.Integer(string="Number of seats")
