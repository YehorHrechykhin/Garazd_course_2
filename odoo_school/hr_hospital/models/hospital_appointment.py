from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointments'

    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient name',
        required=True
    )
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Doctor name',
        required=True
    )
    start_datetime = fields.Datetime(
        string='Date and time of appointment',
        required=True
    )
    diagnosis_id = fields.Many2one(
        comodel_name='hospital.diagnosis',
        string='Diagnosis',
    )

    is_done = fields.Boolean(
        string='Appointment Done',
        default=False
    )

    @api.model
    def create(self, vals):
        # Checking that it is not possible to record at the same time twice.
        existing_appointment = self.env['hospital.appointment'].search([
            ('doctor_id', '=', vals.get('doctor_id')),
            ('start_datetime', '=', vals.get('start_datetime'))
        ], limit=1)
        if existing_appointment:
            raise ValidationError('An appointment already exists for the selected date and time.')
        return super(HospitalAppointment, self).create(vals)

    def write(self, vals):
        # Prohibit changing the time/date/doctor of a visit that has already taken place.
        for appointment in self:
            if appointment.start_datetime < fields.Datetime.now():
                if 'start_datetime' in vals or 'doctor_id' in vals or 'patient_id' in vals:
                    raise UserError(
                        "You cannot change the date, time, doctor,"
                        " or patient of an appointment that has already taken place.")
        return super().write(vals)

    def unlink(self):
        # Prohibit deleting visits with diagnoses.
        for appointment in self:
            if appointment.diagnosis_id:
                raise UserError("You cannot delete an appointment that has a diagnosis.")
        return super().unlink()

    def archive(self):
        # Prohibit archiving visits with diagnoses.
        for appointment in self:
            if appointment.diagnosis_id:
                raise UserError("You cannot archive an appointment that has a diagnosis.")
        return super().archive()

    def name_get(self):
        result = []
        for rec in self:
            date = rec.start_datetime
            result.append((rec.id, date))
        return result
