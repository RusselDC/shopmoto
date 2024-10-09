from controller.user_controller import UserController
from fastapi import FastAPI
from domain.register_inputs import Registerinputs
import json
from domain.service_response import ServiceResponse


user_controller = UserController()
api = FastAPI()

@api.post("/register")
async def register_user(register_inputs : Registerinputs) -> ServiceResponse:
    inputs = dict(register_inputs)
    validation = user_controller.validate_inputs(inputs)
    
    if len(validation) != 0:
        return ServiceResponse(status="fail",status_code=414, data=str(validation), message="Input Validation Failure")
    
    user = user_controller.find_account(inputs.get("user_name"))

    if len(user) != 0:
        return ServiceResponse(status="fail", status_code=401, data='[]', message="Username already used")
    
    email = user_controller.find_account(inputs.get("user_email"), "user_email")
    contact = user_controller.find_account(inputs.get("user_contact"),"user_contact_number")
    
    if len(email) != 0 or len(contact) != 0:
        return ServiceResponse(status="fail", status_code=201, data='[]', message="Email or contact number already used")
    
    return ServiceResponse(data=str(user_controller.register(inputs)), message="User has been registered")

    
    
    
    

    
    
    


