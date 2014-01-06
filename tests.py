__author__ = "n3rdkeller.de"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "github@n3rdkeller.de"
__status__ = "Development"

# Because this is on GitHub, I am not going to publish my
# bank data here. Use your own.

from iban import Iban

# Iban(country_code, account_number, routing_number)
my_own_iban = Iban("DE", "123456789", "12345678")

print(my_own_iban.gen_iban())