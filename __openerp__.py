{
    'name': 'Employee Attendance',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Module for Employee Attendance',
    'description': """
Employee Attendance Management
==============================
This module allows you to record and manage employee attendance 0.1.
""",
    'author': 'Your Name',
    'website': 'http://www.google.com',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',  
        'views.xml',  
    ],
    'installable': True,
    'application': True,
    'auto_install': True,

}
