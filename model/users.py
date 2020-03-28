
class Users:
    def __init__(self,
                 tax_id=None,
                 company = None,
                 firstname = None,
                 lastname = None,
                 address1 = None,
                 address2 = None,
                 postcode = None,
                 city = None,
                 country_code = None,
                 zone_code = None,
                 email = None,
                 phone = None,
                 newsletter = None,
                 password = None,
                 confirmed_password = None
                 ):
        self.tax_id = tax_id
        self.company = company,
        self.firstname = firstname,
        self.lastname = lastname,
        self.address1 = address1,
        self.address2 = address2,
        self.postcode = postcode,
        self.city = city,
        self.country_code = country_code,
        self.zone_code = zone_code,
        self.email = email,
        self.phone = phone,
        self.newsletter = newsletter,
        self.password = password,
        self.confirmed_password = confirmed_password
