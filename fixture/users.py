from model.users import Users
import time

class UsersHelper:
    def __init__(self, app):
        self.app = app

    def fill_fields(self, Users):
        time.sleep(1)
        self.app.page.text_field_fill_by_id('tax_id', Users.tax_id)
        # self.app.page.text_field_fill('company', Users.company)
        self.app.page.text_field_fill_by_id('firstname', Users.firstname)
        self.app.page.text_field_fill_by_id('lastname', Users.lastname)
        self.app.page.text_field_fill_by_id('address1', Users.address1)
        # self.app.page.text_field_fill('address2', Users.address2)
        self.app.page.text_field_fill_by_id('postcode', Users.postcode)
        self.app.page.text_field_fill_by_id('city', Users.city)
        self.app.page.select_field_fill_by_name('country_code', Users.country_code)
        # self.app.page.select_field_fill_by_css('tbody select[name="zone-code"]', Users.zone_code)

        # self.app.page.select_field_fill_by_name('zone-code', Users.zone_code)
        self.app.page.text_field_fill_by_id('email', Users.email)
        self.app.page.text_field_fill_by_id('phone', Users.phone)
        # self.app.page.text_field_fill('newsletter', Users.newsletter)  # Чебокс
        self.app.page.text_field_fill_by_id('password', Users.password)
        self.app.page.text_field_fill_by_id('confirmed_password', Users.confirmed_password)

    def create_account(self):
        driver = self.app.driver
        driver.find_element_by_name('create_account').click()