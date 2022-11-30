from odoo import http
from odoo.http import request


class ContactsForm(http.Controller):

	#Dynamic Controller for Opening the selected Contact's/partner's Configuration form    
    @http.route('/contact/<model("res.partner"):contact>', type='http', auth="public", website=True)
    def contact_details(self, contact, **kw):
        return request.render('savan_30112022.contact_details_template', {'contact': contact})

    #Controller for Updating values to Contacts/Res.partner Model    
    @http.route(route='/update/contact', type='http', auth='public', website=True)
    def contact_update(self, **kw):

        request.env['res.partner'].search([('id', '=', kw.get('c_id'))]).write({
            'name': kw.get('name'),
            'phone': kw.get('phone'),
            'email': kw.get('email'),
        })

        return request.render('website.contactus_thanks', {})
