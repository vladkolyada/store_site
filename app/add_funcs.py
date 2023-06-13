from app.loader import app
from flask import render_template, flash, redirect, url_for
from .data_base import Products, Laptops, Pcs, Phones, Tablet, Mouse, Keyboard, db


def add_product(product_image_name: str, product_type: str, product_title: str,
                product_price: int):
    product = Products(product_title=product_title, product_type=product_type,
                       product_image_name=product_image_name, product_price=product_price)
    db.session.add(product)
    db.session.commit()


def add_laptop_specs(product_id: int, processor_specifications: str, memory_capacity_specifications: str,
                     display_characteristics: str, ram_specifications: str, graphics_card_specifications: str,
                     color: str, brand: str, producing_country: str):
    laptop = Laptops(foreign_key=product_id,
                     color=color,
                     brand=brand,
                     producing_country=producing_country,
                     processor_specifications=processor_specifications,
                     memory_capacity_specifications=memory_capacity_specifications,
                     display_characteristics=display_characteristics,
                     ram_specifications=ram_specifications,
                     graphics_card_specifications=graphics_card_specifications)
    db.session.add(laptop)
    db.session.commit()


def add_pc_specs(product_id: int, processor_specifications: str, memory_capacity_specifications: str,
                 specifications_motherboard: str, ram_specifications: str, number_of_ram_slots: int,
                 graphics_card_specifications: str, color: str, cpu_cooling: str, power_supply_specifications: str,
                 case_characteristics: str):
    pc = Pcs(foreign_key=product_id,
             color=color,
             processor_specifications=processor_specifications,
             graphics_card_specifications=graphics_card_specifications,
             ram_specifications=ram_specifications,
             number_of_ram_slots=number_of_ram_slots,
             specifications_motherboard=specifications_motherboard,
             memory_capacity_specifications=memory_capacity_specifications,
             cpu_cooling=cpu_cooling,
             power_supply_specifications=power_supply_specifications,
             case_characteristics=case_characteristics)
    db.session.add(pc)
    db.session.commit()


def add_phone_specs(product_id: int,
                    brand: str,
                    color: str,
                    communication_standard_or_internet: str,
                    display_characteristics: str,
                    sim_card_characteristics: str,
                    characteristics_memory_functions: str,
                    operating_system: str,
                    characteristics_of_the_front_camera: str,
                    processor_specifications: str,
                    characteristics_of_the_main_camera: str,
                    power_characteristics: str,
                    connectors: str,
                    navigation: str,
                    dimensions: str,
                    producing_country: str):
    phone = Phones(foreign_key=product_id,
                   brand=brand,
                   color=color,
                   communication_standard_or_internet=communication_standard_or_internet,
                   display_characteristics=display_characteristics,
                   sim_card_characteristics=sim_card_characteristics,
                   characteristics_memory_functions=characteristics_memory_functions,
                   operating_system=operating_system,
                   characteristics_of_the_front_camera=characteristics_of_the_front_camera,
                   processor_specifications=processor_specifications,
                   characteristics_of_the_main_camera=characteristics_of_the_main_camera,
                   power_characteristics=power_characteristics,
                   connectors=connectors,
                   navigation=navigation,
                   dimensions=dimensions,
                   producing_country=producing_country)
    db.session.add(phone)
    db.session.commit()


def add_tablet_specs(product_id: int,
                     brand: str,
                     color: str,
                     display_characteristics: str,
                     characteristics_memory_functions: str,
                     operating_system: str,
                     characteristics_of_the_front_camera: str,
                     processor_specifications: str,
                     characteristics_of_the_main_camera: str,
                     power_characteristics: str,
                     connectors: str,
                     navigation: str,
                     dimensions: str,
                     producing_country: str):
    tablet = Tablet(foreign_key=product_id,
                    brand=brand,
                    color=color,
                    display_characteristics=display_characteristics,
                    characteristics_memory_functions=characteristics_memory_functions,
                    operating_system=operating_system,
                    characteristics_of_the_front_camera=characteristics_of_the_front_camera,
                    processor_specifications=processor_specifications,
                    characteristics_of_the_main_camera=characteristics_of_the_main_camera,
                    power_characteristics=power_characteristics,
                    connectors=connectors,
                    navigation=navigation,
                    dimensions=dimensions,
                    producing_country=producing_country)
    db.session.add(tablet)
    db.session.commit()


def add_mouse_specs(product_id: int,
                    connection: str,
                    size: str,
                    interface: str,
                    number_of_mouse_buttons: str,
                    color: str,
                    brand: str,
                    weight: str,
                    sensor_type: str,
                    additional_functions: str,
                    dimensions: str,
                    cable_length: str,
                    producing_country: str):

    mouse = Mouse(foreign_key=product_id,
                  connection=connection,
                  size=size,
                  interface=interface,
                  number_of_mouse_buttons=number_of_mouse_buttons,
                  brand=brand,
                  weight=weight,
                  sensor_type=sensor_type,
                  additional_functions=additional_functions,
                  dimensions=dimensions,
                  cable_length=cable_length,
                  producing_country=producing_country)

    db.session.add(mouse)
    db.session.commit()


def add_keyboard_specs(product_id: int,
                       number_of_keyboard_buttons: str,
                       connection: str,
                       producing_country: str,
                       color: str,
                       brand: str,
                       backlight_color: str,
                       keyboard_layout: str,
                       interface: str,
                       weight: str,
                       appointment: str,
                       cable_length: str,
                       dimensions: str):
    keyboard = Keyboard(foreign_key=product_id,
                        number_of_keyboard_buttons=number_of_keyboard_buttons,
                        connection=connection,
                        producing_country=producing_country,
                        color=color,
                        brand=brand,
                        backlight_color=backlight_color,
                        keyboard_layout=keyboard_layout,
                        interface=interface,
                        weight=weight,
                        appointment=appointment,
                        cable_length=cable_length,
                        dimensions=dimensions)
    db.session.add(keyboard)
    db.session.commit()


