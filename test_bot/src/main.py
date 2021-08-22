import websocket, json, pprint, talib, numpy, config, binance
from binance.enums import *

RSI_PERIOD = 14
OVERSOLD_THRESHOLD = 30
OVERBOUGHT_THRESHOLD = 70
TRADE_QUANTITY = 100
TRADE_SYMBLE = 'VETUSDT'
SOCKET = "wss://stream.binance.com:9443/ws/vetusdt@kline_1m"

closes = []
in_position = False
client = binance.Client(config.get_api_key(), config.get_api_secret(), tld="com")

def order(quantity, symbol, side, order_type):
    try:
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print("Order info")
        print(order)
    except Exception as e:
        print("There was a problem ordering - {}".format(e))
        return False
    
    return True

def on_open(ws):
    print("Connection to {} opened".format(SOCKET))

def on_message(ws, message):
    global closes, in_position

    message = json.loads(message)
    pprint.pprint(message)
    candle = message['k']
    timestamp = candle['t']
    candle_is_closed = candle['x']

    if candle_is_closed:
        closes.append(float(candle['c']))
        num_closes = len(closes)

        print(closes)

        if num_closes > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, timeperiod=RSI_PERIOD)
            print(rsi)
            last_rsi = rsi[-1]
            print("RSI is {}".format(last_rsi))
            if last_rsi > OVERBOUGHT_THRESHOLD:
                print("RSI shows that market is overbought")
                if in_position:
                    print("Bot going to close position")
                    order_result = order(TRADE_QUANTITY, TRADE_SYMBLE, SIDE_SELL, ORDER_TYPE_MARKET)
                    if order_result:
                        in_position = False
                else:
                    print("Nothing to do")
            if last_rsi < OVERBOUGHT_THRESHOLD:
                print("It is oversold")
                if in_position:
                    print("You are already in the position [SELL]")
                else:
                    print("Bot going to open position [BUY]")
                    order_succeeded = order(TRADE_QUANTITY, TRADE_SYMBLE, SIDE_BUY, ORDER_TYPE_MARKET)
                    if order_result:
                        in_position = True

def on_close(ws):
    print("Connection to {} closed".format(SOCKET))

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()


def main():

    print('Ready!')

    return 0

main()