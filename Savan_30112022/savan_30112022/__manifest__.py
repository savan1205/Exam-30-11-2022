{
    'name': 'Update Contact',
    'version': '15.0.1.1',
    'summary': 'Update Contact Through Website',
    'sequence': 0,
    'description': """
        This module contains all the features of Configuring Contact through odoo website.
    """,
    'depends': ['website','contacts'],
    'data': [
        'data/contacts_menu.xml',
        'views/contact_form_view.xml',
        'views/contact_view.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,


    'license': 'LGPL-3',

    'assets':{
        'web.assets_frontend':[
            'savan_30112022/static/src/css/contacts_style.css'
        ]

    }

}
