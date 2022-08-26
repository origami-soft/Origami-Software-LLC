import logging
from odoo import api, fields, models
_logger = logging.getLogger(__name__)


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    partner_project_id = fields.Many2one('project.project', string='Project')
