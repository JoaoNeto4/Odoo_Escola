from odoo import api, fields, models


class BradooEscolasCourse(models.Model):

    _name = "bradoo.escola.course"
    _description = "course"


    name = fields.Char(string='Nome Curso',required=True)

    professor_ids = fields.Many2many(
        comodel_name="hr.employee",
        string="Professores",
        domain=lambda self: [('job_id', '=', self.env.ref('bradoo_escola.job_teacher').id)],
        required=True
    )

    product_id = fields.Many2one(
        comodel_name="product.template", 
        string="Produto", 
        required=True
    )
