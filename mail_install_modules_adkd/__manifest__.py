# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Af ADKD Install all modules",
    "version": "12.0.1.0.1",
    "author": "Swedish Public Employement Service",
    "license": "AGPL-3",
    "website": "https://arbetsformedlingen.se/",
    "category": "Tools",
    "depends": [
		"mail_autoresponder",		# vertelab/odoo-mail generic module to process automatic newsletters
		"mail_autoresponder_crm",	# vertelab/odoo-mail CRM-addon to glue the module to CRM-specific views
		"mail_browser_view",		# vertelab/odoo-mail upgraded OCA module display the newsletter-email in the webbrowser
	    	"mass_mailing_editor_af", 	# vertelab/odoo-mail Module that adds email-editor snippets with custom Af design
			],
    "application": False,
    "installable": True,
}

