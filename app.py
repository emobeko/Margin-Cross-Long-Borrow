from flask import Flask, request
import json
from binance.spot import Spot as Client


app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():

    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        exchange = data['exchange']
        price = data['price']
        side = data['side']
        quantity = data['quantity']
        binanceApiKey = data['binanceApiKey']
        binanceSecretKey = data['binanceSecretKey']

        
        params = {
            "symbol": ticker,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
        }
        
        params2 = {
            "asset": "BTC",
            "amount": quantity,
        }

        params3 = {
            "asset": "BTC",
            "amount": quantity,
        }
        
        Client(binanceApiKey, binanceSecretKey).margin_borrow(**params2)
        Client(binanceApiKey, binanceSecretKey).new_margin_order(**params)
        Client(binanceApiKey, binanceSecretKey).margin_repay(**params3)



    except:
        pass
    return {
        "code": "success",
    }










