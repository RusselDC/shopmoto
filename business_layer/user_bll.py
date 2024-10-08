from data_layer.UserDao import UserDao
from datetime import datetime
from utils.input_utils import InputUtils
import bcrypt
import random
import bcrypt

class UserBLL:
    
    def __init__(self):
        self.user_dao = UserDao()
        self.input_utils = InputUtils()
        
    def register(self,input_dict) -> str:
        result = self.user_dao.register(self.get_user_id(),input_dict.get("user_name"), input_dict.get("user_email"), input_dict.get("user_contact"), self.hash_password(input_dict.get("user_password")))
        return {"username": result[2],"email":result[3]}
    
    def get_user_id(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y%m%d%S')
        return f"USR_{formatted_time}{random.randint(1 ,99)}"
    
    def hash_password(self, password:str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def check_password(self, password:str, hashed_password:str) -> str:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    
    def find_account(self, value, column="user_name"):
        return self.user_dao.find_account(value, column)

    def validate_inputs(self, input_dict):
        validate_arr = []
        if not self.input_utils.is_username(input_dict.get("user_name")):
            validate_arr.append({"username":"Invalid Username. Ex: juandc189"})
        if not self.input_utils.is_int(input_dict.get("user_contact")) or not self.input_utils.is_length(input_dict.get("user_contact"), 10):
            validate_arr.append({"contact":"Invalid Contact. Ex: 9876543210"})
        if not self.input_utils.is_password(input_dict.get("user_password")) or self.input_utils.is_password("password_confirmation"):
            validate_arr.append({"password":"Password Invalid. Ex:Juandc189@"})
        if not self.input_utils.is_same(input_dict.get("user_password"), input_dict.get("password_confirmation")):
            validate_arr.append({"password":"Passwords are not matching"})
        if not self.input_utils.is_valid_email(input_dict.get("user_email")):
            validate_arr.append({"email":"Invalid Email. Ex: juandc189@gmail.com"})
            
        return validate_arr
    

    
    

