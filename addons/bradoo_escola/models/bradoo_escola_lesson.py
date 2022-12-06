from odoo import api, fields, models

from datetime import datetime


class BradooEscolasLesson(models.Model):

    _name = "bradoo.escola.lesson"
    _description = "Lesson"


    class_id = fields.Many2one(
        comodel_name="bradoo.escola.class", 
        string="Turma",
        required=True,
        domain=[("state", "=","started")]
    )

    professor_id = fields.Many2one(
        comodel_name="hr.employee", 
        string="Professor", 
        related="class_id.professor_id"
    )

    resume = fields.Text(string="Resumo")

    date = fields.Date(string='Data', default=datetime.now())

    attendance_ids = fields.One2many(
        comodel_name="bradoo.escola.attendance", 
        inverse_name="lesson_id" 
    )

    course_name = fields.Char(
        string="Curso",
        related="class_id.course_id.name",
        readonly=True
    )
    
    alumns_present = fields.Integer(
        string="Alunos Presentes", 
        compute="_count_alumns_attendance",
        readonly=True
    )

    alumns_not_present = fields.Integer(
        string="Alunos Ausentes", 
        compute="_count_alumns_not_attendance",
        readonly=True
    )


    def _count_alumns_attendance(self):
        for rec in self:
            res = self.env['bradoo.escola.attendance'].search([
                ('is_present', '=', True),
                ('lesson_id', '=', rec.id )])
            rec.alumns_present = len(res)

    def _count_alumns_not_attendance(self):
        for rec in self:
            res = self.env['bradoo.escola.attendance'].search([
                ('is_present', '=', False),
                ('lesson_id', '=', rec.id )])
            rec.alumns_not_present = len(res)

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f'Turma {record.id} da aula {record.class_id.name}'))
        return res

    def _create_attendances(self):
        self.env['bradoo.escola.attendance'].search([
            ('lesson_id', '=', self.id),
        ]).unlink()

        for alumn in self.class_id.alumn_ids:
            if self.env['bradoo.escola.attendance'].search([
                ('lesson_id', '=', self.id),
                ('alumn_id', '=', alumn.id),
            ]):
                continue

            self.env['bradoo.escola.attendance'].create({
                'lesson_id': self.id,
                'alumn_id': alumn.id,
            })


    def write(self, vals):
        res = super().write(vals)

        if 'class_id' in vals:
            self._create_attendances()

        return res


    @api.model
    def create(self, vals):
        res = super().create(vals)

        if 'class_id' in vals:
            res._create_attendances()
    
        return res

    