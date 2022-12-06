from odoo import api, fields, models

from odoo.exceptions import UserError


class BradooEscolaClass(models.Model):

    _name = "bradoo.escola.class"
    _description = "Classroom"


    name = fields.Char(string="Nome da Turma", required=True)

    course_id = fields.Many2one(
        comodel_name="bradoo.escola.course", 
        string="Curso", 
        required=True
    )

    professor_id = fields.Many2one(comodel_name="hr.employee", string="Professor")

    alumn_ids = fields.Many2many(
        comodel_name="res.partner", 
        string="Alunos",
        compute="_compute_alumn_ids"
    )

    state = fields.Selection(
        selection=[
            ("draft", "Em formação"),
            ("started", "Iniciada"),
            ("done", "Finalizada"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="draft",
    )

    course_professor_ids = fields.Many2many(related='course_id.professor_ids')

    alumns_count = fields.Integer(
        string='Qtd. Alunos', 
        compute='_count_alumns_course', 
        readonly=True
    )


    def _count_alumns_course(self):
        for rec in self:
            rec.alumns_count = len(rec.alumn_ids.mapped('id'))

    @api.depends('course_id')
    def _compute_alumn_ids(self):
        for rec in self:
            sale_order_ids = self.env['sale.order'].search([
                ('order_line.product_template_id', '=', rec.course_id.product_id.id), 
                ('state', '=', 'sale')
            ])
            rec.alumn_ids = sale_order_ids.mapped('partner_id')

    def action_init_class(self):
        if not "draft" in self.mapped("state"):
            raise UserError("A turma ja está iniciada.")
        return self.write({"state": "started"})

    def action_stop_class(self):
        if "done" in self.mapped("state"):
            raise UserError("A turma ja está encerrada")
        return self.write({"state": "done"})
    
    