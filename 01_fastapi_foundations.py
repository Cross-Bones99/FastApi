from fastapi import FastAPI
from fastapi import Request

app=FastAPI(
    title="Dwizzy Order Service",
    description="This is a simple order service API built with FastAPI.",

    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@app.get("/")
def order():

    return {"message": "Welcome to the Dwizzy Order Service!","status": "API is running successfully."}



@app.get("/about")
def about():
    """Get information about the Dwizzy Order Service."""
    return {"message": "This is a simple order service API built with FastAPI.",
    "service": "Dwizzy Order Service", "version": "1.0.0", "status": "API is running successfully."}


@app.get("/order")
def get_order():
    """Get a sample order."""
    return {
        "order_id": 12345,
        "customer_name": "John Doe",
        "items": [
            {"item_id": 1, "item_name": "burger", "quantity": 2},
            {"item_id": 2, "item_name": "fries", "quantity": 1}
        ],
        "total_price": 49.99,
        "status": "Processing"
    }    


@app.get("/order/{order_id}")
def get_order_by_id(order_id: int):
    """Get order details by order ID."""
    return {
        "order_id": order_id,
        "customer_name": "John Doe",
        "items": [
            {"item_id": 1, "item_name": "burger", "quantity": 2},
            {"item_id": 2, "item_name": "fries", "quantity": 1}
        ],
        "total_price": 49.99,
        "status": "Processing"
    }


@app.get("/requests/request_info")
def get_request_info(request: Request):
    """Get information about the incoming request."""
    return {
        
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": dict(request.path_params),
        "query_params": dict(request.query_params)
        
    }


# customizing the OpenAPI documentation with tags, summary, and description for the /orders endpoint
@app.get("/orders", tags=["Orders"],
         summary="Get a list of active orders",
         description="This endpoint returns a list of active orders in the system.")

def get_active_orders():
    """Get a list of active orders."""
    return [
        {
            "order_id": 1,
            "customer_name": "Alice",
            "item": "Pizza",
        },

        {
            "order_id": 2,
            "customer_name": "Bob",
            "item": "Burger",
        }
    ]    