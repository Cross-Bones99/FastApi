from fastapi import FastAPI,Query,HTTPException
from models import MenuItem,MenuResponse
from data import menu_items

app=FastAPI(
    title="Chai Menu Service",
    description="This is a simple chai menu service API built with FastAPI.",
)

@app.get("/")
def menu():
    return {"message": "Welcome to the Chai Menu Service!","status": "API is running successfully."}


@app.get("/menu",response_model=MenuResponse)
def get_menu(category:str |None =Query(None,description="Filter menu items by category (tea, coffee, snack)")):
    """Get the menu items. Optionally filter by category."""
    if category:
        filtered_items=[item for item in menu_items if item["category"].lower()==category.lower()]
        if not filtered_items:
            raise HTTPException(status_code=404,detail=f"No menu items found for category '{category}'")
        return MenuResponse(count=len(filtered_items),items=filtered_items)

    return MenuResponse(count=len(menu_items),items=menu_items)



@app.get("/menu/{item_id}",response_model=MenuItem)
def get_menu_item(item_id:int):
    """Get a specific menu item by its ID."""
    for item in menu_items:
        if item["id"]==item_id:
            return item
    raise HTTPException(status_code=404,detail=f"Menu item with ID '{item_id}' not found")