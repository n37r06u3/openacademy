# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "n37r06u3",
    'website': "http://www.devecho.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'report'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'openacademy.xml',
        'data.xml',
        'partner.xml',
        'session_workflow.xml',
        'reports.xml',
        'session_board.xml'
    ],
    # only loaded in demonstration mode
    'demo': [

    ],

}