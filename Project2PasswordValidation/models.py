from pydantic import BaseModel,field_validator

class PasswordValidation(BaseModel):
    pincode: str

    #pincode must be 6 digits long and only contain numbers
    @field_validator('pincode')
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode must be 6 digits long and only contain numbers.")
        return value



class LocationResponse(BaseModel):
    pincode: str
    city: str
    state: str



class BulkRequests(BaseModel):
    pincodes: list[str]

    @field_validator('pincodes')
    @classmethod
    def validate_pincodes(cls, value):
        for pincode in value:
            if len(pincode) != 6 or not pincode.isdigit():
                raise ValueError(f"Pincode '{pincode}' must be 6 digits long and only contain numbers.")
        return value    



class BulkResponse(BaseModel):
    status: str = "success"
    found: int
    not_found: int
    results: list[LocationResponse]
    missing: list[str]
