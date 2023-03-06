from odoo import api, models, fields


class HospitalPersonMixin(models.AbstractModel):
    _name = 'hospital.person.mixin'
    _description = 'Hospital Person'

    first_name = fields.Char(
        string='Name',
        required=True
    )
    last_name = fields.Char(
        string='Surname',
        required=True
    )
    full_name = fields.Char(compute='_compute_full_name')
    phone_number = fields.Char(
        string='Telephone number',
        size=10
    )
    image = fields.Image(
        string="Photo",
        max_width=512,
        max_height=512)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-binary')
    ],
        string='Sex'
    )

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.first_name} {record.last_name}"

    def name_get(self):
        result = []
        for rec in self:
            name = rec.full_name
            result.append((rec.id, name))
        return result
