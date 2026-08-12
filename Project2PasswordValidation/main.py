from fastapi import FastAPI, HTTPException
from exception import PinCodeNotFoundError, InvalidPinCodeError, pin_code_not_found_exception_handler, invalid_pin_code_exception_handler
from models import PasswordValidation, LocationResponse, BulkRequests, BulkResponse
from data import pincode_db

app = FastAPI(
    title="Password Validation Service",
    description="This is a simple password validation service API built with FastAPI.",
    version="1.0.0",
)

# Register custom exception handlers
app.add_exception_handler(PinCodeNotFoundError, pin_code_not_found_exception_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pin_code_exception_handler)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Password Validation Service!",
    }


@app.get("/pincode/{pincode}", response_model=LocationResponse)
def get_location_by_pincode(pincode:str):
    """Get location details by pin code."""
    if not pincode.isdigit() or len(pincode) != 6:
        raise InvalidPinCodeError(pincode, "Pin code must be a 6-digit number.")
    
    location = pincode_db.get(pincode)
    if not location:
        raise PinCodeNotFoundError(pincode)
    
    return LocationResponse(pincode=pincode, city=location["city"], state=location["state"])


@app.post("/pincode/bulk", response_model=BulkResponse)
def  get_bulk_pincodes(request: BulkRequests):

    results=[]
    missing=[]
    for code in request.pincodes:
        if code in pincode_db:
            results.append(pincode_db[code])
        else:
            missing.append(code)

    return BulkResponse(
        found=len(results),
        not_found=len(missing),
        results=results,
        missing=missing

    )            

