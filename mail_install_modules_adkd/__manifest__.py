# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Af ADKD Install all modules",
    "version": "12.0.1.0.1",
    "author": "Swedish Public Employement Service",
    "license": "AGPL-3",
    "website": "https://arbetsformedlingen.se/",
    "category": "Tools",
    "depends": [
		"mail_autoresponder",		# generic module to process automatic newsletters
		"mail_autoresponder_crm",	# CRM-addon to glue the module to CRM-specific views
		"mail_browser_view",		# OCA module display the newsletter-email in the webbrowser
			],
    "application": False,
    "installable": True,
}

