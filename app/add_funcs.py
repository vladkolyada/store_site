from app.loader import app
from flask import render_template, flash, redirect, url_for
from .data_base import Products, Laptops, db


def add_laptop(product_image_name: str, product_type: str, product_title: str,
               product_price: int, processor_specifications: str, memory_capacity_specifications: str,
               display_characteristics: str, ram_specifications: str, number_of_ram_slots: int,
               graphics_card_specifications: str):
    laptop_product = Products(product_title=product_title, product_type=product_type,
                              product_image_name=product_image_name, product_price=product_price)
    laptop_specs = Laptops(foreign_key=laptop_product.product_id,
                           processor_specifications=processor_specifications,
                           memory_capacity_specifications=memory_capacity_specifications,
                           display_characteristics=display_characteristics,
                           ram_specifications=ram_specifications,
                           number_of_ram_slots=number_of_ram_slots,
                           graphics_card_specifications=graphics_card_specifications)
    db.session.add(laptop_product)
    db.session.add(laptop_specs)
    db.session.commit()

