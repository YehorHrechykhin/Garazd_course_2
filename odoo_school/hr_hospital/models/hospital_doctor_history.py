from odoo import fields, models


class HospitalDoctorHistory(models.Model):
    _name = 'hospital.doctor.history'
    _description = 'History of Personal Doctor Changes'

    set_date = fields.Datetime(
        string='Date and Time of set',
        default=lambda self: fields.Datetime.now()
    )
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        ondelete='cascade'
    )
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        required=True
    )
