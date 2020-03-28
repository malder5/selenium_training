from model.users import Users

class UsersHelper:
    def __init__(self, app):
        self.app = app

    def fill_fields(self, Users):
        self.app.page.text_field_fill('tax_id', Users.tax_id)
        self.app.page.text_field_fill('company', Users.company)
        self.app.page.text_field_fill('firstname', Users.firstname)
        self.app.page.text_field_fill('lastname', Users.lastname)
        self.app.page.text_field_fill('address1', Users.address1)
        self.app.page.text_field_fill('address2', Users.address2)
        self.app.page.text_field_fill('postcode', Users.postcode)
        self.app.page.text_field_fill('city', Users.city)
        self.app.page.text_field_fill('country_code', Users.country_code)
        self.app.page.text_field_fill('zone_code', Users.zone_code)
        self.app.page.text_field_fill('email', Users.email)
        self.app.page.text_field_fill('phone', Users.phone)
        self.app.page.text_field_fill('newsletter', Users.newsletter)
        self.app.page.text_field_fill('password', Users.password)
        self.app.page.text_field_fill('confirmed_password', Users.confirmed_password)
    def create_account(self):
        driver = self.app.driver

        driver.find_element_by_name('create_account').click()