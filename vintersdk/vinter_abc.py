from abc import ABC, abstractmethod
from typing import Union


class VinterAPIABC(ABC):
    @abstractmethod
    def __init__(self, api_key: str, asset_type: str):  # pragma: no cover
        """This function takes in an api_key and asset_type and sets them as attributes of the class

        Parameters
        ----------
        api_key : str
            Your API key.
        asset_type : AssetType (str)
            The type of asset you want to get data for.
            The acceptable asset types listed in the AssetType enum.
        """
        pass

    @abstractmethod
    def get_all_active_data(
        self, frequency: str = None, symbol_only: bool = False
    ) -> Union[list, dict]:  # pragma: no cover
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
        pass

    @abstractmethod
    def get_latest_data(
        self, symbol: str, limit: int = 1
    ) -> dict:  # pragma: no cover
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
        pass

    @abstractmethod
    def get_latest_value(self, symbol: str) -> float:  # pragma: no cover
        """This function takes in a symbol and returns the latest value for that symbol

        Parameters
        ----------
        symbol : str
            The symbol of the asset you want to get data for.

        Returns
        -------
            The latest value for the symbol

        """
        pass

    @abstractmethod
    def _filter_by_symbol(
        self, data: list, symbol: str
    ) -> list:  # pragma: no cover
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
        pass

    @abstractmethod
    def get_active_data(self, symbol: str) -> dict:  # pragma: no cover
        """This function returns the data for the active asset

        Parameters
        ----------
        symbol : str
            The symbol of the asset you want to get data for.

        Returns
        -------
            A dictionary of the data for the active asset

        """
        pass

    @abstractmethod
    def get_multi_current_rebalance_weight(
        self, symbol: str
    ) -> dict:  # pragma: no cover
        """This function returns the current rebalance weight of multi_assets symbol

        Returns
        -------
            Weight of the current rebalance of the multi_assets symbol

            OR

            ValueError if the symbol is not a present in the
            list of active symbols for asset_type multi_assets

        """
        pass

    @abstractmethod
    def get_single_contributions(
        self, symbol: str
    ) -> dict:  # pragma: no cover
        """This function returns the contributions of the single_assets symbol

        Returns
        -------
            A dictionary of the contributions of the single_assets symbol

            OR

            ValueError if the symbol is not a present in the
            list of active symbols for asset_type single_assets

        """
        pass

    @abstractmethod
    def get_multi_previous_rebalance_date(
        self, symbol: str
    ) -> Union[str, None]:  # pragma: no cover
        """This function returns the previous rebalance date of multi_assets symbol

        Returns
        -------
            Date of the previous rebalance of the multi_assets symbol

            OR

            ValueError if the symbol is not a present in the
            list of active symbols for asset_type multi_assets

            OR

            None if the symbol Rebalance is not scheduled

        """
        pass

    @abstractmethod
    def get_multi_previous_review_date(
        self, symbol: str
    ) -> Union[str, None]:  # pragma: no cover
        """This function returns the previous review date of multi_assets symbol

        Returns
        -------
            Date of the previous review of the multi_assets symbol

            OR

            ValueError if the symbol is not a present in the
            list of active symbols for asset_type multi_assets

            OR

            None if the symbol Review is not scheduled

        """
        pass

    @abstractmethod
    def get_multi_next_review_date(
        self, symbol: str
    ) -> Union[str, None]:  # pragma: no cover
        """This function returns the next review date of multi_assets symbol

        Returns
        -------
            Date of the next review of the multi_assets symbol

            OR

            ValueError if the symbol is not a present in the
            list of active symbols for asset_type multi_assets

            OR

            None if the symbol Review is not scheduled

        """
        pass

    @abstractmethod
    def get_multi_next_rebalance_date(
        self, symbol: str
    ) -> Union[str, None]:  # pragma: no cover
        """This function returns the next rebalance date of multi_assets symbol

        Returns
        -------
            Date of the next rebalance of the multi_assets symbol

            OR

            ValueError if the symbol is not a present in the
            list of active symbols for asset_type multi_assets

            OR

            None if the symbol Rebalance is not scheduled

        """
        pass

    @abstractmethod
    def get_multi_next_rebalance_weight(
        self, symbol: str
    ) -> Union[str, None]:  # pragma: no cover
        """This function returns the next rebalance weight of multi_assets symbol

        Returns
        -------
            Weight of the next rebalance of the multi_assets symbol

            OR

            ValueError if the symbol is not a present in the
            list of active symbols for asset_type multi_assets

            OR

            None if the symbol Rebalance is not present in the payload

        """
        pass

    @abstractmethod
    def get_data_by_date(
        self, symbol: str, date: Union[str, list]
    ) -> dict:  # pragma: no cover
        """This function takes in a symbol and a date and returns a dictionary of the data for that date

        This function is only for daily data.

        Parameters
        ----------
        symbol : str
            The symbol of the asset you want to get data for.
        date : str | list
            The date of the data you want to get. format: YYYY-MM-DD

        Returns
        -------
            A dictionary of the data

        """
        pass

    @abstractmethod
    def get_data_by_range(
        self, symbol: str, start: str, end: str = None, limit: int = 1000
    ) -> dict:  # pragma: no cover
        """This function takes in a symbol and a start and end date and returns a dictionary of the data
        for that period

        Parameters
        ----------
        symbol : str
            The symbol of the asset you want to get data for.
        start : str
            The start datatime . format: YYYY-MM-DDTHH:MM:SSZ or YYYY-MM-DDTHH:MM:SS.sssZ
        end : str
            The end datatime. format: YYYY-MM-DDTHH:MM:SSZ or YYYY-MM-DDTHH:MM:SS.sssZ

        Returns
        -------
            A dictionary of the data

        """
        pass
