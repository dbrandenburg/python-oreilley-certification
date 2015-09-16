#!/usr/bin/env python3

import re
import os
import logging
from optparse import OptionParser
import configparser

config = configparser.RawConfigParser()
config_filename = os.path.join(os.path.dirname(__file__), 'property_address.cfg')
config.read(config_filename)

try:
    LOG_FORMAT = config.get('log', 'format')
    LOG_OUTPUT = config.get('log', 'output')
    ZIP_CODE_VALIDATOR = config.get('validators','zip_code')
    STATE_VALIDATOR = config.get('validators','state')
except:
    LOG_OUTPUT = 'property_address.log'
    pass


def start_logging(loglevel='INFO'):
    # Log defaults
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
    LEVELS = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO,
          'WARNING': logging.WARNING, 'ERROR': logging.ERROR,
          'CRITICAL' : logging.CRITICAL}

    output =  os.path.join(os.path.dirname(__file__), LOG_OUTPUT)
    logging.basicConfig(filename=output, level=LEVELS[loglevel], format=LOG_FORMAT)

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
        self.state = state
        self.zip_code = zip_code
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
        try:
            state_validator = STATE_VALIDATOR
        except:
            state_validator = '^[A-Z]{2}$'
        if not re.match(state_validator,value):
            logging.error('STATE exception')
            raise StateError("State doesn't match format LL")
        self._state = str(value)

    # Zip Code
    @property
    def zip_code(self):
        return self._zip_code


    @zip_code.setter
    def zip_code(self, value):
        try:
            zipcode_validator = ZIP_CODE_VALIDATOR
        except:
            zipcode_validator = '^\d{5}$'
        if not re.match(zipcode_validator,value):
            logging.error('ZIPCODE exception')
            raise ZipCodeError("Zipcode doesn't match")
        self._zip_code = value

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-l", "--level", action="store", dest="level", default="INFO", help="INFO yes Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL")
    parser.add_option("-n", "--name", action="store", dest="name", help="Throws a parser error if empty yes Sets the name value of the Address object")
    parser.add_option("-a", "--address", action="store", dest="address", help="Throws a parser error if empty yes Sets the street_address value of the Address object")
    parser.add_option("-c", "--city", action="store", dest="city", help="Throws a parser error if empty yes Sets the city value of the Address object")
    parser.add_option("-s", "--state", action="store", dest="state", help="Throws a parser error if empty yes Sets the state value of the Address object")
    parser.add_option("-z","--zip_code", action="store", dest="zip_code", help="Throws a parser error if empty yes Sets the zip_code value of the Address object")
    (options, args) = parser.parse_args()

    start_logging(loglevel=options.level)

    if not options.name or not options.address or not options.city or not options.state or not options.zip_code:
        parser.error("property_address.py: error: options -n, -a, -c, -s, -z are required")
        parser.print_usage()
        exit(1)
    try:
        home = Address(name=options.name, street_address=options.address, city=options.city,
        state=options.state,zip_code=options.zip_code)
        home.zip_code = options.zip_code
        home.state = options.state
    except StateError:
        parser.error("option -s requires a valid state")
    except ZipCodeError:
        parser.error("option -z requires a valid zip code")
