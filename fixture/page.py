import time


class PageHelper:
    def __init__(self, app):
        self.app = app

    def open_menu(self, text):
        elems = self.app.driver.find_element_by_id('box-apps-menu').find_elements_by_id('app-')
        for elem in elems:
            if elem.text == text:
                elem.click()
                break
        h1 = self.app.driver.find_element_by_tag_name('h1')
        assert h1.is_displayed()==True
        assert h1.text == text

    def text_field_fill_by_id(self, id, text):
        if text is not None:
            driver = self.app.driver
            # driver.find_element_by_css_selector('tbody input[name=\'{}\']'.format(id)).click()
            driver.find_element_by_name(id).click()
            driver.find_element_by_name(id).send_keys(text)

    def text_field_fill_by_css(self, css, text):
        if text is not None:
            driver = self.app.driver
            driver.find_element_by_css_selector(css).click()
            driver.find_element_by_css_selector(css).clear()
            driver.find_element_by_css_selector(css).send_keys(text)

    def text_field_fill_by_xpath(self, xpath, text):
        if text is not None:
            driver = self.app.driver
            driver.find_element_by_css_selector('{}'.format(xpath)).click()
            driver.find_element_by_css_selector(xpath).send_keys(text)

    def select_field_fill_by_name(self, id, text):
        if text is not None:
            time.sleep(2)
            driver = self.app.driver
            select = self.app.driver.find_element_by_name(id)

            data = select.text

            data1 = data.split('\n  ')
            data2 = type(text)
            text = text[0]

            if text in data1:
                index = data1.index(str(text))

                self.app.driver.execute_script(
                    'arguments[0].selectedIndex = {}; arguments[0].dispatchEvent(new Event("change"))'.format(index),
                    select)

    def select_field_fill_by_name_base(self, id, text):
        if text != None:
            driver = self.app.driver
            driver.find_element_by_name(id).click()
            select = self.app.Select(driver.find_element_by_name(id))
            select.select_by_visible_text(text)


    def select_field_fill_by_css(self, id, text):
        if text is not None:
            # text = str(text)
            driver = self.app.driver

            select = self.app.driver.find_element_by_css_selector("select[name='zone-code']")

            data = select.text
            data1 = data.split('\n  ')
            text = text[0]

            if text in data1:
                index = data1.index(str(text))

                self.app.driver.execute_script(
                    'arguments[0].selectedIndex = {}; arguments[0].dispatchEvent(new Event("change"))'.format(index), select)


    def textarea_field_fill(self, id, text):
        if text != None:
            driver = self.app.driver
            pass

    def date_field_fill(self, id, text):
        if text != None:
            driver = self.app.driver
            pass

    def tree_field_fill_by_css(self, css, text):
        if text != None:
            driver = self.app.driver
            pass
    def tree_select_category(self, css, name):
        driver = self.app.driver
        elems1 =  driver.find_element_by_css_selector(css)
        elems = elems1.find_elements_by_css_selector('tr')
        for elem in elems:
            if elem.text == name:
                elem.find_element_by_css_selector('td').click()

    def boolean_field_fill_name(self, id, text):
        if text != None:
            driver = self.app.driver
            elems = driver.find_elements_by_css_selector('label'.format(id))
            for elem in elems:
                if elem.text == text:
                    elem.click()

    def input_images(self, css, path):
        if path != None:
            self.app.driver.find_element_by_css_selector(css).send_keys(path)