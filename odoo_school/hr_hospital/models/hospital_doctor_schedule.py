from odoo import models, fields, api


class HospitalDoctorSchedule(models.Model):
    _name = 'hospital.doctor.schedule'
    _description = "Doctor's schedule"

    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Doctor',
        required=True
    )
    appointment_date = fields.Date(
        string='Appointment Date',
        required=True
    )
    appointment_hour = fields.Selection(
        [
            ('08:00', '08:00'),
            ('09:00', '09:00'),
            ('10:00', '10:00'),
            ('11:00', '11:00'),
            ('12:00', '12:00'),
            ('13:00', '13:00'),
            ('14:00', '14:00'),
            ('15:00', '15:00'),
            ('16:00', '16:00'),
            ('17:00', '17:00'),
            ('18:00', '18:00'),
            ('19:00', '19:00'),
            ('20:00', '20:00'),
        ],
        string='Appointment Hour',
        required=True
    )

    @api.constrains('doctor_id', 'appointment_date', 'appointment_hour')
    def check_reception_hour(self):
        # Checking that appointment hours are not repeated.
        for schedule in self:
            domain = [
                ('doctor_id', '=', schedule.doctor_id.id),
                ('appointment_date', '=', schedule.appointment_date),
                ('appointment_hour', '=', schedule.appointment_hour),
            ]
            if len(self.search(domain)) > 1:
                raise models.ValidationError(
                    "This doctor already has a reception scheduled for this hour"
                )
