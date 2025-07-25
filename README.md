# SuperFaktura Integration

This repository contains a minimal Python client for the [SuperFaktura](https://www.superfaktura.sk/) API.

## Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Set the following environment variables with your SuperFaktura credentials:

- `SF_EMAIL` – your SuperFaktura account email
- `SF_API_KEY` – the API key
- `SF_COMPANY_ID` – the company identifier

## Fetching invoices

Run the provided script to fetch invoices:

```bash
python fetch_invoices.py
```

The script prints the returned JSON payload of invoices.

## Running tests

Install the test dependency `pytest` and execute the suite:

```bash
pip install pytest
pytest
```

