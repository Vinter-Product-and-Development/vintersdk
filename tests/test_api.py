import pytest
import httpx
from vintersdk import VinterAPI
from unittest.mock import patch, Mock


def test_get_all_active_data_async_returns_list():
    """
    Test that get_all_active_data returns a list of dicts
    """
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
            {"symbol": "ton-usdt-p-5-d", "contrib": ["ton-usdt-p-r"]},
        ],
        "params": {},
    }
    expected_output = mock_response["data"]
    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_all_active_data()
        assert result == expected_output


def test_get_latest_data_returns_dict():
    """
    Test that get_latest_data returns a dict
    """
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {
                "symbol": "btc-usd-p-r",
                "timestamp": 1647724800,
            }
        ],
        "params": {"symbol": "btc-usd-p-r", "limit": 1},
    }
    expected_output = mock_response["data"]
    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_latest_data("btc-usd-p-r")
        assert result == expected_output


def test_get_latest_data_raises_exception():
    """
    Test that get_latest_data raises a ValueError
    """
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [],
        "params": {"symbol": "btc-usd-p-r", "limit": 1},
    }
    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_latest_data("btc-usd-p-r")


def test_get_latest_value():
    """
    Test that get_latest_value returns a float
    """
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "btc-usd-p-r", "timestamp": 1647724800, "value": 1000}
        ],
        "params": {"symbol": "btc-usd-p-r", "limit": 1},
    }
    expected_output = mock_response["data"][0]["value"]

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_latest_value("btc-usd-p-r")
        assert result == expected_output


def test_filter_by_symbol():
    """
    Test that _filter_by_symbol returns a list of dicts
    """
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    symbol = "waves-usd-p-d"
    expected_output = [
        {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
    ]
    mock_data = [
        {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
        {"symbol": "ton-usdt-p-5-d", "contrib": ["ton-usdt-p-r"]},
    ]
    result = api._filter_by_symbol(mock_data, symbol)
    assert result == expected_output


def test_get_all_active_data_async_with_frequency_returns_filtered_list():
    """
    Test that get_all_active_data_async returns a list of dicts
    """
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
            {"symbol": "ton-usdt-p-5-r", "contrib": ["ton-usdt-p-r"]},
        ],
        "params": {},
    }
    expected_output = [
        {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]}
    ]
    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_all_active_data(frequency="d")
        assert result == expected_output


def test_get_all_active_data_async_symbol_only_returns_symbol_list():
    """
    Test that get_all_active_data_async returns a list of dicts
    """
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
            {"symbol": "ton-usdt-p-5-d", "contrib": ["ton-usdt-p-r"]},
        ],
        "params": {},
    }
    expected_output = ["waves-usd-p-d", "ton-usdt-p-5-d"]
    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_all_active_data(symbol_only=True)
        assert result == expected_output


def testget_active_data():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
            {"symbol": "ton-usdt-p-5-d", "contrib": ["ton-usdt-p-r"]},
        ],
        "params": {},
    }
    expected_output = {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]}

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_active_data(symbol="waves-usd-p-d")
        assert result == expected_output


def testget_active_data_invalid():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_active_data(symbol="waves-usd-p-d")


def test_get_multi_current_rebalance_weight():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "weights": {"mockweight": 0.5}},
        ],
        "params": {},
    }
    expected_output = {"mockweight": 0.5}

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_multi_current_rebalance_weight(symbol="waves-usd-p-d")
        assert result == expected_output


def test_get_multi_current_rebalance_weight_invalid():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "weights": ""},
        ],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_multi_current_rebalance_weight(symbol="waves-usd-p-d")


def test_get_multi_current_rebalance_weight_invalid_type():
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "weights": ""},
        ],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_multi_current_rebalance_weight(symbol="waves-usd-p-d")


def test_get_single_contributions():
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
        ],
        "params": {},
    }
    expected_output = ["waves-usd-p-r"]

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_single_contributions(symbol="waves-usd-p-d")
        assert result == expected_output


def test_get_single_contributions_invalid_type():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
        ],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_single_contributions(symbol="waves-usd-p-d")


def test_get_single_contributions_invalid():
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "contrib": ""},
        ],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_single_contributions(symbol="waves-usd-p-d")


def test_get_multi_previous_rebalance_date():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {
                "symbol": "waves-usd-p-d",
                "previous_rebalance_date": "2021-01-01",
            },
        ],
        "params": {},
    }
    expected_output = "2021-01-01"

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_multi_previous_rebalance_date(symbol="waves-usd-p-d")
        assert result == expected_output


def test_get_multi_previous_rebalance_date_invalid():
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "previous_rebalance_date": None},
        ],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_multi_previous_rebalance_date(symbol="waves-usd-p-d")


def test_get_multi_previous_review_date():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "previous_review_date": "2021-01-01"},
        ],
        "params": {},
    }
    expected_output = "2021-01-01"

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_multi_previous_review_date(symbol="waves-usd-p-d")
        assert result == expected_output


def test_get_multi_previous_review_date_invalid():
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "previous_review_date": None},
        ],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_multi_previous_review_date(symbol="waves-usd-p-d")


def test_get_multi_next_review_date():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "next_review_date": "2021-01-01"},
        ],
        "params": {},
    }

    expected_output = "2021-01-01"

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_multi_next_review_date(symbol="waves-usd-p-d")
        assert result == expected_output


def test_get_multi_next_review_date_invalid():
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "next_review_date": None},
        ],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_multi_next_review_date(symbol="waves-usd-p-d")


def test_get_multi_next_rebalance_date():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "next_rebalance_date": "2021-01-01"},
        ],
        "params": {},
    }

    expected_output = "2021-01-01"

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_multi_next_rebalance_date(symbol="waves-usd-p-d")
        assert result == expected_output


def test_get_multi_next_rebalance_date_invalid():
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "next_rebalance_date": None},
        ],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_multi_next_rebalance_date(symbol="waves-usd-p-d")


def test_get_multi_next_rebalance_weight():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "next_rebalance_weights": 0.5},
        ],
        "params": {},
    }

    expected_output = 0.5

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_multi_next_rebalance_weight(symbol="waves-usd-p-d")
        assert result == expected_output


def test_get_multi_next_rebalance_weight_invalid():
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "next_rebalance_weights": None},
        ],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_multi_next_rebalance_weight(symbol="waves-usd-p-d")


def test_get_data_by_date():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()

    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {
                "symbol": "waves-usd-p-d",
                "date": "2021-01-01",
            }
        ],
        "params": {},
    }

    expected_output = [
        {
            "symbol": "waves-usd-p-d",
            "date": "2021-01-01",
        }
    ]

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        result = api.get_data_by_date(
            symbol="waves-usd-p-d", date="2021-01-01"
        )
        assert result == expected_output


def test_get_data_by_range_invalid():
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPI(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.Client()

    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [],
        "params": {},
    }

    with patch.object(api.httpx_client, "get", new_callable=Mock) as mock_get:
        mock_get.return_value = Mock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            api.get_data_by_range(symbol="waves-usd-p-d", start="2021-01-01")


def test_invalid_api_key_type():
    api_key = None
    asset_type = "multi_assets"
    with pytest.raises(TypeError):
        VinterAPI(api_key=api_key, asset_type=asset_type)
