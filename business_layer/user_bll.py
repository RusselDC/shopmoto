from data_layer.UserDao import UserDao
from datetime import datetime
import bcrypt
import random

class UserBLL:
    
    def __init__(self):
        self.user_dao = UserDao()
        
    def register(self, username, user_password, user_email,user_contact) -> str:
        return self.user_dao.register(self.get_user_id(),username, user_email, user_contact, self.hash_password(user_password))
    
    def get_user_id(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y%m%d%S')
        return f"USR_{formatted_time}{random.randitnt(1 ,99)}"
    
    def hash_password(self, password:str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def check_password(self, password:str, hashed_password:str) -> str:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    
    def find_account(self, username):
        return self.user_dao.find_account(username)