
class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, user='admin', passwd='admin'):
        self.open_login_page()
        driver = self.app.driver
        username = driver.find_elements_by_name('username')
        assert len(username) == 1
        password = driver.find_elements_by_name('password')
        assert len(password) == 1
        username[0].send_keys('%s' % user)
        password[0].send_keys('%s' % passwd)
        driver.find_element_by_name('login').click()
        return driver

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

