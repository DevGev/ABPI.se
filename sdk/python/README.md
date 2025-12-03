<img src="https://i.postimg.cc/5Y75s2D6/full.png" alt="logo" width="120" style="border-radius:5px; display:inline;"/>

# ABPI Python SDK

Python SDK for ABPI.se, visit https://abpi.se for more information. \
Documentation: https://abpi.se/docs


## Installation

Installation through PIP:

```bash
pip install https://github.com/devgev/abpi.se/releases/download/0.1.0/abpi_python-0.1.0.tar.gz
```

## Usage

#### Basic usage

```python
import abpi_python as abpi

abpi_client = abpi.Client()
company = abpi_client.company(organization_number="5560747551")
print(company.basic_info.name) # IKEA of Sweden AB

trademarks = abpi_client.trademarks(organization_number="5560747551")
print(trademarks) # [...]
```


#### Usage with authorization

```python
import abpi_python as abpi

abpi_client = abpi.Client(
    credentials = abpi.Credentials(
        "your_email",             # Email of your ABPI.se account 
        "your_client_name",       # Client name (create in dashboard https://abpi.se/dashboard)
        "your_api_key"            # API key (create in dashboard https://abpi.se/dashboard)
    )
)
```

