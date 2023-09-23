# Multi Asset Specific Usage

## Get Contributions for a Single Asset

Docs [VinterAPI.get_single_contributions][vintersdk.vinter_sdk.VinterAPI.get_single_contributions]

```python
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "single_assets")
btc_usd_p_r = vinter_single.get_single_contributions(symbol="btc-usd-p-r")
print(btc_usd_p_r)
```
