from odoo import http
from odoo.http import request
from odoo.addons.website.controllers import form


class WebsiteForm(form.WebsiteForm):

    def _handle_website_form(self, model_name, **kwargs):
        partner_project_id = request.params.get('partner_project_id')
        if partner_project_id:
            project_id = request.env['project.project'].sudo().search([('id', '=', partner_project_id)], limit=1)
            if project_id and project_id.helpdesk_team:
                request.params['team_id'] = project_id.helpdesk_team.id

        return super(WebsiteForm, self)._handle_website_form(model_name, **kwargs)


class HelpdeskTicket(http.Controller):

    @http.route(['/create_ticket_custom'], type='http', auth='user', website=True)
    def helpdesk_ticket_data(self):
        context = dict(request.context)
        ticket_types = request.env['helpdesk.ticket.type'].sudo().with_context(context).search([])
        return request.render('website_helpdesk_ticket.helpdesk_ticket_create', {'ticket_type_ids': ticket_types})
