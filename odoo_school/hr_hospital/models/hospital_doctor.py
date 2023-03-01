from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctors'
    _inherit = ['hospital.person.mixin']

    specialty = fields.Char(
        string='Medical specialty',
        required=True
    )
    is_intern = fields.Boolean()
    mentor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Mentor',
        domain=[('is_intern', '=', False)])

