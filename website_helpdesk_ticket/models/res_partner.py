import logging
from odoo import api, fields, models
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    project_ids = fields.Many2many('project.project', string='Projects')

