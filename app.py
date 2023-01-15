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
            "isIsolated": "TRUE",
            "symbol": "BTCBUSD",
        }
        
        params2 = {
            "asset": "BTC",
            "amount": quantity,
            "isIsolated": "TRUE",
            "symbol": "BTCBUSD",
        }
        
        Client(binanceApiKey, binanceSecretKey).margin_borrow(**params2)
        Client(binanceApiKey, binanceSecretKey).new_margin_order(**params)
        Client(binanceApiKey, binanceSecretKey).margin_repay(**params2)



    except:
        pass
    return {
        "code": "success",
    }










