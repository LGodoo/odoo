# -*- coding: utf-8 -*-
{
    'name': "Generate Partner",

    'summary': """
    Verify phone numbers in Odoo checkout form using NumVerify APIs
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "MorePython",
    'website': "http://www.morepython.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account', ],

    # always loaded
    'data': [
        'views/views.xml',
    ]

}