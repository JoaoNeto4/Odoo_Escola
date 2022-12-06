from odoo import api, fields, models


class BradooEscolaAttendance(models.Model):

    _name = "bradoo.escola.attendance"
    _description = "attendance"


    lesson_id = fields.Many2one(
        comodel_name="bradoo.escola.lesson", 
        string="Turma", required=True
    )

    alumn_id = fields.Many2one(comodel_name="res.partner", string="Alunos")
    
    is_present = fields.Boolean(string='Presente')
