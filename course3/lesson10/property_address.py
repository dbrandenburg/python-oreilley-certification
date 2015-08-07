import re

class StateError(Exception):
    """Custom error for wrong state"""
    pass

class ZipCodeError(Exception):  
    """Custom error for wrong ZipCode"""
    pass

class Address:
    def __init__(self, name, street_address, city, state, zip_code):
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
            raise StateError("State doesn't match format LL")
        self._state = str(value)

    # Zip Code
    @property
    def zip_code(self):
        return self._zip_code
        
    @zip_code.setter    
    def zip_code(self, value):
        if not re.match('^\d{5}$',value):
            raise ZipCodeError("Zipcode doesn't match nnnnn")
        self._zip_code = value