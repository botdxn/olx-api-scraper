from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from scrape import get_list_of_ads

app = FastAPI()

@app.get("/")
def read_root():
    html_content = """
    <html>
        <head>
            <title>OLX Rent Ads API</title>
        </head>
        <body>
            <h1>Usage:</h1>
            <h3>/ads/city/min_price/max_price</h3>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/ads/{city}/{min_price}/{max_price}")
def get_ads(city: str, min_price: str, max_price: str):
    data = get_list_of_ads(city, min_price, max_price)
    return data
