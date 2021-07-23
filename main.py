from typing import Optional
from fastapi import FastAPI
from scrape import get_list_of_ads
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_ads/{city}/{min_price}/{max_price}")
def get_ads(city: str, min_price: str, max_price: str):
    data = get_list_of_ads(city, min_price, max_price)
    return data