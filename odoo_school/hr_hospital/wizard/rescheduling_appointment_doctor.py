from odoo import _, models, fields


class ReschedulingAppointmentDoctorWizard(models.TransientModel):
    _name = 'hospital.rescheduling.appointment.doctor.wizard'
    _description = 'Rescheduling an appointment to the doctor'

    appointment_id = fields.Many2one(
        comodel_name='hospital.appointment',
        string='Appointment',
        required=True)
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        required=True)
    appointment_date = fields.Datetime(
        string='Date/time visit',
        default=fields.Datetime.now(),
        required=True)

    def action_open_wizard(self):
        return {
            'name': _('Rescheduling a appointment to the doctor'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.rescheduling.appointment.doctor.wizard',
            'target': 'new',
        }

    def action_change_visit(self):
        self.ensure_one()
        self.appointment_id.write(
            {
                'doctor_id': self.doctor_id.id,
                'start_datetime': self.appointment_date,
            })
