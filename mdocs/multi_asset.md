# Multi Asset Specific Usage

## Get Current Rebalance Weight

Docs [VinterAPI.get_multi_current_rebalance_weight][vintersdk.vinter_sdk.VinterAPI.get_multi_current_rebalance_weight]

```python
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "multi_assets")
vntr_eq_5_d = vinter_multi.get_multi_current_rebalance_weight(symbol="vntr-eq-5-d")
print(vntr_eq_5_d)
```

## Get Previous Rebalance Date

Docs [VinterAPI.get_multi_previous_rebalance_date][vintersdk.vinter_sdk.VinterAPI.get_multi_previous_rebalance_date]

```python
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "multi_assets")
vntr_eq_5_d = vinter_multi.get_multi_previous_rebalance_date(symbol="vntr-eq-5-d")
print(f"Previous Rebalance Date for vntr-eq-5-d: {vntr_eq_5_d}")
```

## Get Previous Review Date

Docs [VinterAPI.get_multi_previous_review_date][vintersdk.vinter_sdk.VinterAPI.get_multi_previous_review_date]

```python
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "multi_assets")
vntr_eq_5_d = vinter_multi.get_multi_previous_review_date(symbol="vntr-eq-5-d")
print(f"Previous Review Date for vntr-eq-5-d: {vntr_eq_5_d}")
```

## Get Next Review Date

Docs [VinterAPI.get_multi_next_review_date][vintersdk.vinter_sdk.VinterAPI.get_multi_next_review_date]

```python
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "multi_assets")
vntr_eq_5_d = vinter_multi.get_multi_next_review_date(symbol="vntr-eq-5-d")
print(f"Next Review Date for vntr-eq-5-d: {vntr_eq_5_d}")
```

## Get Next Rebalance Date

Docs [VinterAPI.get_multi_next_rebalance_date][vintersdk.vinter_sdk.VinterAPI.get_multi_next_rebalance_date]

```python
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "multi_assets")
vntr_eq_5_d = vinter_multi.get_multi_next_rebalance_date(symbol="vntr-eq-5-d")
print(f"Next Rebalance Date for vntr-eq-5-d: {vntr_eq_5_d}")
```

## Get Next Rebalance Weight

Docs [VinterAPI.get_multi_next_rebalance_weight][vintersdk.vinter_sdk.VinterAPI.get_multi_next_rebalance_weight]

```python
from vintersdk import VinterAPI
vinter_multi = VinterAPI(APIKEY, "multi_assets")
vntr_eq_5_d = vinter_multi.get_multi_next_rebalance_weight(symbol="vntr-eq-5-d")
print(f"Next Rebalance Weight for vntr-eq-5-d: {vntr_eq_5_d}")
```
