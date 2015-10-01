# -*- coding: utf-8 -*-
# © 2015 Malte Jacobi (maljac @ github)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging
from openerp.addons.connector.unit.mapper import (ExportMapChild,
                                                  ImportMapChild)

_logger = logging.getLogger(__name__)


class IntercompanyExportMapChild(ExportMapChild):

    def format_items(self, item_values):
        items = super(IntercompanyExportMapChild, self).format_items(
            item_values
        )
        # The (0, 0, data) creates a new line, linked to the parent order
        # For an betterexplanation what the tripple (0,0 data) and (5,0) means,
        # see 'Odoo Development Essentials' p.64: 'Setting values for
        # relational fields'
        return [(5, 0)] + [(0, 0, data) for data in items]


class IntercompanyImportMapChild(ImportMapChild):

    def format_items(self, item_values):
        items = super(IntercompanyImportMapChild, self).format_items(
            item_values
        )
        return [(5, 0)] + items
