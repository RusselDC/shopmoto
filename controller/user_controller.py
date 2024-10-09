from business_layer.user_bll import UserBLL


class UserController:
    
    def __init__(self):
        self.user_bll = UserBLL()
        
    def register(self,input_dict):
        return self.user_bll.register(input_dict)
    
    def find_account(self, value, column="user_name"):
        return self.user_bll.find_account(value, column)
    
    def validate_inputs(self, input_dict):
        return self.user_bll.validate_inputs(input_dict)
    
        
        
    