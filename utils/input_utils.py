import re

class InputUtils:
    
    def __init__(self):
        self.name_pattern = r'^[a-zA-Z ]*$'
        self.number_pattern = r'^[0-9]*\.?[0-9]+$'
        
    def is_string(self, value):
        return isinstance(value, str)
    
    def is_float(self, value):
        try:
            float(value)
            return True
        except:
            return False

    def is_amount(self, value):
        return bool(re.match(self.number_pattern, value))
    
    def is_name(self, value):
        return bool(re.match(self.name_pattern, value))
    
    def is_not_shorter_and_longer_than(self, value, u_limit, l_limit):
        return str(value) <= u_limit and str(value) >= l_limit
    
    def is_shorter(self, value, limit):
        return value <= limit
    
    def is_longer(self, value, limit):
        return value >= limit
