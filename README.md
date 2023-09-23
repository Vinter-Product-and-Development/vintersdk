# Getting Started

![Code Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)

The official Python client library for the Vinter.co APIs.

## Installation

```bash
pip install vintersdk
```

## Upgrade

```bash
pip install --upgrade vintersdk
```

## API Documentation

[Vinter API Documentation](https://www.vinterapi.com/)

## Important Notes About the Library

- The library supports both synchronous and asynchronous requests.
- The library is still in development and will be updated frequently.
- All the methods are documented in the source code.
- All the methods are callable from both the synchronous and asynchronous classes.
- The asynchronous class is called VinterAPIAsync.
- The synchronous class is called VinterAPI.
- The asynchronous class repeats the same methods as the synchronous class, but can be called with the await keyword.

## Version of the Library

```python
import vintersdk

print(vintersdk.__version__)
```

## Importing the library

```python
from vintersdk import VinterAPI, VinterAPIAsync
```

## Creating Instances of the VinterAPI class

```python
from vintersdk import VinterAPI

# Create instances of the VinterAPI class
vinter_multi = VinterAPI(APIKEY, "multi_assets")
vinter_single = VinterAPI(APIKEY, "single_assets")
vinter_staking = VinterAPI(APIKEY, "staking_yields")
vinter_nav = VinterAPI(APIKEY, "nav")
```
