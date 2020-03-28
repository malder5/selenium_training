from model.add_new_product import AddNewProduct

class new_product:
    def __init__(self, app):
        self.app = app

    def fill_fields(self, AddNewProduct):
        driver = self.app.driver

        self.app.page.boolean_field_fill_name('status', AddNewProduct.status)
        self.app.page.text_field_fill_by_css('input[name="name[en]"]', AddNewProduct.name)
        self.app.page.text_field_fill_by_css('input[name="code"]', AddNewProduct.code)
        # self.app.page.tree_field_fill('input[name="code"]', AddNewProduct.code)
        self.app.page.tree_select_category('#tab-general tr:nth-child(4) div',AddNewProduct.categories)
        self.app.page.select_field_fill_by_name_base('default_category_id', AddNewProduct.default_category)
        self.app.page.tree_select_category('#tab-general tr:nth-child(7) div', AddNewProduct.product_groups)
        self.app.page.input_images('input[name="new_images[]"]', AddNewProduct.upload_images)


    def select_field(self, name):
        driver = self.app.driver

        select = self.app.Select()


