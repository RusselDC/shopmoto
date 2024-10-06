from data_layer.AbstractShopDao import AbstractShopDao

class UserDao:
    
    def __init__(self):
        self.__abstract_dao = AbstractShopDao()
        
    def register(self,user_id:str, user_name:str, user_email:str,user_contact:str,user_password:str) -> str:
        sql_stmt = "insert into users(user_id, user_name, user_email, user_contact, user_password) values (%s, %s, %s, %s, %s) returning *"
        sql_values = (user_id, user_name, user_email, user_contact, user_password)
        return self.__abstract_dao.write(sql_stmt, sql_values)
    
    def find_account(self, username):
        sql_stmt = "select * from users where user_name = %s"
        sql_value = (username,)
        return self.__abstract_dao.read_one(sql_stmt,sql_value)
    
    def deactivate_account(self, username):
        sql_stmt = "update users set is_active = False where user_name = %s returning *"
        sql_value = (username,)
        return self.__abstract_dao.write(sql_stmt, sql_value)

    def change_password(self, username, new_password):
        sql_stmt = "update users set user_password = %s where username = %s returning *"
        sql_values = (new_password, username)
        return self.__abstract_dao.write(sql_stmt, sql_values)
    
    def update_account(self,id, new_username, new_email, new_contact):
        sql_stmt = "update users set user_name = %s, user_email = %s, user_contact_number = %s, updated_at = current_timestamp where id = %s returning *"
        sql_values = (id, new_username, new_email, new_contact)
        return self.__abstract_dao.write(sql_stmt, sql_values)
    