## Handling Exceptions

#### Invalid Symbol exception

```python
from vintersdk import VinterAPI

vinter_multi = VinterAPI(APIKEY, "multi_assets")
# How to handle exceptions and get error messages
try:
    # Get data for a non-existent symbol
    invalid_symbol = "BTC"
    data = vinter_multi.get_latest_data(symbol=invalid_symbol, limit=1)
except Exception as e:
    print(f"Exception: {e}")

```

## Get Active Data

Docs [VinterAPI.get_all_active_data][vintersdk.vinter_sdk.VinterAPI.get_all_active_data]

#### Get All Active Multi-Asset Symbols Dictionary

```python
from vintersdk import VinterAPI

vinter_multi = VinterAPI(APIKEY, "multi_assets")

# Get All Active Multi-Asset Symbols Dictionary
active_symbols_multi = vinter_multi.get_all_active_data()
print(active_symbols_multi)
```

#### Get All Active Multi-Asset Symbols only

```python
from vintersdk import VinterAPI

vinter_multi = VinterAPI(APIKEY, "multi_assets")
active_symbols_multi = vinter_multi.get_all_active_data(symbol_only=True)
print(f"Number of total active multi-asset symbols: {len(active_symbols_multi)}")
print(f"First 5 symbols: {active_symbols_multi[:5]}")
```

#### Get All Active Multi-Asset Symbols filter with frequency

```python
from vintersdk import VinterAPI

vinter_multi = VinterAPI(APIKEY, "multi_assets")
# Three frequency options: "r", "d", "h"
active_symbols_multi = vinter_multi.get_all_active_data(symbol_only=True, frequency="r")

print(f"Number of filtered realtime active multi-asset symbols: {len(active_symbols_multi)}")
print(f"First 5 symbols: {active_symbols_multi[:5]}")
```

#### Get active symbol data for a specific symbol

Docs [VinterAPI.get_active_data][vintersdk.vinter_sdk.VinterAPI.get_active_data]

```python
from vintersdk import VinterAPI

vinter_multi = VinterAPI(APIKEY, "multi_assets")
vntr_eq_5_d = vinter_multi.get_active_data("vntr-eq-5-d")
print(vntr_eq_5_d)
```

## Get Latest Data

Docs [VinterAPI.get_latest_data][vintersdk.vinter_sdk.VinterAPI.get_latest_data]

#### Get single data point

```python
from vintersdk import VinterAPI

vinter_multi = VinterAPI(APIKEY, "multi_assets")
data = vinter_multi.get_latest_data(symbol="vntr-eq-5-d", limit=1)
# The data returned is in schema described in the API documentation
print(data)
```

#### Get multiple data points in a pandas dataframe

```python
import pandas as pd
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "multi_assets")
# To get 100 rows of data add limit=100
data = vinter_multi.get_latest_data(symbol="vntr-eq-5-d", limit=100)
# A pandas dataframe can be created from the data
df = pd.DataFrame(data)
# Get shape of the dataframe
print(df.info())
```

#### Get just the latest value

Docs [VinterAPI.get_latest_value][vintersdk.vinter_sdk.VinterAPI.get_latest_value]

```python
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "single_assets")
# Get latest value of a btc-usd-p-d
# As it is a single asset, the instance of the VinterAPI class is different
latest_value_btc_usd = vinter_single.get_latest_value(symbol="btc-usd-p-d")
print(f"Latest BTC-USD Price: {latest_value_btc_usd} , Type: {type(latest_value_btc_usd)}")
```

## Get Historical Data by Date

Docs [VinterAPI.get_data_by_date][vintersdk.vinter_sdk.VinterAPI.get_data_by_date]

```python
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "single_assets")
### Get data for specified dates for a given symbol
get_data_by_date_btc_usd = vinter_single.get_data_by_date(symbol="btc-usd-p-d", date="2023-01-01")
print(get_data_by_date_btc_usd)
```

## Get Historical Data Between Time Ranges

Docs [VinterAPI.get_data_by_range][vintersdk.vinter_sdk.VinterAPI.get_data_by_range]

```python
import pandas as pd
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "single_assets")
# Get data for a single asset for a specific date (2022-01-01 to 2023-01-01)
# The data returned is in schema described in the API documentation
get_data_by_range_btc_usd = vinter_single.get_data_by_range(symbol="btc-usd-p-d", start="2022-01-01", end="2023-01-01")
df = pd.DataFrame(get_data_by_range_btc_usd)
pprint({
    "First Date": df["date"].iloc[0],
    "Last Date": df["date"].iloc[-1]
})
# The end date is not included, the last date is 2022-12-31 instead of 2023-01-01
# Due parsing of the date, the end date is set to 2023-01-01T00:00:00Z
# So the end="2023-01-01T23:59:59Z" will return the last date as 2023-01-01
# Or the end="2023-01-02" will return the last date as 2023-01-01
print("-"*50)
get_data_by_range_btc_usd = vinter_single.get_data_by_range(symbol="btc-usd-p-d", start="2022-01-01", end="2023-01-01T23:59:59Z")
df = pd.DataFrame(get_data_by_range_btc_usd)
pprint({
    "First Date": df["date"].iloc[0],
    "Last Date": df["date"].iloc[-1]
})
```
