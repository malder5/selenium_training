
class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_login(username, password)
        pass

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_id('sidebar').find_element_by_class_name('header')

    def open_home_page(self):
        driver = self.app.driver

        link = 'http://localhost/litecart'
        driver.get(link)

    def open_login_page(self):
        driver = self.app.driver
        link = 'http://localhost/litecart/admin/login.php'
        driver.get(link)

        # if driver.current_url != 'http://localhost/litecart/admin/':

