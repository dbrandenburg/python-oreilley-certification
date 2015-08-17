import re
import logging
from optparse import OptionParser

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
logging.basicConfig(filename='property_address.log', level=logging.INFO,
                    format=LOG_FORMAT)

class StateError(Exception):
    """Custom error for wrong state"""
    pass

class ZipCodeError(Exception):  
    """Custom error for wrong ZipCode"""
    pass

class Address:
    def __init__(self, name, street_address, city, state, zip_code):
        logging.info('Creating a new address')
        self._name = name
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip_code = zip_code
        pass
        
    @property
    def name(self):
        return self._name
    
    # Street Address
    @property
    def street_address(self):
        return self._street_address
    
    @street_address.setter
    def street_address(self, value):
        self._street_address = value
    
    # City
    @property
    def city(self):
        return self._city
        
    @city.setter
    def city(self, value):
        self._city = value
    
    # State
    @property
    def state(self):
        return self._state
        
    @state.setter
    def state(self, value):
        if not re.match('^[A-Z]{2}$',value):
            logging.error('STATE exception')
            raise StateError("State doesn't match format LL")
        self._state = str(value)

    # Zip Code
    @property
    def zip_code(self):
        return self._zip_code
        

    @zip_code.setter    
    def zip_code(self, value):
        if not re.match('^\d{5}$',value):
            logging.error('ZIPCODE exception')
            raise ZipCodeError("Zipcode doesn't match nnnnn")
        self._zip_code = value

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-l", "--level", action="store", dest="level", default="info", help="INFO yes Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL")
    parser.add_option("-n", "--name", action="store", dest="name", help="Throws a parser error if empty yes Sets the name value of the Address object")
    parser.add_option("-a", "--address", action="store", dest="address", help="Throws a parser error if empty yes Sets the street_address value of the Address object")
    parser.add_option("-c", "--city", action="store", dest="city", help="Throws a parser error if empty yes Sets the city value of the Address object")
    parser.add_option("-s", "--state", action="store", dest="state", help="Throws a parser error if empty yes Sets the state value of the Address object")
    parser.add_option("-z","--zip_code", action="store", dest="zip_code", help="Throws a parser error if empty yes Sets the zip_code value of the Address object")
    (options, args) = parser.parse_args()
    if not options.name or not options.address or not options.city or not options.state or not options.zip_code:
        parser.error("property_address.py: error: options -n, -a, -c, -s, -z are required")
        parser.print_usage()
        exit(1)
    
    
    
    
    
    
    