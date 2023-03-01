from odoo import models


class ContactPerson(models.Model):
    _name = 'hospital.contact_person'
    _description = 'Hospital Contact person'
    _inherit = ['hospital.person.mixin']
