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
class Iban(object):
    '''New instance of iban-class'''

    def __init__(self, country_code, account_number, routing_number):
        self.country_code = country_code
        self.account_number = account_number
        self.routing_number = routing_number

    def gen_iban() -> str:
        if self.country_code == "DE":
            # I know there are many things that are equal here to other
            # countries. But I decided to only do DE for now.
            fill_to_ten = 10 - len(self.account_number)
            bban = str(self.routing_number) + \
                    (fill_to_ten * "0") + \
                    str(self.account_number)
            country_code_ascii = 1314
            checksum = 0
            my_iban = self.country_code + str(checksum) + bban
            return my_iban
        else:
            print("\nOther countries than 'DE' not yet working.")
            print("Feel free to contribute on GitHub.\n")