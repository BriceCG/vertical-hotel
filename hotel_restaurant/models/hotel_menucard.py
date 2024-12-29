# Copyright (C) 2022-TODAY Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.osv import expression


class HotelMenucardType(models.Model):

    _name = "hotel.menucard.type"  # need to recheck for v15
    _description = "Food Item Type"

    name = fields.Char(required=True)
    menu_id = fields.Many2one("hotel.menucard.type", "Food Item Type")
    child_ids = fields.One2many("hotel.menucard.type", "menu_id", "Child Categories")
    product_properties_definition = fields.PropertiesDefinition("Product Properties")

    def _compute_display_name(self):
        for menu_card in self:
            if menu_card.name and menu_card.menu_id:
                menu_card.display_name = menu_card.menu_id.name + " / " + menu_card.name
            else:
                menu_card.display_name = menu_card.name

    @api.model
    def name_create(self, name):
        menu_card = self.create({'name': name})
        return menu_card.id, menu_card.display_name


class HotelMenucard(models.Model):

    _name = "hotel.menucard"
    _description = "Hotel Menucard"

    product_id = fields.Many2one(
        "product.product",
        "Hotel Menucard",
        required=True,
        delegate=True,
        ondelete="cascade",
        index=True,
    )
    categ_id = fields.Many2one(
        "hotel.menucard.type", "Food Item Category", required=True
    )
    product_manager_id = fields.Many2one("res.users", "Product Manager")
