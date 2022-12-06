from odoo import fields, models


class HrEmployee(models.Model):

    _inherit = "hr.employee"


    course_id = fields.Many2one(comodel_name="bradoo.escola.course", string="Curso")