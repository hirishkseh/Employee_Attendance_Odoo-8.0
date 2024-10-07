from openerp import models, fields

class EmployeeAttendance(models.Model):
    _name = 'employee.attendance'
    _description = 'Employee Attendance'

    # Fields for attendance tracking
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    attendance_date = fields.Date(string="Date", required=True, default=fields.Date.today)
    present = fields.Boolean(string="Present", default=False)

    # You can also add computed or other fields as needed
