from odoo import models, fields


class ReschedulingAppointmentDoctorWizard(models.TransientModel):
    _name = 'hospital.rescheduling.appointment.doctor.wizard'
    _description = 'Rescheduling an appointment to the doctor'

    doctor_id = fields.Many2one(comodel_name='hospital.doctor')
    start_date = fields.Datetime(
        string='Appointment time',
        default=fields.Datetime.today,
    )

    def action_change_appointment_time(self):
        self.ensure_one()
        result = self.env['hospital.appointment'].search([
            ('patient_id.id', '=', self._context['active_id']),
            ('is_done', '=', False),
        ])

        if result:
            result[0].start_date = self.start_date
        else:
            self.env['hospital.appointment'].create({
                'doctor_id': self.doctor_id.id,
                'patient_id': self._context['active_id'],
                'start_date': self.start_date,
            })
