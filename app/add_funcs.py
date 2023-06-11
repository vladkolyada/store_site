from app.loader import app
from flask import render_template, flash, redirect, url_for
from .data_base import Products, Laptops, Pcs, Phones, Tablet, Mouse, Keyboard, db


def add_product(product_image_name: str, product_type: str, product_title: str,
                product_price: int):
    product = Products(product_title=product_title, product_type=product_type,
                       product_image_name=product_image_name, product_price=product_price)
    db.session.add(product)
    db.session.commit()


def add_laptop(product_id: int, processor_specifications: str, memory_capacity_specifications: str,
               display_characteristics: str, ram_specifications: str, number_of_ram_slots: int,
               graphics_card_specifications: str, color: str, brand: str, producing_country: str):
    laptop = Laptops(foreign_key=product_id,
                     color=color,
                     brand=brand,
                     producing_country=producing_country,
                     processor_specifications=processor_specifications,
                     memory_capacity_specifications=memory_capacity_specifications,
                     display_characteristics=display_characteristics,
                     ram_specifications=ram_specifications,
                     number_of_ram_slots=number_of_ram_slots,
                     graphics_card_specifications=graphics_card_specifications)
    db.session.add(laptop)
    db.session.commit()


def add_pc(product_id: int, processor_specifications: str, memory_capacity_specifications: str,
           display_characteristics: str, ram_specifications: str, number_of_ram_slots: int,
           graphics_card_specifications: str, color: str, brand: str, producing_country: str):
    laptop = Laptops(foreign_key=product_id,
                     color=color,
                     brand=brand,
                     producing_country=producing_country,
                     processor_specifications=processor_specifications,
                     memory_capacity_specifications=memory_capacity_specifications,
                     display_characteristics=display_characteristics,
                     ram_specifications=ram_specifications,
                     number_of_ram_slots=number_of_ram_slots,
                     graphics_card_specifications=graphics_card_specifications)
    db.session.add(laptop)
    db.session.commit()


def add_phone(product_id: int, processor_specifications: str, memory_capacity_specifications: str,
              display_characteristics: str, ram_specifications: str, number_of_ram_slots: int,
              graphics_card_specifications: str, color: str, brand: str, producing_country: str):
    laptop = Laptops(foreign_key=product_id,
                     color=color,
                     brand=brand,
                     producing_country=producing_country,
                     processor_specifications=processor_specifications,
                     memory_capacity_specifications=memory_capacity_specifications,
                     display_characteristics=display_characteristics,
                     ram_specifications=ram_specifications,
                     number_of_ram_slots=number_of_ram_slots,
                     graphics_card_specifications=graphics_card_specifications)
    db.session.add(laptop)
    db.session.commit()


def add_tablet(product_id: int, processor_specifications: str, memory_capacity_specifications: str,
               display_characteristics: str, ram_specifications: str, number_of_ram_slots: int,
               graphics_card_specifications: str, color: str, brand: str, producing_country: str):
    laptop = Laptops(foreign_key=product_id,
                     color=color,
                     brand=brand,
                     producing_country=producing_country,
                     processor_specifications=processor_specifications,
                     memory_capacity_specifications=memory_capacity_specifications,
                     display_characteristics=display_characteristics,
                     ram_specifications=ram_specifications,
                     number_of_ram_slots=number_of_ram_slots,
                     graphics_card_specifications=graphics_card_specifications)
    db.session.add(laptop)
    db.session.commit()


def add_mouse(product_id: int, processor_specifications: str, memory_capacity_specifications: str,
              display_characteristics: str, ram_specifications: str, number_of_ram_slots: int,
              graphics_card_specifications: str, color: str, brand: str, producing_country: str):
    laptop = Laptops(foreign_key=product_id,
                     color=color,
                     brand=brand,
                     producing_country=producing_country,
                     processor_specifications=processor_specifications,
                     memory_capacity_specifications=memory_capacity_specifications,
                     display_characteristics=display_characteristics,
                     ram_specifications=ram_specifications,
                     number_of_ram_slots=number_of_ram_slots,
                     graphics_card_specifications=graphics_card_specifications)
    db.session.add(laptop)
    db.session.commit()


def add_keyboard(product_id: int, processor_specifications: str, memory_capacity_specifications: str,
                 display_characteristics: str, ram_specifications: str, number_of_ram_slots: int,
                 graphics_card_specifications: str, color: str, brand: str, producing_country: str):
    laptop = Laptops(foreign_key=product_id,
                     color=color,
                     brand=brand,
                     producing_country=producing_country,
                     processor_specifications=processor_specifications,
                     memory_capacity_specifications=memory_capacity_specifications,
                     display_characteristics=display_characteristics,
                     ram_specifications=ram_specifications,
                     number_of_ram_slots=number_of_ram_slots,
                     graphics_card_specifications=graphics_card_specifications)
    db.session.add(laptop)
    db.session.commit()


