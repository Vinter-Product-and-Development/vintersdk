import websocket
from .utils import VinterUrl, WsAssetType


class VinterAPIWS:
    def __init__(
        self,
        symbol: str,
        token: str,
        asset_type: WsAssetType,
        on_message: callable,
        on_error: callable,
        on_close: callable,
        on_open: callable,
    ):
        """
        This class is used to create a websocket connection to the Vinter API.

        Parameters
        ----------
        symbol : str
            The symbol of the asset you want to get data for.
        token : str
            The API token.
        asset_type : WsAssetType (str)
            The type of asset you want to get data for.
        on_message : callable
            Callback function for when a message is received.
        on_error : callable
            Callback function for when an error occurs.
        on_close : callable
            Callback function for when the connection is closed.
        on_open : callable
            Callback function for when the connection is opened.
        """
        self.ws = None
        self.symbol = symbol
        self.token = token
        self.asset_type = asset_type
        self.url = self.get_ws_url() + "/?token=" + self.token
        self.on_message = on_message
        self.on_error = on_error
        self.on_close = on_close
        self.on_open = on_open

    def get_ws_url(self):
        """It takes the asset type and symbol and returns the websocket url

        Returns
        -------
            The websocket url for the asset type and symbol.

        """
        return VinterUrl.websocket_url(self.asset_type, self.symbol)

    def open(self):
        """The function opens a websocket connection to the url specified in the constructor"""
        self.ws = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open,
        )
        self.ws.run_forever()

    def close(self):
        """The function closes the websocket connection"""
        self.ws.close()
