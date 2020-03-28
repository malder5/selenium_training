from model.users import Users
from random import randrange

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
    '''
    Сделайте сценарий для добавления нового товара (продукта) в учебном приложении litecart (в админке).
    Для добавления товара нужно открыть меню Catalog, в правом верхнем углу нажать кнопку "Add New Product",
    заполнить поля с информацией о товаре и сохранить.
    Достаточно заполнить только информацию на вкладках General, Information и Prices. Скидки (Campains) на
    вкладке Prices можно не добавлять.
    Переключение между вкладками происходит не мгновенно, поэтому после переключения можно сделать небольшую
    паузу (о том, как делать более правильные ожидания, будет рассказано в следующих занятиях).
    Картинку с изображением товара нужно уложить в репозиторий вместе с кодом. При этом указывать в коде
    полный абсолютный путь к файлу плохо, на другой машине работать не будет. Надо средствами языка программирования
    преобразовать относительный путь в абсолютный.
    '''

    app.session.login()

    # Открыть каталог
    # app.page.open_menu('Catalog')
    # нажать на кнопку "новый продукт"
    # app.click_button(app, 'Add New Product')

    app.addnewproduct.open_page()
    # Вкладка General
    # Вкладка Information
    # Вкладка Prices

    # Добавить картинку
    # Проверить, что добавилось в админке.
    pass