# SuperFaktura Integration

This repository contains a minimal Python client for the [SuperFaktura](https://www.superfaktura.sk/) API.

## Setup

1. Install the required dependency `requests`:

```bash
pip install requests
```

2. Set the following environment variables with your SuperFaktura credentials:

- `SF_EMAIL` – your SuperFaktura account email
- `SF_API_KEY` – the API key
- `SF_COMPANY_ID` – the company identifier
- `SF_BASE_URL` – *(optional)* base API URL, defaults to `https://moja.superfaktura.sk/api`

## Fetching invoices

Run the provided script to fetch invoices:

```bash
python fetch_invoices.py
```

The script prints the returned JSON payload of invoices.
