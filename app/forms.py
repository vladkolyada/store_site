from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo


class LogInAdmin(FlaskForm):
    password = PasswordField('password', validators=[DataRequired()])
    username = StringField('name', validators=[DataRequired()])
    remember_me = BooleanField('Remember?')
    submit = SubmitField('Enter')


class AddProduct(FlaskForm):
    product_image_name = StringField('Імя_зображення_продукту', validators=[DataRequired()])
    product_type = StringField('Тип_продукту', validators=[DataRequired()])
    product_title = StringField('Назва_продукту', validators=[DataRequired()])
    product_description = StringField('Опис_продукту', validators=[DataRequired()])
    product_price = StringField('Ціна_товару', validators=[DataRequired()])
    submit = SubmitField('Enter')


class LoginUser(FlaskForm):
    password = PasswordField('password', validators=[DataRequired()])
    username = StringField('name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    remember_me = BooleanField('Remember?')
    submit = SubmitField('Enter')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



class Otpavka(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    phone = StringField('number', validators=[DataRequired()])
    adressa = SelectField('adressa', choices=[('Kiev', 'Kiev'), ('chernivci', 'Chernivci')])
    dostavka = SelectField('sposib dostavki', choices=[('Ukrposhta', 'Ukrposhta'), ('olx', 'Olx')])
    send = SubmitField('Submit')


class FormForAddingLaptop(FlaskForm):
    color = StringField('Колір')
    brand = StringField('Бренд')
    processor_specifications = StringField('Характеристики процесора')
    graphics_card_specifications = StringField('Характеристики відеокарти')
    ram_specifications = StringField('Характеристики оперативної пам`яті')
    memory_capacity_specifications = StringField('Характеритики об`єму пам`яті')
    display_characteristics = StringField('Характеристики дисплея')
    producing_country = StringField('Країна виробник')
    submit = SubmitField('Enter')


class FormForAddingPC(FlaskForm):
    color = StringField('Колір корпусу')
    processor_specifications = StringField('Характеристики процесора')
    graphics_card_specifications = StringField('Характеристики відеокарти')
    ram_specifications = StringField('Характеристики оперативної пам`яті')
    number_of_ram_slots = StringField('Кількість планок оперативної пам`яті(Напишіть тільки число)')
    memory_capacity_specifications = StringField('Характеритики об`єму пам`яті')
    specifications_motherboard = StringField('Характеристики материнської плати')
    cpu_cooling = StringField('Охолодження процесора')
    power_supply_specifications = StringField('Характеристики блока живлення')
    submit = SubmitField('Enter')
    case_characteristics = StringField('Характеристики корпуса')


class FormForAddingPhone(FlaskForm):
    brand = StringField('Бренд')
    color = StringField('Колір')
    communication_standard_or_internet = StringField('Характеристики інтернету')
    display_characteristics = StringField('Характеристики дисплея')
    sim_card_characteristics = StringField('Характеристики SIM-картки')
    characteristics_memory_functions = StringField('Характеристики функції пам`яті')
    operating_system = StringField('Операційна система')
    characteristics_of_the_front_camera = StringField('Характеристики селфі камери')
    processor_specifications = StringField('Характеристики процесора')
    characteristics_of_the_main_camera = StringField('Характеристики головної камери')
    power_characteristics = StringField('Характеристики батареї')
    connectors = StringField('Роз`єми')
    navigation = StringField('Навігація')
    dimensions = StringField('Розміри')
    producing_country = StringField('Країна виробник')
    submit = SubmitField('Enter')


class FormForAddingTablet(FlaskForm):
    brand = StringField('Бренд')
    color = StringField('Колір')
    display_characteristics = StringField('Характеристики дисплея')
    characteristics_memory_functions = StringField('Характеристики функції пам`яті')
    operating_system = StringField('Операційна система')
    characteristics_of_the_front_camera = StringField('Характеристики селфі камери')
    processor_specifications = StringField('Характеристики процесора')
    characteristics_of_the_main_camera = StringField('Характеристики головної камери')
    power_characteristics = StringField('Характеристики батареї')
    connectors = StringField('Роз`єми')
    navigation = StringField('Навігація')
    dimensions = StringField('Розміри')
    producing_country = StringField('Країна виробник')
    submit = SubmitField('Enter')


class FormForAddingMouse(FlaskForm):
    connection = StringField('Приєднання')
    size = StringField('Розмір')
    interface = StringField('Інтерфейс')
    number_of_mouse_buttons = StringField('Кількість кнопок на миші(Напишіть тільки число)')
    color = StringField('Колір')
    brand = StringField('Бренд')
    weight = StringField('Вага')
    sensor_type = StringField('Тип сенсора')
    additional_functions = StringField('Додаткові функції')
    dimensions = StringField('Розміри')
    cable_length = StringField('Довжина кабелю')
    producing_country = StringField('Країна виробник')
    submit = SubmitField('Enter')


class FormForAddingKeyboard(FlaskForm):
    number_of_keyboard_buttons = StringField('Кількість кнопок на клавіатурі(Напишіть тільки число)')
    connection = StringField('Приєднання')
    producing_country = StringField('Країна виробник')
    color = StringField('Колір')
    brand = StringField('Бренд')
    backlight_color = StringField('Колір підсвітки')
    keyboard_layout = StringField('Розкладка')
    interface = StringField('Інтерфейс')
    weight = StringField('Вага')
    appointment = StringField('Призначення')
    cable_length = StringField('Довжина кабелю')
    dimensions = StringField('Розміри')
    submit = SubmitField('Enter')

