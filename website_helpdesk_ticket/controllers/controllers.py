import logging
from odoo.http import request
# from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import fields, http, tools

_logger = logging.getLogger(__name__)


class HelpdeskTicket(http.Controller):

    @http.route(['/create_ticket'], type='http', auth='user', website=True)
    def get_ticket_data(self):
        partner_id = request.env['res.users'].browse(request.uid).partner_id
        return request.render('website_helpdesk_ticket.helpdesk_ticket_create',
                              {'partner_id': partner_id})
