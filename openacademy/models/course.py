from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Openacademy Course'

    name = fields.Char(string='Title', required=True, help="Course name")
    description = fields.Text()
    responsible_id = fields.Many2one('openacademy.partner', string='Partner Reference')
    session_ids = fields.One2many('openacademy.session', inverse_name='course_id', string='Session Reference')
    level = fields.Selection([('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard'), ], default='easy')
