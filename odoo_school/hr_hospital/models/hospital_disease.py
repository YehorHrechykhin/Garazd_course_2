from odoo import models, fields


class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Hospital Diseases'
    _parent_name = "parent_id"
    _parent_store = True

    name = fields.Char(
        string='Name of disease',
        required=True
    )
    parent_id = fields.Many2one(
        comodel_name='hospital.disease',
        string='Parent Category',
        index=True,
        ondelete='cascade'
    )
    child_ids = fields.One2many(
        comodel_name='hospital.disease',
        inverse_name='parent_id',
        string='Child Categories'
    )
    parent_path = fields.Char(index=True)
    description = fields.Text(string='Short description')
    symptoms = fields.Text(string='Main symptoms')

    def name_get(self):
        result = []
        for rec in self:
            name = rec.name
            result.append((rec.id, name))
        return result
