from vintersdk import VinterAPIWS


def test_validate_class():
    """This function tests the classes in the vinter_validation.py and vinter_url.py files"""

    def on_message(ws, message):
        pass

    def on_error(ws, error):
        pass

    def on_close(ws, close_status_code, close_msg):
        pass

    def on_open(ws):
        pass

    vinter_api_ws = VinterAPIWS(
        symbol="btc-usd-p-d",
        token="",
        asset_type="multi_assets",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open,
    )
    assert vinter_api_ws is not None
    vinter_api_ws.open()
    vinter_api_ws.close()
