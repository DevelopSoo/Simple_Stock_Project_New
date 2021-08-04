from typing import Optional

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/stocks", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# from pykrx import stock

# df = stock.get_market_ohlcv_by_ticker("20210122")
# print(df.head(1))

# for ticker in stock.get_market_ticker_list()[1:3]:
#         종목 = stock.get_market_ticker_name(ticker)
#         print(종목)
