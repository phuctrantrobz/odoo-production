# -*- coding: utf-8 -*-
# Copyright (C) 2016-Today: La Louve (<http://www.lalouve.net/>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{
    'name': 'Louve Custom - Point of Sale Custom views',
    'version': '9.0.1.0.0',
    'category': 'Custom',
    'summary': 'Customize Point of Sale Display',
    'author': 'La Louve',
    'website': 'http://www.lalouve.net',
    'depends': [
        'point_of_sale',
        'pos_report_total_vat_excluded'
    ],
    'data': [
        'static/src/xml/templates.xml',
        'views/view_pos_order.xml',
    ],
    'qweb': [
        'static/src/xml/point_of_sale.xml',
    ],
    'installable': True,
}
