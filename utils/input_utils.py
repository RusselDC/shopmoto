import re

class InputUtils:
    
    def __init__(self):
        self.name_pattern = r'^[a-zA-Z ]*$'
        self.amount_pattern = r'^[0-9]*\.?[0-9]+$'
        self.string_pattern = r'^[a-zA-Z]*$'
        self.username_pattern = r'^[a-zA-Z0-9]*$'
        self.number_pattern = r'^\d+$'
        self.password_patten = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'

    
    def is_string(self, value):
        return isinstance(value, str)
        
    def is_username(self, value):
        return isinstance(value, str) and bool(re.match(self.username_pattern, value))
    
    def is_password(self, value):
        return isinstance(value, str) and bool(re.match(self.password_patten, value))
    
    def is_int(self, value):
        try:
            int(value)
            return bool(re.match(self.number_pattern, value))
        except:
            return False
    
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
        return len(str(value)) <= u_limit and len(str(value)) >= l_limit
    
    def is_shorter(self, value, limit):
        return len(str(value)) <= limit
    
    def is_length(self, value, limit):
        return len(str(value)) == limit
    
    def is_longer(self, value, limit):
        return len(str(value)) >= limit
    
    def is_same(self, value_1, value_2):
        return str(value_1) == str(value_2)
    
    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
