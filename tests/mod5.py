# Добавить обёртку к логину админа
# Убрать драйвера в PATH. Перенести драйвера в папку TOOLS
import time


def test_geo_zone(app):
    '''1) на странице http://localhost/litecart/admin/?app=countries&doc=countries
    а) провер   ить, что страны расположены в алфавитном порядке
    б) для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить, 
    что зоны расположены в алфавитном порядке
    # 
    2) на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones
    зайти в каждую из стран и проверить, что зоны расположены в алфавитном порядке'''
    app.session.login()
    app.page.open_menu('Geo Zones')
    #Получить значения зон в виде списка
    zone_list = app.geozones.table_get_cels_value_list('Name')
    # отсортировать
    sort_zone_list = sorted(zone_list)
    # Проверить, что они отсортированы
    assert zone_list == sort_zone_list

    # Прокликать те страны, зоны которых отличные от нуля.
    rows = app.geozones.table_get_rows()

    # Прокликать
    for row in range(0,len(rows)):
        # Если третье поле не равно 0, то
        rows = app.geozones.table_get_rows()
        elem = rows[row].find_element_by_tag_name('a')
        elem.click()

        # Проверяем, что открылась страница редактирования Геозоны
        h1 = app.driver.find_element_by_tag_name('h1').text
        assert h1 == 'Edit Geo Zone'

        # Проверяем, что открылась нужная нам карточка
        value = app.driver.find_element_by_name('form_geo_zone')\
            .find_element_by_name('name').get_attribute('value')
        assert value in zone_list

        # Получаем список геозон в виде листа. Все select с атрибутов входящим в name *= zones[1][zone_code]
        elems = app.driver.find_element_by_id('table-zones').find_elements_by_css_selector("#table-zones [name $= '[zone_code]']")
        data = []
        for elem in elems:
            name = elem.find_element_by_css_selector("[selected = 'selected']").text
            data.append(name)
        data_sort = sorted(data)
        assert data == data_sort

        # Нажать на кнопку.
        button_click(app, 'Cancel')


def button_click(app, name_button):
    buttons_menu = app.driver.find_element_by_class_name('button-set')
    elems = buttons_menu.find_elements_by_tag_name('button')
    data = []
    for elem in elems:
        data.append(elem.get_attribute('value'))
    assert name_button in data
    for elem in elems:
        if elem.get_attribute('value') == name_button:
            elem.click()
            break


def test_countries(app):
    app.session.login()
    app.page.open_menu('Countries')

    counties_list = app.countries.table_get_cels_value_list('Name')
    # отсортировать
    counties_list_sorted = sorted(counties_list)
    # Проверить, что они отсортированы
    assert counties_list == counties_list_sorted

    # Прокликать те страны, зоны которых отличные от нуля.
    rows = app.countries.table_get_rows()


    # Прокликать
    for row in range(0, len(rows)):
        # Если третье поле не равно 0, то
        rows = app.countries.table_get_rows()
        cols = rows[row].find_elements_by_tag_name('td')
        col = int(cols[-2].text)
        if col != 0:

            elem = rows[row].find_element_by_tag_name('a')
            name = elem.text
            elem.click()

            # Проверяем, что открылась страница редактирования Геозоны
            h1 = app.driver.find_element_by_tag_name('h1').text
            assert h1 == 'Edit Country'

            # Проверяем, что открылась нужная нам карточка

            new_name = app.driver.find_element_by_name('name').get_attribute('value')

            assert name == new_name


            # Получаем список геозон в виде листа. Все select с атрибутов входящим в name *= zones[1][zone_code]

            # #table-zones > tbody > tr:nth-child(2) > td:nth-child(3)
            elems = app.driver.find_elements_by_css_selector("#table-zones td:nth-child(3)")
            #
            data = []
            for elem in elems:
                name = elem.text
                if name != '':
                    data.append(name)
            data_sort = sorted(data)
            assert data == data_sort

            # Нажать на кнопку.
            button_click(app, 'Cancel')

