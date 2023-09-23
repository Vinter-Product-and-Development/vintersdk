# Websocket Specific Usage

## Get Contributions for a Single Asset

Docs [VinterAPIWS][vintersdk.vinter_sdk_ws.VinterAPIWS]

```python
from vintersdk import VinterAPIWS

def on_message(ws, message):
    print(message)

    #ws.close() # Uncomment this line to close the websocket after receiving a message

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")
    print(f"close_status_code: {close_status_code} close_msg: {close_msg}")

def on_open(ws):
    print("### open ###")

vinter_ws = VinterAPIWS(
    symbol="btc-usd-p-r",
    token=APIKEY,
    asset_type="single_assets",
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
    on_open=on_open,
)
vinter_ws.open()
```