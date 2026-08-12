from fastapi.responses import JSONResponse
from fastapi import Request

# Custon exception class

class PinCodeNotFoundError(Exception):
    def __init__(self, pin_code: str):
        self.pin_code = pin_code


class InvalidPinCodeError(Exception):
    def __init__(self,pincode:str,reason:str = "Invalid pin code format"):
        self.pincode=pincode
        self.reason=reason


#Exception handler for Exception classes

async def pin_code_not_found_exception_handler(request: Request, exc: PinCodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message":f"pin code '{exc.pin_code}' does not exist in the database."},
        pincode=exc.pin_code
    )


async def invalid_pin_code_exception_handler(request: Request, exc: InvalidPinCodeError):
    return JSONResponse(
        status_code=400,
        content={"message":f"Invalid pin code '{exc.pincode}': {exc.reason}"},
        pincode=exc.pincode
    )