# -*- coding: utf-8 -*-

{
    'name': 'Bdtask Core Banking',
    'version': '1.0',
    'summary': 'Core Banking',
    'description': 'Core Banking',
    'category': 'Core Banking',
    'author': 'Bdtask',
    'company': 'Bdtask Limited',
    'maintainer': '',
    'depends': ['base'],
    'website': 'https://www.bdtask.com/',
    'data': [
    'security/ir.model.access.csv',

    'views/administrator.xml',
    'views/manager.xml',
    'views/auditor.xml',
    'views/regulator.xml',
    ],
    
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
