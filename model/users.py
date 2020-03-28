
class Users:
    def __init__(self,
                 tax_id=None,
                 company=None,
                 firstname=None,
                 lastname=None,
                 address1=None,
                 address2=None,
                 postcode=None,
                 city=None,
                 country_code=None,
                 zone_code=None,
                 email=None,
                 phone=None,
                 newsletter=None,
                 password=None,
                 confirmed_password=None
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

    def __eq__(self, other):
        return self.tax_id == other.tax_id \
               and self.confirmed_password == other.confirmed_password \
               and self.password == other.password \
               and self.newsletter==other.newsletter \
               and self.phone == other.phone \
               and self.email == other.email \
               and self.zone_code == other.zonecode \
               and self.country_code == other.country_code \
               and self.city == other.city \
               and self.postcode == other.postcode \
               and self.address1 == other.address1 \
               and self.address2 == other.address2 \
               and self.lastname == other.lastname \
               and self.company == other.company \
               and self.firstname == other.firstname

