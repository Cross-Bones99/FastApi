from fastapi import FastAPI


app=FastAPI()

@app.get("/")
def home():
    return{
        "message":"Learning FastAPI is fun!"
    }


# dynamic path parameter
# http://127.0.0.1:8000/users/1
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }



# query parameter
# http://127.0.0.1:8000/products?category=laptop
@app.get("/products")
def get_products(category: str):
    return {
        "category": category
    }


# query parameter with multiple parameters
@app.get("/products")
def get_products(category: str, page: int):
    return {
        "category": category,
        "page": page
    }



@app.post("/chat")
def chat():
    return {
        "message": "This is a chat endpoint"
    }