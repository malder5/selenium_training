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


