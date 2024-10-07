from pydantic import BaseModel, Field

class Registerinputs(BaseModel):
    user_name:str = Field(description="username for your account", default="Juandc189", max_length=16, min_length=8)
    user_password: str = Field(description="password for youra ccount", default="Juandc189@", max_length=16, min_length=8)
    password_confirmation: str = Field(description="password confirmation", default="Juandc189@", max_length=16, min_length=8)
    user_email: str = Field(description="Email for your account recovery and confirmation", default="Juandc189@gmail.com", max_length=50, min_length=8)
    user_contact:str = Field(description="Phone number for your account recover or confirmation", default="9876543210", max_length=10, min_length=10)
    
    