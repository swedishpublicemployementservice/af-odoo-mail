# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Af Secure Messages Install all modules",
    "version": "12.0.1.0.2",
    "author": "Swedish Public Employement Service",
    "maintainer": "Swedish Public Employement Service",
    "contributer": "Swedish Public Employement Service, Vertel AB",
    "description": """
        v12.0.1.0.2 Added tabs to display messages on contact and hr-form \N 
    """,
    "license": "AGPL-3",
    "website": "https://arbetsformedlingen.se/",
    "category": "Tools",
    "depends": [
		"contacts", 
		"hr", 
		"hr_employee_mail_client",	# Displayes messages on a tab on the HR-form
		"mail",
		"partner_mail_client",		# Displayes messages on a tab on the Contact-form
		],
    "application": False,
    "installable": True,
}

