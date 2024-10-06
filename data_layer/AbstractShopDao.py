from abc import ABC
import json
import psycopg2
from utils.file_utils import FileUtils

class AbstractShopDao(ABC, FileUtils):
    
    def __init__(self):
        self.__db_cred = self.read_string_from_file()
    
    def read_string_from_file(self):
        return json.loads(self.read_file())
    
    def db_connect(self):
        return psycopg2.connect(database=self.__db_cred.get("database"),user=self.__db_cred.get("username"),password=self.__db_cred.get("password"),port=self.__db_cred.get("port"),host=self.__db_cred.get("host"))
    
    def read(self,sql_statement, sql_values):
        
        try:
            conn = self.db_connect()
            cursor = conn.cursor()
        
            cursor.execute(sql_statement, sql_values)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
        
            return result
        except psycopg2.OperationalError as e:
            return f"Operational Error: {e}"
        
    def read_one(self, sql_statement, sql_values):
        try:
            conn = self.db_connect()
            cursor = conn.cursor()
            
            cursor.execute(sql_statement, sql_values)
            result =  cursor.fetchall()
            
            cursor.close()
            conn.close()
            
            return result
        except psycopg2.OperationalError as e:
            return e
           
        
    def write(self, sql_statement, sql_values):
        try:
            conn = self.db_connect()
            cursor = conn.cursor()
            conn.autocommit = False
            cursor.execute(sql_statement, sql_values)
            row = cursor.fetchone()
            
            if row:
                conn.commit()
                return row
            else:
                conn.rollback()
                return "No row has been written"
            
        except psycopg2.OperationalError as e:
            conn.rollback()
            return e
        finally:
            cursor.close()
            conn.close()
            
            
        
    
    
    


    
    

