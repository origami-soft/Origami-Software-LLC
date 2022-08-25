{
    "name": """Website Helpdesk Ticket""",
    "summary": """Add new page in website with a form to create a ticket""",
    "category": "Website",
    "version": "15.0.1.0.0",
    "application": False,
    "author": "Yhasmani Valdes Migenes",
    "license": "LGPL-3",
    "depends": ["helpdesk", "contacts", "project", "website", "website_helpdesk_form"],
    "data": [
        "data/data.xml",
        "views/helpdesk_ticket_view.xml",
        "views/res_partner_view.xml",
        "views/project_project_view.xml",
        "views/templates.xml",
    ],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
}
