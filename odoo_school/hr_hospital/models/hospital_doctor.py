from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctors'
    _inherit = ['hospital.person.mixin']

    specialty = fields.Char(
        string='Medical specialty',
        required=True
    )
    color = fields.Integer()
    is_intern = fields.Boolean()
    mentor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        domain=[('is_intern', '=', False)]
    )
    intern_ids = fields.One2many(
        comodel_name='hospital.doctor',
        inverse_name='mentor_id',
    )
    patient_ids = fields.One2many(
        comodel_name='hospital.patient',
        inverse_name='doctor_id',
    )
    appointment_ids = fields.One2many(
        comodel_name='hospital.appointment',
        inverse_name='doctor_id'
    )

    def action_new_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Appointments',
            'res_model': 'hospital.appointment',
            'domain': [],
            'context': {'default_doctor_id': self.id},
            'views': [[False, 'form']],
            'target': 'current',
        }
