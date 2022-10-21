from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    """
    this class Item represent

    """
    id: str
    title: str
    description: str


app = FastAPI()

items = {
    "465464687684": Item(id="465464687684", title="item 1", description="description of iteù 1"),
    "465464687685": Item(id="465464687685", title="item 1", description="description of iteù 1")
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/items')
async def list_items():
    print(items.values())
    return list(items.values())


@app.post('/items')
async def create(item: Item):
    items[item.id] = item
    return item

