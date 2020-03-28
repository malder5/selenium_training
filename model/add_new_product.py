class AddNewProduct():

    def __init__(self,
                 status = None,
                 name = None,
                 code = None,
                 categories = None,
                 default_category = None,
                 product_groups = None,
                 quantity = None,
                 quantity_unit = None,
                 delivery_status = None,
                 sold_out_status = None,
                 upload_images = None,
                 date_valid_form = None,
                 date_valid_to = None,
                 # Information
                 manufacturer_id = None,
                 supplier_id = None,
                 keywords = None,
                 short_description = None,
                 description = None,
                 # Data
                 sku = None,
                 gtin = None,
                 taric = None,
                 weight = None,
                 weight_class = None,
                 Width = None,
                 Height = None,
                 Length = None,
                 dim_class = None,
                 # Prices
                 purchase_price = None,
                 purchase_price_currency_code = None,
                 tax_class_id = None,
                 pricesUSD = None,
                 gross_pricesUSD = None,
                 pricesEUR = None,
                 gross_pricesEUR = None
                 # Options

                 # Options Stock


                 ):
        self.status = status                    # Булевое
        self.name = name                        # Текстовое
        self.code = code                        # Текстовое
        self.categories = categories            # Дерево
        self.default_category = default_category# Селект
        self.product_groups = product_groups    # Дерево
        self.quantity = quantity                # Текстовое
        self.quantity_unit = quantity_unit      # Селект
        self.delivery_status = delivery_status  # Селект
        self.sold_out_status = sold_out_status  # Селект
        self.upload_images = upload_images      # Текстовое
        self.date_valid_form = date_valid_form  # Дата
        self.date_valid_to = date_valid_to      # Дата
        # Information
        self.manufacturer_id = manufacturer_id,
        self.supplier_id = supplier_id,
        self.keywords = keywords,
        self.short_description = short_description,
        self.description = description,
        # Data
        self.sku = sku,
        self.gtin = gtin,
        self.taric = taric,
        self.weight = weight,
        self.weight_class = weight_class,
        # self.width = width,
        # self.height = height,
        # self.length = length,
        self.dim_class = dim_class,
        # Prices
        self.purchase_price = purchase_price,
        self.purchase_price_currency_code = purchase_price_currency_code,
        self.tax_class_id = tax_class_id,
        self.pricesUSD = pricesUSD,
        self.gross_pricesUSD = gross_pricesUSD,
        self.pricesEUR = pricesEUR,
        self.gross_pricesEUR = gross_pricesEUR

    def __eq__(self, other):
        return self.status == other.status \
            and self.name == other.name \
            and self.code == other.code \
            and self.categories == other.categories \
            and self.default_category == other.default_category \
            and self.product_groups == other.product_groups \
            and self.quantity == other.quantity \
            and self.quantity_unit == other.quantity_unit \
            and self.delivery_status == other.delivery_status \
            and self.sold_out_status == other.sold_out_status \
            and self.upload_images == other.upload_images \
            and self.date_valid_form == other.date_valid_form \
            and self.date_valid_to == other.date_valid_to \
            and self.manufacturer_id == other.manufacturer_id \
            and self.supplier_id == other.supplier_id \
            and self.keywords == other.keywords \
            and self.short_description == other.short_description \
            and self.description == other.description\
            and self.sku == other.sku\
            and self.gtin == other.gtin \
            and self.taric == other.taric\
            and self.weight == other.weight \
            and self.weight_class == other.weight_class\
            and self.width == other.width\
            and self.height == other.height\
            and self.length == other.length\
            and self.dim_class == other.dim_class\
            and self.purchase_price == other.purchase_price\
            and self.purchase_price_currency_code == other.purchase_price_currency_code\
            and self.tax_class_id == other.tax_class_id \
            and self.pricesUSD == other.pricesUSD \
            and self.gross_pricesUSD == other.gross_pricesUSD \
            and self.pricesEUR == other.pricesEUR\
            and self.gross_pricesEUR == other.gross_pricesEUR

