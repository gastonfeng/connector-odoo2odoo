# -*- coding: utf-8 -*-
# © 2015 Malte Jacobi (maljac @ github)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Connector - Odoo2Odoo',
    'summary': 'Base connector for Odoo2Odoo scenarios',
    'version': '0.0.1',
    'category': 'Connector',
    'website': 'https://odoo-community.org/',
    'author': 'IBO Institut (Malte Jacobi), Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'external_dependencies': {
        'python': ['oerplib'],
    },
    'depends': ['base',
                'connector',
                ],
    'data': [
    ],
    'demo': [
    ],
}
