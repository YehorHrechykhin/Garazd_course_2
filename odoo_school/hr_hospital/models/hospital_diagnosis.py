from odoo import api, models, fields


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Hospital Diagnosis'

    date = fields.Date(
        string='Date of diagnosis',
        default=fields.Date.today,
        required=True,
    )
    doctor_id = fields.Many2one(
        string='The doctor who diagnosed',
        comodel_name='hospital.doctor',
        required=True)
    patient_id = fields.Many2one(
        string='Patient name',
        comodel_name='hospital.patient',
        required=True)
    disease_id = fields.Many2one(
        string='Disease',
        comodel_name='hospital.disease',
        required=True)
    prescribed_to_treat = fields.Text(
        string="Treatment plan",
        required=True)
    comment_of_mentor = fields.Text()

    @api.constrains('doctor_id', 'comments_of_mentor')
    def check_comments_of_mentor(self):
        # If the intern diagnoses the patient, the mentor doctor must add his comment to this diagnosis.
        for diagnosis in self:
            if diagnosis.doctor_id.mentor_id and not diagnosis.comment_of_mentor:
                raise models.ValidationError("Comments from mentor doctor are required")

    def name_get(self):
        result = []
        for rec in self:
            date = rec.date
            result.append((rec.id, date))
        return result
