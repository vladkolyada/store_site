from flask import render_template, redirect, url_for, flash, request
from .forms import LogInAdmin, RegistrationForm, LoginUser, AddProduct, FormForAddingLaptop, FormForAddingPC, \
    FormForAddingPhone, FormForAddingTablet, FormForAddingMouse, FormForAddingKeyboard
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from app.data_base import AdminUsers, Users, db, Products, Laptops, Pcs, Phones, Tablet, Mouse, Keyboard
from app.loader import app

login = LoginManager(app)
login.login_view = "log_in"


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


@login.user_loader
def load_user(id):
    return AdminUsers.query.get(int(id))


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_name = form.username.data
        email = form.email.data
        password = form.password.data
        user = Users(user_name=user_name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('sign_up.html', form=form)


@login_required
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddProduct()
    if request.method == 'POST':
        file = request.files['lalala_file']
        file.save(f'app/static/{file.filename}')
        print(file)
        product_type = request.form.get('product_type')
        product_title = request.form.get('product_title')
        product_description = request.form.get('product_description')
        product_price = request.form.get('product_price')
        base = Products(product_image_name=file.filename, product_type=product_type,
                        product_title=product_title, product_description=product_description,
                        product_price=product_price)
        db.session.add(base)
        db.session.commit()
        if product_type == "Laptop":
            return redirect(url_for('laptop', image_name=file.filename, product_title=product_title,
                                    description=product_description, price=product_price))
        elif product_type == "PC":
            return redirect(url_for('pc', image_name=file.filename, product_title=product_title,
                                    description=product_description, price=product_price))
        elif product_type == "Phone":
            return redirect(url_for('phone', image_name=file.filename, product_title=product_title,
                                    description=product_description, price=product_price))
        elif product_type == "Tablet":
            return redirect(url_for('tablet', image_name=file.filename, product_title=product_title,
                                    description=product_description, price=product_price))
        elif product_type == "Mouse":
            return redirect(url_for('mouse', image_name=file.filename, product_title=product_title,
                                    description=product_description, price=product_price))
        elif product_type == "Keyboard":
            return redirect(url_for('keyboard', image_name=file.filename, product_title=product_title,
                                    description=product_description, price=product_price))
    return render_template('addproduct.html', form=form)


@app.route('/laptop', methods=['GET', 'POST'])
def laptop():
    form = FormForAddingLaptop()
    image_name = request.args.get('image_name')
    product_title = request.args.get('product_title')
    price = request.args.get('price')
    product = Products.query.filter_by(product_title=product_title).first()
    if request.method == "POST":
        color = request.form.get('color')
        brand = request.form.get('brand')
        processor_specifications = request.form.get('processor_specifications')
        graphics_card_specifications = request.form.get('graphics_card_specifications')
        ram_specifications = request.form.get('ram_specifications')
        memory_capacity_specifications = request.form.get('memory_capacity_specifications')
        display_characteristics = request.form.get('display_characteristics')
        producing_country = request.form.get('producing_country')
        return redirect(url_for('adding_product',
                                foreign_key=product.product_id,
                                product_type="Laptop",
                                color=color,
                                brand=brand,
                                processor_specifications=processor_specifications,
                                graphics_card_specifications=graphics_card_specifications,
                                ram_specifications=ram_specifications,
                                memory_capacity_specifications=memory_capacity_specifications,
                                display_characteristics=display_characteristics,
                                producing_country=producing_country))
    return render_template('add_laptop.html', image_name=image_name,
                           product_title=product_title, price=price,
                           form=form)


@app.route('/PC', methods=['GET', 'POST'])
def pc():
    form = FormForAddingPC()
    image_name = request.args.get('image_name')
    product_title = request.args.get('product_title')
    price = request.args.get('price')
    product = Products.query.filter_by(product_title=product_title).first()
    if request.method == "POST":
        color = request.form.get('color')
        number_of_ram_slots = int(request.form.get('number_of_ram_slots'))
        specifications_motherboard = request.form.get('specifications_motherboard')
        processor_specifications = request.form.get('processor_specifications')
        graphics_card_specifications = request.form.get('graphics_card_specifications')
        ram_specifications = request.form.get('ram_specifications')
        memory_capacity_specifications = request.form.get('memory_capacity_specifications')
        cpu_cooling = request.form.get('cpu_cooling')
        power_supply_specifications = request.form.get('power_supply_specifications')
        case_characteristics = request.form.get('case_characteristics')
        return redirect(url_for('adding_product',
                                foreign_key=product.product_id,
                                product_type="PC",
                                color=color,
                                processor_specifications=processor_specifications,
                                graphics_card_specifications=graphics_card_specifications,
                                ram_specifications=ram_specifications,
                                memory_capacity_specifications=memory_capacity_specifications,
                                number_of_ram_slots=number_of_ram_slots,
                                specifications_motherboard=specifications_motherboard,
                                cpu_cooling=cpu_cooling,
                                power_supply_specifications=power_supply_specifications,
                                case_characteristics=case_characteristics))
    return render_template('add_pc.html', image_name=image_name, product_title=product_title, price=price, form=form)


@app.route('/Phone', methods=['GET', 'POST'])
def phone():
    form = FormForAddingPhone()
    image_name = request.args.get('image_name')
    product_title = request.args.get('product_title')
    price = request.args.get('price')
    product = Products.query.filter_by(product_title=product_title).first()
    if request.method == "POST":
        return redirect(url_for('adding_product',
                                foreign_key=product.product_id,
                                product_type="Phone",
                                brand=request.form.get('brand'),
                                color=request.form.get('color'),
                                communication_standard_or_internet=request.form.get(
                                    'communication_standard_or_internet'),
                                display_characteristics=request.form.get('display_characteristics'),
                                sim_card_characteristics=request.form.get('sim_card_characteristics'),
                                characteristics_memory_functions=request.form.get('characteristics_memory_functions'),
                                operating_system=request.form.get('operating_system'),
                                characteristics_of_the_front_camera=request.form.get(
                                    'characteristics_of_the_front_camera'),
                                processor_specifications=request.form.get('processor_specifications'),
                                characteristics_of_the_main_camera=request.form.get(
                                    'characteristics_of_the_main_camera'),
                                power_characteristics=request.form.get('power_characteristics'),
                                connectors=request.form.get('connectors'),
                                navigation=request.form.get('navigation'),
                                dimensions=request.form.get('dimensions'),
                                producing_country=request.form.get('producing_country')))
    return render_template('add_phone.html', image_name=image_name, product_title=product_title, price=price, form=form)


@app.route('/Tablet', methods=['GET', 'POST'])
def tablet():
    form = FormForAddingTablet()
    image_name = request.args.get('image_name')
    product_title = request.args.get('product_title')
    price = request.args.get('price')
    product = Products.query.filter_by(product_title=product_title).first()
    if request.method == "POST":
        return redirect(url_for('adding_product',
                                foreign_key=product.product_id,
                                product_type="Tablet",
                                brand=request.form.get('brand'),
                                color=request.form.get('color'),
                                display_characteristics=request.form.get('display_characteristics'),
                                characteristics_memory_functions=request.form.get('characteristics_memory_functions'),
                                operating_system=request.form.get('operating_system'),
                                characteristics_of_the_front_camera=request.form.get(
                                    'characteristics_of_the_front_camera'),
                                processor_specifications=request.form.get('processor_specifications'),
                                characteristics_of_the_main_camera=request.form.get(
                                    'characteristics_of_the_main_camera'),
                                power_characteristics=request.form.get('power_characteristics'),
                                connectors=request.form.get('connectors'),
                                navigation=request.form.get('navigation'),
                                dimensions=request.form.get('dimensions'),
                                producing_country=request.form.get('producing_country')))
    return render_template('add_tablet.html', image_name=image_name,
                           product_title=product_title, price=price,
                           form=form)


@app.route('/Keyboard', methods=['GET', 'POST'])
def keyboard():
    form = FormForAddingKeyboard()
    image_name = request.args.get('image_name')
    product_title = request.args.get('product_title')
    price = request.args.get('price')
    product = Products.query.filter_by(product_title=product_title).first()
    if request.method == 'POST':
        return redirect(url_for('adding_product',
                                product_type="Keyboard",
                                foreign_key=product.product_id,
                                number_of_keyboard_buttons=request.form.get('number_of_keyboard_buttons'),
                                connection=request.form.get('connection'),
                                producing_country=request.form.get('producing_country'),
                                color=request.form.get('color'),
                                brand=request.form.get('brand'),
                                backlight_color=request.form.get('backlight_color'),
                                keyboard_layout=request.form.get('keyboard_layout'),
                                interface=request.form.get('interface'),
                                weight=request.form.get('weight'),
                                appointment=request.form.get('appointment'),
                                cable_length=request.form.get('cable_length'),
                                dimensions=request.form.get('dimensions')
                                ))
    return render_template('add_keyboard.html', image_name=image_name,
                           product_title=product_title, price=price,
                           form=form)


@app.route('/Mouse', methods=['GET', 'POST'])
def mouse():
    form = FormForAddingMouse()
    image_name = request.args.get('image_name')
    product_title = request.args.get('product_title')
    price = request.args.get('price')
    product = Products.query.filter_by(product_title=product_title).first()
    if request.method == 'POST':
        return redirect(url_for('adding_product',
                                product_type="Mouse",
                                foreign_key=product.product_id,
                                number_of_mouse_buttons=request.form.get('number_of_mouse_buttons'),
                                connection=request.form.get('connection'),
                                size=request.form.get('size'),
                                sensor_type=request.form.get('sensor_type'),
                                producing_country=request.form.get('producing_country'),
                                color=request.form.get('color'),
                                brand=request.form.get('brand'),
                                interface=request.form.get('interface'),
                                weight=request.form.get('weight'),
                                cable_length=request.form.get('cable_length'),
                                dimensions=request.form.get('dimensions'),
                                additional_functions=request.form.get('additional_functions')
                                ))
    return render_template('add_mouse.html', image_name=image_name,
                           product_title=product_title, price=price,
                           form=form)


@app.route('/adding_product', methods=["GET", "POST"])
def adding_product():
    product_type = request.args.get('product_type')
    if product_type == "Laptop":
        data_laptop = Laptops(foreign_key=request.args.get('foreign_key'),
                              color=request.args.get('color'),
                              brand=request.args.get('brand'),
                              processor_specifications=request.args.get('processor_specifications'),
                              graphics_card_specifications=request.args.get('graphics_card_specifications'),
                              ram_specifications=request.args.get('ram_specifications'),
                              memory_capacity_specifications=request.args.get('memory_capacity_specifications'),
                              display_characteristics=request.args.get('display_characteristics'),
                              producing_country=request.args.get('producing_country'))
        db.session.add(data_laptop)
        db.session.commit()
        return redirect('/')
    if product_type == "PC":
        data_pc = Pcs(foreign_key=request.args.get('foreign_key'),
                      color=request.args.get('color'),
                      number_of_ram_slots=int(request.args.get('number_of_ram_slots')),
                      specifications_motherboard=request.args.get('specifications_motherboard'),
                      processor_specifications=request.args.get('processor_specifications'),
                      graphics_card_specifications=request.args.get('graphics_card_specifications'),
                      ram_specifications=request.args.get('ram_specifications'),
                      memory_capacity_specifications=request.args.get('memory_capacity_specifications'),
                      cpu_cooling=request.args.get('cpu_cooling'),
                      power_supply_specifications=request.args.get('power_supply_specifications'),
                      case_characteristics=request.args.get('case_characteristics'))
        db.session.add(data_pc)
        db.session.commit()
        return redirect('/')
    if product_type == "Phone":
        data_phone = Phones(foreign_key=request.args.get('foreign_key'),
                            brand=request.args.get('brand'),
                            color=request.args.get('color'),
                            communication_standard_or_internet=request.args.get('communication_standard_or_internet'),
                            display_characteristics=request.args.get('display_characteristics'),
                            sim_card_characteristics=request.args.get('sim_card_characteristics'),
                            characteristics_memory_functions=request.args.get('characteristics_memory_functions'),
                            operating_system=request.args.get('operating_system'),
                            characteristics_of_the_front_camera=request.args.get('characteristics_of_the_front_camera'),
                            processor_specifications=request.args.get('processor_specifications'),
                            characteristics_of_the_main_camera=request.args.get('characteristics_of_the_main_camera'),
                            power_characteristics=request.args.get('power_characteristics'),
                            connectors=request.args.get('connectors'),
                            navigation=request.args.get('navigation'),
                            dimensions=request.args.get('dimensions'),
                            producing_country=request.args.get('producing_country'))
        db.session.add(data_phone)
        db.session.commit()
        return redirect('/')
    if product_type == "Tablet":
        data_tablet = Tablet(foreign_key=request.args.get('foreign_key'),
                             brand=request.args.get('brand'),
                             color=request.args.get('color'),
                             display_characteristics=request.args.get('display_characteristics'),
                             characteristics_memory_functions=request.args.get('characteristics_memory_functions'),
                             operating_system=request.args.get('operating_system'),
                             characteristics_of_the_front_camera=request.args.get('characteristics_of_the_front_camera'),
                             processor_specifications=request.args.get('processor_specifications'),
                             characteristics_of_the_main_camera=request.args.get('characteristics_of_the_main_camera'),
                             power_characteristics=request.args.get('power_characteristics'),
                             connectors=request.args.get('connectors'),
                             navigation=request.args.get('navigation'),
                             dimensions=request.args.get('dimensions'),
                             producing_country=request.args.get('producing_country'))
        db.session.add(data_tablet)
        db.session.commit()
        return redirect('/')
    if product_type == "Keyboard":
        data_keyboard = Keyboard(foreign_key=request.args.get('foreign_key'),
                                 number_of_keyboard_buttons=request.args.get('number_of_keyboard_buttons'),
                                 connection=request.args.get('connection'),
                                 producing_country=request.args.get('producing_country'),
                                 color=request.args.get('color'),
                                 brand=request.args.get('brand'),
                                 backlight_color=request.args.get('backlight_color'),
                                 keyboard_layout=request.args.get('keyboard_layout'),
                                 interface=request.args.get('interface'),
                                 weight=request.args.get('weight'),
                                 appointment=request.args.get('appointment'),
                                 cable_length=request.args.get('cable_length'),
                                 dimensions=request.args.get('dimensions'))
        db.session.add(data_keyboard)
        db.session.commit()
        return redirect('/')
    if product_type == "Mouse":
        data_mouse = Mouse(foreign_key=request.args.get('foreign_key'),
                           number_of_mouse_buttons=request.args.get('number_of_mouse_buttons'),
                           connection=request.args.get('connection'),
                           size=request.args.get('size'),
                           sensor_type=request.args.get('sensor_type'),
                           producing_country=request.args.get('producing_country'),
                           color=request.args.get('color'),
                           brand=request.args.get('brand'),
                           interface=request.args.get('interface'),
                           weight=request.args.get('weight'),
                           cable_length=request.args.get('cable_length'),
                           dimensions=request.args.get('dimensions'),
                           additional_functions=request.args.get('additional_functions'))
        db.session.add(data_mouse)
        db.session.commit()
        return redirect('/')


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    form = LoginUser()
    if current_user.is_authenticated:
        return redirect('/')
    if form.validate_on_submit():
        user = Users.query.filter_by(user_name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/log_in')
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('log_in.html', form=form)


@app.route('/log_in_for_admins', methods=['GET', 'POST'])
def log_in_admin():
    form = LogInAdmin()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = AdminUsers.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return redirect('/log_in_for_admins')
        login_user(user, remember=form.remember_me.data)
        return redirect('/add_product')
    return render_template('registeradmin.html', title='Увійти', form=form)