def test_campaigns(app):
    '''
    Более точно, нужно открыть главную страницу, выбрать первый товар в блоке Campaigns и проверить следующее:
    
    +) на главной странице и на странице товара совпадает текст названия товара
    +) на главной странице и на странице товара совпадают цены (обычная и акционная)
    +) обычная цена 
        [+] зачёркнутая и    
        [+] серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
    +) акционная 
        [+] жирная и 
        [+] красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
    (цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
    +) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
    '''
    app.session.open_home_page()
    app.driver.find_element_by_id("box-campaigns")
    # собираем карточки продукта
    elems = app.driver.find_element_by_id("box-campaigns").find_elements_by_class_name('product')
    page = {}
    for elem in elems:
        # Есть ли вообще цены
        assert elem.find_elements_by_class_name('regular-price') != []
        assert elem.find_elements_by_class_name('campaign-price') != []

        # Имя
        page['name'] = elem.find_element_by_class_name('name').text
        # Цена
        page['price'] = elem.find_element_by_class_name('regular-price').text
        # каталожная цена должна быть серой
        color = elem.find_element_by_class_name('regular-price').value_of_css_property('color')
        color = color.replace('rgba(','').replace(')', '').split(',')
        assert int(color[0])==int(color[1])
        assert int(color[0])==int(color[2])
        # Каталожная цена должна быть зачёркнутой
        data = elem.find_element_by_class_name('regular-price').get_attribute('tagName')
        assert data == 'S'


        # Красная цена
        page['sale'] = elem.find_element_by_class_name('campaign-price').text
        # Красная цена должна быть красной
        color = elem.find_element_by_class_name('campaign-price').value_of_css_property('color')
        color = color.replace('rgba(','').replace(')', '').split(',')
        assert int(color[0])!=0
        assert int(color[1])==0
        assert int(color[2])==0

        # Красная цена должна быть жирной.
        data = elem.find_element_by_class_name('campaign-price').get_attribute('tagName')
        assert data == 'STRONG'

        # проверить размеры цены каталога и красной цены.
        red_price = elem.find_element_by_class_name('campaign-price').get_attribute('offsetHeight')
        price = elem.find_element_by_class_name('regular-price').get_attribute('offsetHeight')
        assert price<red_price

        # Открыть карточку товара

        link = elem.find_element_by_class_name('link')
        app.driver.execute_script('arguments[0].target = "_blank";', link)
        link.click()
        app.driver.switch_to.window(app.driver.window_handles[1])

        page2 = {}
        # Имя
        page2['name'] = app.driver.find_element_by_tag_name('h1').text
        # Цена
        page2['price'] = app.driver.find_element_by_class_name('regular-price').text
        # каталожная цена должна быть серой
        color = app.driver.find_element_by_class_name('regular-price').value_of_css_property('color')
        color = color.replace('rgba(', '').replace(')', '').split(',')
        assert int(color[0]) == int(color[1])
        assert int(color[0]) == int(color[2])
        # Каталожная цена должна быть зачёркнутой
        data = app.driver.find_element_by_class_name('regular-price').get_attribute('tagName')
        assert data == 'S'

        # Красная цена
        page2['sale'] = app.driver.find_element_by_class_name('campaign-price').text
        # Красная цена должна быть красной
        color = app.driver.find_element_by_class_name('campaign-price').value_of_css_property('color')
        color = color.replace('rgba(', '').replace(')', '').split(',')
        assert int(color[0]) != 0
        assert int(color[1]) == 0
        assert int(color[2]) == 0

        # Красная цена должна быть жирной.
        data = app.driver.find_element_by_class_name('campaign-price').get_attribute('tagName')
        assert data == 'STRONG'

        # проверить размеры цены каталога и красной цены.
        red_price = app.driver.find_element_by_class_name('campaign-price').get_attribute('offsetHeight')
        price = app.driver.find_element_by_class_name('regular-price').get_attribute('offsetHeight')
        assert price < red_price

        assert page['name']==page2['name']

