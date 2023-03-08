from odoo import api, models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patients'
    _inherit = ['hospital.person.mixin']

    birthday = fields.Date(
        string='Birthday date',
        required=True)
    age = fields.Integer(
        string='Full years',
        compute='_compute_age',
        store=True
    )
    passport_data = fields.Char(string='Passport №')
    contact_person_id = fields.Many2one(comodel_name='hospital.contact_person')
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Attending doctor',
        required=True
    )
    change_doctor_history_ids = fields.One2many(
        comodel_name='hospital.doctor.history',
        inverse_name='patient_id',
    )
    diagnosis_history_ids = fields.One2many(
        comodel_name='hospital.diagnosis',
        inverse_name='patient_id',
    )
    analysis_history_ids = fields.One2many(
        comodel_name='hospital.analysis',
        inverse_name='patient_id'
    )

    @api.depends('birthday')
    def _compute_age(self):
        """Calculated age from the current date"""
        for record in self:
            if record.birthday:
                age = (fields.Date.today() - record.birthday).days // 365
                record.age = age

    @api.onchange('doctor_id')
    def onchange_doctor_id(self):
        """Create new record to hospital.doctor.history
         when you change patient's doctor"""
        if self.doctor_id:
            self.env['hospital.doctor.history'].create({
                'patient_id': self._origin.id,
                'doctor_id': self.doctor_id.id,
            })

    def action_open_appointment_history(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointment',
            'res_model': 'hospital.appointment',
            'domain': [('patient_id', '=', self.id)],
            'context': {},
            'views': [[False, 'tree']],
            'target': 'current',
        }

    def action_open_analysis_history(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'Analyses',
            'res_model': 'hospital.analysis',
            'domain': [('patient_id', '=', self.id)],
            'context': {},
            'views': [[False, 'tree']],
            'target': 'current',
        }

    def action_new_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Appointment',
            'res_model': 'hospital.appointment',
            'domain': [],
            'context': {'default_patient_id': self.id},
            'views': [[False, 'form']],
            'target': 'current',
        }
