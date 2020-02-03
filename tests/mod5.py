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
        # Спасибо. Освоил работу с составными селекторами. Решают очень большой пласт проблем с выдёргиванием нужных элементов.
        # Не понимаю как я раньше до этого работал.
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


def test_country(app):
    '''Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара в учебном 
    приложении litecart.

    Более точно, нужно открыть главную страницу, выбрать первый товар в блоке Campaigns и проверить следующее:
    
    а) на главной странице и на странице товара совпадает текст названия товара
    б) на главной странице и на странице товара совпадают цены (обычная и акционная)
    в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении 
    одинаковые значения для каналов R, G и B)
    г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы 
    G и B имеют нулевые значения)
    (цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
    д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
    
    Необходимо убедиться, что тесты работают в разных браузерах, желательно проверить во всех трёх ключевых браузерах 
    (Chrome, Firefox, IE).'''
    app.session.open_home_page()