# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
{
    'name': "hr_hospital",
    'version': "15.0.1.0.0",
    'category': 'Human Resources',
    'summary': """Module for hospital automation""",
    'license': 'LGPL-3',
    'author': "Hrechykhin Yehor",
    #   'website': "http://www.mycompany.com",
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/hospital_disease_data.xml',
        'wizard/hospital_change_doctor_wizard.xml',
        'wizard/hospital_create_disease_report_wizard.xml',
        'wizard/hospital_rescheduling_appointment_doctor_wizard.xml',
        'views/hospital_menus.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_disease_views.xml',
        'views/hospital_diagnosis_views.xml',
        'views/hospital_appointment_views.xml',
        'views/hospital_doctor_schedule_views.xml',
        'report/hospital_disease_report_template.xml',
        'report/hospital_disease_report.xml'
    ],
    'demo': [
        'demo/hospital_doctor_demo.xml',
        'demo/hospital_patient_demo.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
