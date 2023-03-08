from odoo import api, models, fields


class HospitalAnalysis(models.Model):
    _name = 'hospital.analysis'
    _description = 'Hospital Analysis'

    name = fields.Char(
        string="Name of analysis",
        required=True
    )
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient name',
        required=True
    )
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        required=True
    )
    phone_number = fields.Char(
        string='Telephone number',
        size=10
    )
    result = fields.Text(required=True)
    result_file = fields.Binary()
    set_date = fields.Datetime(
        string="Data and time of analysis",
        default=lambda self: fields.Datetime.now()
    )

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.phone_number = self.patient_id.phone_number
