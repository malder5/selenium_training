from model.add_new_product import AddNewProduct

class AddNewProductHelper:
    def __init__(self, app):
        self.app = app

    def open_page(self):
        # Открыть каталог
        self.app.page.open_menu('Catalog')
        # нажать на кнопку "новый продукт"
        self.click_button('Add New Product')

    def click_button(self, text):
        buttons = self.app.driver.find_elements_by_css_selector('.button')
        for button in buttons:
            if button.text == text:
                button.click()

    def check_section(self, AddNewProduct):
        if AddNewProduct.manufacturer_id!=None or \
            AddNewProduct.supplier_id != None or \
            AddNewProduct.keywords != None or  \
            AddNewProduct.short_description != None or \
            AddNewProduct.description != None:
            # Открыть info

            pass

        elif AddNewProduct.sku != None or \
            AddNewProduct.gtin!=None or \
            AddNewProduct.taric != None or \
            AddNewProduct.weight != None or \
            AddNewProduct.weight_class != None or \
            AddNewProduct.Width != None or \
            AddNewProduct.Height != None or \
            AddNewProduct.Length != None or \
            AddNewProduct.dim_class != None:
            # Open Data

            pass

        elif AddNewProduct.purchase_price != None or \
            AddNewProduct.purchase_price_currency_code != None or \
            AddNewProduct.tax_class_id != None or \
            AddNewProduct.pricesUSD != None or\
            AddNewProduct.gross_pricesUSD != None or\
            AddNewProduct.pricesEUR != None or\
            AddNewProduct.gross_pricesEUR != None:

            pass




    def fill_fields(self, AddNewProduct):

        self.app.page.boolean_field_fill_name('status', AddNewProduct.status)
        self.app.page.text_field_fill_by_id('name', AddNewProduct.name)
        self.app.page.text_field_fill_by_id('code', AddNewProduct.code)
        self.app.page.tree_field_fill('categories', AddNewProduct.categories)
        self.app.page.select_field_fill('default_category', AddNewProduct.default_category)
        self.app.page.tree_field_fill('product_groups', AddNewProduct.product_groups)
        self.app.page.text_field_fill_by_id('quantity', AddNewProduct.quantity)
        self.app.page.select_field_fill('quantity_unit', AddNewProduct.quantity_unit)
        self.app.page.select_field_fill('delivery_status', AddNewProduct.delivery_status)
        self.app.page.select_field_fill('sold_out_status', AddNewProduct.sold_out_status)
        self.app.page.text_field_fill_by_id('upload_images', AddNewProduct.upload_images)
        self.app.page.text_field_fill_by_id('date_valid_form', AddNewProduct.date_valid_form)
        self.app.page.text_field_fill_by_id('date_valid_to', AddNewProduct.date_valid_to)

        self.check_section(AddNewProduct)

        self.app.page.text_field_fill_by_id('manufacturer_id', AddNewProduct.manufacturer_id)
        self.app.page.text_field_fill_by_id('supplier_id', AddNewProduct.supplier_id)
        self.app.page.text_field_fill_by_id('keywords', AddNewProduct.keywords)
        self.app.page.text_field_fill_by_id('short_description', AddNewProduct.short_description)
        self.app.page.text_field_fill_by_id('description', AddNewProduct.description)

        self.app.page.text_field_fill_by_id('sku', AddNewProduct.sku)
        self.app.page.text_field_fill_by_id('gtin', AddNewProduct.gtin)
        self.app.page.text_field_fill_by_id('taric', AddNewProduct.taric)
        self.app.page.text_field_fill_by_id('weight', AddNewProduct.weight)
        self.app.page.text_field_fill_by_id('weight_class', AddNewProduct.weight_class)
        self.app.page.text_field_fill_by_id('Width', AddNewProduct.Width)
        self.app.page.text_field_fill_by_id('Height', AddNewProduct.Height)
        self.app.page.text_field_fill_by_id('Length', AddNewProduct.Length)
        self.app.page.text_field_fill_by_id('dim_class', AddNewProduct.dim_class)


        self.app.page.text_field_fill_by_id('purchase_price', AddNewProduct.purchase_price)
        self.app.page.text_field_fill_by_id('purchase_price_currency_code', AddNewProduct.purchase_price_currency_code)
        self.app.page.text_field_fill_by_id('tax_class_id', AddNewProduct.tax_class_id)
        self.app.page.text_field_fill_by_id('pricesUSD', AddNewProduct.pricesUSD)
        self.app.page.text_field_fill_by_id('gross_pricesUSD', AddNewProduct.gross_pricesUSD)
        self.app.page.text_field_fill_by_id('pricesEUR', AddNewProduct.pricesEUR)
        self.app.page.text_field_fill_by_id('gross_pricesEUR', AddNewProduct.gross_pricesEUR)