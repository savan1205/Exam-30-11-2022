from odoo import http
from odoo.http import request

class ContactsPage(http.Controller):
	
	#Controller for Opening all Contact's/partner's after clicking Contacts Menu    
	@http.route(route='/contacts',type='http',auth='public',website=True)
	def customer_page(self,**kw):
		contacts = request.env['res.partner'].search([])
		return request.render('savan_30112022.contacts_template_page',{'contacts':contacts})