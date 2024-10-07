from business_layer.user_bll import UserBLL
from fastapi import FastAPI
from domain.register_inputs import Registerinputs
from domain.service_response import ServiceResponse


user_bll = UserBLL()
api = FastAPI()

@api.post("/register")
async def register_user(register_inputs : Registerinputs) -> ServiceResponse:
    inputs = dict(register_inputs)
    validation = user_bll.validate_inputs(inputs)
    
    if len(validation) != 0:
        return ServiceResponse(status="fail",status_code=414, data=str(validation), message="Input Validation Failure")
    
    user = user_bll.find_account(inputs.get("user_name"))

    if len(user) != 0:
        return ServiceResponse(status="fail", status_code=401, data='[]', message="Username already used")

    
    
    


