import os
import httpx
from typing import Union
from datetime import datetime, timedelta
from .config import Frequency, AssetType
from .utils import VinterValidation, VinterUrl, handle_response
from .vinter_abc import VinterAPIABC

APIKEY = os.environ.get("VINTER_API_KEY", None)


class VinterAPI(VinterAPIABC):
    def __init__(self, api_key: str, asset_type: AssetType):
        """This function takes in an api_key and asset_type and sets them as attributes of the class

        Parameters
        ----------
        api_key : str
            Your API key.
        asset_type : AssetType (str)
            The type of asset you want to get data for.
            The acceptable asset types listed in the AssetType enum.
        """
        self.api_key = api_key
        self.asset_type = asset_type
        self.frequencies = [frequency.value for frequency in Frequency]
        self.valid_asset_types = [asset_type.value for asset_type in AssetType]
        VinterValidation.validate_asset_type(self.asset_type)
        VinterValidation.validate_api_key(self.api_key)
        self.httpx_client = httpx.Client(follow_redirects=True, timeout=10)
        self.headers = {
            "Authorization": self.api_key,
            "Service-Type": "vintersdk",
        }

    def get_all_active_data(
        self, frequency: Frequency = None, symbol_only: bool = False
    ) -> Union[list, dict]:
        """
        This function returns a list of all the active symbols for the asset type

        Parameters
        ----------
        frequency : Frequency (str), optional
            The frequency of the asset you want to get data for., by default None
        symbol_only : bool, optional
            If True, it returns a list of symbols only, by default False

        Returns
        -------
        Union[list, dict]
            A list of data for the active symbols for the asset type
        """
        url = VinterUrl.get_active_url(self.asset_type)
        headers = self.headers
        response = self.httpx_client.get(url, headers=headers)

        handle_response(response)

        data = response.json()["data"]

        if frequency is not None:
            VinterValidation.validate_frequency(frequency)

            data = [
                asset
                for asset in data
                if asset["symbol"].split("-")[-1] == frequency
            ]

        if symbol_only:
            data = [asset["symbol"] for asset in data]

        return data

    def get_latest_data(self, symbol: str, limit: int = 1) -> dict:
        """It takes a symbol and a limit as parameters, and returns a dictionary of the latest data for
        that symbol

        Parameters
        ----------
        symbol : str
            The symbol of the asset you want to get data for.
        limit : int
            The number of data points to return.

        Returns
        -------
            A dictionary of the latest data for the symbol and limit.

        """
        url = VinterUrl.get_url_by_symbol(self.asset_type, symbol)

        params = {"symbol": symbol, "limit": limit}
        headers = self.headers
        response = self.httpx_client.get(url, params=params, headers=headers)

        handle_response(response)

        data = response.json()["data"]

        if len(data) == 0:
            raise ValueError(
                "No data was found for the symbol: {}".format(symbol)
            )

        return data

    def get_latest_value(self, symbol: str) -> float:
        """This function takes in a symbol and returns the latest value for that symbol

        Parameters
        ----------
        symbol : str
            The symbol of the asset you want to get data for.

        Returns
        -------
            The latest value for the symbol

        """
        data = self.get_latest_data(symbol=symbol)
        return data[0]["value"]

    def _filter_by_symbol(self, data: list, symbol: str) -> list:
        """This function takes in a list of data and a symbol and returns a list of data for that symbol

        Parameters
        ----------
        data : list
            A list of data
        symbol : str
            The symbol of the asset you want to get data for.

        Returns
        -------
            A list of data for the symbol

        """
        return [asset for asset in data if asset["symbol"] == symbol]

    def get_active_data(self, symbol: str) -> dict:
        """This function returns the data for the active asset

        Parameters
        ----------
        symbol : str
            The symbol of the asset you want to get data for.

        Returns
        -------
            A dictionary of the data for the active asset

        Raises
        ------
            ValueError
                If the symbol is not a present in the list of active symbols for the asset type

        """

        symbol, frequency = VinterValidation.validate_symbol_frequency(symbol)

        url = VinterUrl.get_active_url(self.asset_type)
        headers = self.headers
        parameters = {"symbol": symbol}
        response = self.httpx_client.get(
            url, headers=headers, params=parameters
        )

        handle_response(response)

        data = response.json()["data"]

        if len(data) == 0:
            raise ValueError(
                "No data was found for the symbol: {}".format(symbol)
            )

        return data[0]

    def get_multi_current_rebalance_weight(self, symbol: str) -> dict:
        """
        This function returns the current rebalance weight of multi_assets symbol

        Requires the asset_type to be multi_assets

        Returns
        -------
            Weight of the current rebalance of the multi_assets symbol

        Raises
        ------
            ValueError
                If the symbol is not a present in the list of active symbols for asset_type multi_assets

        """

        if self.asset_type != AssetType.MULTI_ASSET.value:
            raise ValueError(
                f"The asset type must be {AssetType.MULTI_ASSET.value} to use this function"
            )

        output = ""

        data = self.get_active_data(symbol=symbol)

        output = data.get("weights", None)

        if output is None or output == "":
            raise ValueError(
                "No data was found for the symbol: {}".format(symbol)
            )

        return output

    def get_single_contributions(self, symbol: str) -> dict:
        """This function returns the contributions of the single_assets symbol

        Returns
        -------
            A dictionary of the contributions of the single_assets symbol

        Raises
        ------
            ValueError
                If the symbol is not a present in the list of active symbols for asset_type single_assets

        """

        if self.asset_type != AssetType.SINGLE_ASSET.value:
            raise ValueError(
                f"The asset type must be {AssetType.SINGLE_ASSET.value} to use this function"
            )

        output = ""

        data = self.get_active_data(symbol=symbol)

        output = data.get("contrib", None)

        if output == "" or output is None:
            raise ValueError(
                f"The symbol {symbol} does not have any contributions associated with it."
            )

        return output

    def get_multi_previous_rebalance_date(
        self, symbol: str
    ) -> Union[str, None]:
        """This function returns the previous rebalance date of multi_assets symbol

        Returns
        -------
            Date of the previous rebalance of the multi_assets symbol

            OR

            None if the symbol Rebalance is not present in the payload

        Raises
        ------
            ValueError
                If the symbol is not a present in the list of active symbols for asset_type multi_assets

        """

        if self.asset_type != AssetType.MULTI_ASSET.value:
            raise ValueError(
                f"The asset type must be {AssetType.MULTI_ASSET.value} to use this function"
            )

        output = ""

        data = self.get_active_data(symbol=symbol)

        output = data.get("previous_rebalance_date", None)

        return output

    def get_multi_previous_review_date(self, symbol: str) -> Union[str, None]:
        """This function returns the previous review date of multi_assets symbol

        Returns
        -------
            Date of the previous review of the multi_assets symbol

            OR

            None if the symbol Review is not present in the payload

        Raises
        ------
            ValueError
                If the symbol is not a present in the list of active symbols for asset_type multi_assets

        """

        if self.asset_type != AssetType.MULTI_ASSET.value:
            raise ValueError(
                f"The asset type must be {AssetType.MULTI_ASSET.value} to use this function"
            )

        output = ""

        data = self.get_active_data(symbol=symbol)

        output = data.get("previous_review_date", None)

        return output

    def get_multi_next_review_date(self, symbol: str) -> Union[str, None]:
        """This function returns the next review date of multi_assets symbol

        Returns
        -------
            Date of the next review of the multi_assets symbol

            OR

            None if the symbol Review is not scheduled

        Raises
        ------
            ValueError
                If the symbol is not a present in the list of active symbols for asset_type multi_assets

        """

        if self.asset_type != AssetType.MULTI_ASSET.value:
            raise ValueError(
                f"The asset type must be {AssetType.MULTI_ASSET.value} to use this function"
            )

        output = ""

        data = self.get_active_data(symbol=symbol)

        output = data.get("next_review_date", None)

        return output

    def get_multi_next_rebalance_date(self, symbol: str) -> Union[str, None]:
        """This function returns the next rebalance date of multi_assets symbol

        Returns
        -------
            Date of the next rebalance of the multi_assets symbol

            OR

            None if the symbol Rebalance is not scheduled

        Raises
        ------
            ValueError
                If the symbol is not a present in the list of active symbols for asset_type multi_assets

        """

        if self.asset_type != AssetType.MULTI_ASSET.value:
            raise ValueError(
                f"The asset type must be {AssetType.MULTI_ASSET.value} to use this function"
            )

        output = ""

        data = self.get_active_data(symbol=symbol)

        output = data.get("next_rebalance_date", None)

        return output

    def get_multi_next_rebalance_weight(self, symbol: str) -> Union[str, None]:
        """This function returns the next rebalance weight of multi_assets symbol

        Returns
        -------
            Weight of the next rebalance of the multi_assets symbol

            OR

            None if the symbol Rebalance is not present in the payload

        Raises
        ------
            ValueError
                If the symbol is not a present in the list of active symbols for asset_type multi_assets

        """

        if self.asset_type != AssetType.MULTI_ASSET.value:
            raise ValueError(
                f"The asset type must be {AssetType.MULTI_ASSET.value} to use this function"
            )

        output = ""

        data = self.get_active_data(symbol=symbol)

        output = data.get("next_rebalance_weights", None)

        return output

    def get_data_by_date(self, symbol: str, date: str) -> dict:
        """This function takes in a symbol and a date and returns a dictionary of the data for that date

        Parameters
        ----------
        symbol : str
            The symbol of the asset you want to get data for.
        date : str
            The date of the data you want to get. format: YYYY-MM-DD

        Returns
        -------
            A dictionary of the data

        """
        symbol, frequency = VinterValidation.validate_symbol_frequency(symbol)

        if isinstance(date, str):
            dates = [date]

        # Validate Dates with regex pattern & Date validation
        VinterValidation.validate_dates(dates)

        start_date, last_date = dates[0], dates[-1]

        # Adding 1 day to the last date to get the data for the last date
        last_date = datetime.strptime(last_date, "%Y-%m-%d") + timedelta(
            days=1
        )

        # Converting the datetime object to string
        last_date = last_date.strftime("%Y-%m-%d")

        data = self.get_data_by_range(
            symbol=symbol, start=start_date, end=last_date
        )

        return data

    def get_data_by_range(
        self, symbol: str, start: str, end: str = None, limit: int = 1000
    ) -> dict:
        """This function takes in a symbol and a start and end date and returns a dictionary of the data
        for that period

        Parameters
        ----------
        symbol : str
            The symbol of the asset you want to get data for.
        start : str
            The start datatime . format:

                - YYYY-MM-DD

                - YYYY-MM-DDTHH:MM:SSZ

                - YYYY-MM-DDTHH:MM:SS.fffZ
        end : str
            The end datatime. format:

                - YYYY-MM-DD

                - YYYY-MM-DDTHH:MM:SSZ

                - YYYY-MM-DDTHH:MM:SS.fffZ
        limit : int
            The number of data points to return.

        Returns
        -------
            A dictionary of the data


        """
        url = VinterUrl.get_url_by_symbol(
            asset_type=self.asset_type, symbol=symbol
        )

        params = {
            "symbol": symbol,
            "start_time": start,
            "end_time": end,
            "limit": limit,
        }
        headers = self.headers
        response = self.httpx_client.get(url, params=params, headers=headers)

        handle_response(response)

        data = response.json()["data"]

        if len(data) == 0:
            raise ValueError(
                f"No data was found for the symbol: {symbol} between {start} and {end}."
            )

        return data
