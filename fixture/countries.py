

class CoutriesHelper:
    def __init__(self, app):
        self.app = app

    def table_get_rows(self):
        driver = self.app.driver
        elems = driver.find_element_by_name('countries_form').find_elements_by_class_name('row')
        return elems

    def open_zone_by_name(self, text):
        header = self.table_get_header_value()
        rows = self.table_get_rows()
        index = header.index(text)
        for row in rows:
            elems = row.find_elements_by_tag_name('a').click()

    def table_get_cels_value_list(self, text):
        # Получить значения Header
        # Сравнить с параметром, Если не верно, выдать ошибку
        # получить список строк.
        # Пройтись по строкам, записывая в лист нужные значения ячейки

        # Получить значения Header
        header = self.table_get_header_value()
        # Сравнить с параметром, Если не верно, выдать ошибку
        assert text in header
        # получить индекс значения list
        index = header.index(text)
        # получить список строк.
        row_list= self.table_get_rows()

        # Пройтись по строкам, записывая в лист нужные значения ячейки
        data = []
        for row in row_list:
            elems = row.find_elements_by_tag_name('td')
            data.append(elems[index].text)
        return data


    def table_get_header_value(self):
        data = []
        driver = self.app.driver
        elems = driver.find_element_by_name('countries_form').find_element_by_class_name('header').find_elements_by_tag_name('th')
        for elem in elems:
            data.append(elem.text.strip())
        return data

    def table_get_footer_value(self):
        pass


    def add_new_geo_zone(self):
        pass

