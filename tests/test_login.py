

def test_login(app):
    # 1) входит в панель администратора http://localhost/litecart/admin
    # 2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
    # 3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)


    # 1) входит в панель администратора http://localhost/litecart/admin
    app.session.open_login_page()

    driver = app.driver
    username = driver.find_elements_by_name('username')
    assert len(username)==1
    password = driver.find_elements_by_name('password')
    assert len(password)==1

    username[0].send_keys('admin')
    password[0].send_keys('admin')

    driver.find_element_by_name('login').click()

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
    # открыть главную страницу
    app.session.open_home_page()













    # 3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
