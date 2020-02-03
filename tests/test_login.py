import time

def test_login(app):
    # 1) входит в панель администратора http://localhost/litecart/admin
    # 2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
    # 3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)


    # 1) входит в панель администратора http://localhost/litecart/admin
    driver = app.session.login()

    # 2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
    menu = driver.find_element_by_id('box-apps-menu')
    elems = menu.find_elements_by_id('app-')
    # elems = menu.find_elements_by_tag_name('a')

    # .login = class
    # #login = id
    # [name] = attribute
    # label:not(.error) - отрицание

    # document.QuerySelectorAll
    # "[name = 'name_element']" равен значению
    #  "[name *= 'name']" содержит текст
    #  "[name $= 'name']" Заканчивается
    #  "[src ^= 'https://']" начинается с текста

    # "[type = 'Button']" - Check attribute value
    # "[checked]" - check attribute
    # "[name]"

    main_menu_count = len(elems)

    for count in range(0,main_menu_count):
        menu = elems[count].find_element_by_tag_name('a')
        menu.click()

        menu = driver.find_element_by_id('box-apps-menu')
        elems = menu.find_elements_by_id('app-')
        #
        module_elem = elems[count]
        links = module_elem.find_elements_by_tag_name('a')

        for sub_menu_count in range(1, len(links)):

            # 3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
            links[sub_menu_count].click()
            h1 = driver.find_element_by_tag_name('h1')
            assert h1.is_displayed()==True

            elems = driver.find_elements_by_id('app-')
            module_elem = elems[count]
            links = module_elem.find_elements_by_tag_name('a')


def test_check_sticker(app):
    '''Сделайте сценарий, проверяющий наличие стикеров у всех товаров в учебном приложении litecart на главной странице.
     Стикеры -- это полоски в левом верхнем углу изображения товара, на которых написано 
     New или Sale или что-нибудь другое. Сценарий должен проверять, что у каждого товара имеется ровно один стикер.'''
    # открыть главную страницу
    app.session.open_home_page()

    box = app.driver.find_element_by_css_selector('#box-most-popular')
    elems = box.find_elements_by_tag_name('li')
    for elem in elems:
        sticker = elem.find_elements_by_class_name('sticker')
        # print(len(sticker))
        assert (len(sticker)) == 1

    box = app.driver.find_element_by_css_selector('#box-campaigns')
    elems = box.find_elements_by_tag_name('li')
    for elem in elems:
        sticker = elem.find_elements_by_class_name('sticker')
        # print(len(sticker))
        assert (len(sticker)) == 1

    box = app.driver.find_element_by_css_selector('#box-latest-products')
    elems = box.find_elements_by_tag_name('li')
    for elem in elems:
        sticker = elem.find_elements_by_class_name('sticker')
        # print(len(sticker))
        assert (len(sticker)) == 1
