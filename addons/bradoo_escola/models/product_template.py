from odoo import api, fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"


    is_course = fields.Boolean(string="É curso")