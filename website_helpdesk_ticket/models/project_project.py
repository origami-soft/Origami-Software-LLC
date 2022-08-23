import logging
from odoo import api, fields, models
_logger = logging.getLogger(__name__)


class ProjectProject(models.Model):
    _inherit = 'project.project'

    helpdesk_team = fields.Many2one('helpdesk.team', string='Helpdesk Team')