from odoo import models, fields


class DiseaseReportWizard(models.TransientModel):
    _name = 'hospital.create.disease.report.wizard'
    _description = 'Disease report'

    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

    def action_print_disease_report(self):
        self.ensure_one()
        domain_line = [
            ('diagnosis_date', '>=', self.start_date),
            ('diagnosis_date', '<=', self.end_date),
        ]
        result = self.env['hospital.diagnosis'].search(domain_line)
        diseases = {}
        diseases_list = []
        for res in result:
            if diseases.get(res.disease_id.name):
                diseases[res.disease_id.name] += 1
            else:
                diseases[res.disease_id.name] = 1
        for key, value in diseases.items():
            diseases_list.append({
                'disease': key,
                'count': value
            })
        data = {
            'diseases': diseases_list
        }
        return self.env.ref('hr_hospital.hospital_disease_report').report_action(self, data=data)
