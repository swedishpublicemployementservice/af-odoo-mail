# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Af ADKD Install all modules",
    "version": "12.0.1.0.2",
    "author": "Swedish Public Employement Service",
    "license": "AGPL-3",
    "website": "https://arbetsformedlingen.se/",
    "category": "Tools",
    "description": """
	 v12.0.1.0.1 New Module.\n
	 v12.0.1.0.2 Added mass_mailaing_editor\n
    """,
    "depends": [
		"mail_autoresponder",		# vertelab/odoo-mail generic module to process automatic newsletters
		"mail_autoresponder_crm",	# vertelab/odoo-mail CRM-addon to glue the module to CRM-specific views
		"mail_browser_view",		# vertelab/odoo-mail upgraded OCA module display the newsletter-email in the webbrowser
	    	"mass_mailing_editor_af", 	# vertelab/odoo-mail Module that adds email-editor snippets with custom Af design
	    	"mail_improved_tracking_value", # oca/social Module that lists changes in fields in a convinient way for audit-loggin
			],
    "application": False,
    "installable": True,
}

