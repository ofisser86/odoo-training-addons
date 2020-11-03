# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.openacademy'
    _description = 'openacademy.openacademy'

    name = fields.Char()
