__author__ = "n3rdkeller.de"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "github@n3rdkeller.de"
__status__ = "Development"


# global variables
COUNTRIES = ("AD", "AT", "BE", "CH", "CY", "CZ", "DE", "DK", "EE", "ES", \
             "FI", "FR", "GB", "GI", "GR", "HU", "IE", "IS", "IT", "LT", \
             "LU", "LV", "NL", "NO", "PL", "SE", "SI", "SK")

##############
# class IBAN #
##############
class iban(object):
    '''New instance of iban-class'''

    def __init__(self, country_code, account_number, routing_number):
        self.country_code = country_code
        self.account_number = account_number
        self.routing_number = routing_number