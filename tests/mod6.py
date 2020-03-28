from model.users import Users
from model.add_new_product import AddNewProduct
from random import randrange
import time

def test_new_user(app):

    '''
    Сценарий должен состоять из следующих частей:
    
    1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты
    (чтобы не конфликтовало с ранее созданными пользователями, в том числе при предыдущих запусках того же самого сценария),
    2) выход (logout), потому что после успешной регистрации автоматически происходит вход,
    3) повторный вход в только что созданную учётную запись,
    4) и ещё раз выход.
    
    В качестве страны выбирайте United States, штат произвольный. При этом формат индекса -- пять цифр.
    
    Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.
    '''

    # Цель - зарегистрировать нового пользователя
    # открыть страницу магазина
    app.session.open_home_page()
    # открыть поле для новых пользователей.
    app.driver.find_element_by_css_selector('#box-account-login tr:nth-child(5)').click()
    # заполнить поля
    email = ''

    for index in range (0, 11):
        email+=str(randrange(0, 9))
    phone = email
    email+='@mail.ru'

    app.users.fill_fields(Users(
        # company='1223',
        firstname='123',
        lastname='23',
        address1='123',
        postcode='12345',
        city='123',
        country_code='United States',
        # zone_code="Colorado",
        email=email,
        phone = phone,
        password=phone,
        confirmed_password=phone
    ))

    # нажать на кнопку "создать аккаунт"
    app.users.create_account()

    # нажать логаут
    app.driver.find_element_by_css_selector('.list-vertical li:nth-child(4) > a').click()
    # залогиниться
    app.driver.find_element_by_css_selector("input[name='email']").click()
    app.driver.find_element_by_css_selector("input[name='email']").send_keys(email)

    app.driver.find_element_by_css_selector("input[name='password']").click()
    app.driver.find_element_by_css_selector("input[name='password']").send_keys(phone)

    app.driver.find_element_by_css_selector("button[name='login']").click()


    # проверить, что открылась нужная страница

    # Ещё раз выход
    app.driver.find_element_by_css_selector('.list-vertical li:nth-child(4) > a').click()

def test_add_product(app):

    app.session.login()
    time.sleep(2)
    # Открыть каталог

    app.page.open_menu('Catalog')
    # нажать на кнопку "новый продукт"
    # app.click_button(app, 'Add New Product')
    text_button = 'Add New Product'

    elems = app.driver.find_elements_by_css_selector('a.button')
    for elem in elems:
        if text_button in elem.text:
            elem.click()
            time.sleep(2)
    assert app.driver.find_element_by_css_selector('h1').text == 'Add New Product'

    # Вкладка General
    app.new_product.fill_fields(AddNewProduct(
        status='Enabled',
        name='123',
        code = '123',
        categories='Subcategory',
        default_category='Subcategory',
        product_groups='Male',
        upload_images=None,
        date_valid_form=None,
        date_valid_to=None
        ))

    # app.addnewproduct(AddNewProduct(
    #     status='Enable
    #     ))d',
    #     # name=None,
    #     # code=None,
    #     # categories=None,
    #     # default_category=None,
    #     # product_groups=None,
    #     # quantity=None,
    #     # quantity_unit=None,
    #     # delivery_status=None,
    #     # sold_out_status=None,
    #     # upload_images=None,
    #     # date_valid_form=None,
    #     # date_valid_to=None,
    # ))

    # Вкладка Information
    # app.addnewproduct(AddNewProduct(
    #     manufacturer_id=None,
    #     supplier_id=None,
    #     keywords=None,
    #     short_description=None,
    #     description=None,
    # ))
    # Вкладка Prices
    # app.addnewproduct(AddNewProduct(
    #     purchase_price=None,
    #     purchase_price_currency_code=None,
    #     tax_class_id=None,
    #     pricesUSD=None,
    #     gross_pricesUSD=None,
    #     pricesEUR=None,
    #     gross_pricesEUR=None
    # ))
    # Добавить картинку
    # Проверить, что добавилось в админке.