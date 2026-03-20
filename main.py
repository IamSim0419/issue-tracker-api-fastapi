from fastapi import FastAPI

# Run promptly with: fastapi dev main.py
app = FastAPI()

items = [
    {"id": 1, "Mio": "Item 1"},
    {"id": 2, "Suzu": "Item 2"},
    {"id": 3, "Mina": "Item 3"},
]

@app.get("/health")
def health_check():
    return {"status": "Ok!"}

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

