import os
import requests

class SuperFakturaClient:
    """Simple client for the SuperFaktura API."""

    DEFAULT_BASE_URL = "https://moja.superfaktura.sk/api"

    def __init__(self, email=None, api_key=None, company_id=None, base_url=None):
        self.email = email or os.getenv("SF_EMAIL")
        self.api_key = api_key or os.getenv("SF_API_KEY")
        self.company_id = company_id or os.getenv("SF_COMPANY_ID")
        self.base_url = base_url or os.getenv("SF_BASE_URL", self.DEFAULT_BASE_URL)
        if not all([self.email, self.api_key, self.company_id]):
            raise ValueError("Missing SuperFaktura credentials")

        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "User-Agent": "SuperFakturaClient/1.0",
        })

    def _auth_params(self):
        return {
            "email": self.email,
            "apikey": self.api_key,
            "company_id": self.company_id,
        }

    def get_invoices(self, page=1, per_page=20):
        """Return list of invoices."""
        params = {"page": page, "per_page": per_page, **self._auth_params()}
        url = f"{self.base_url}/invoices"
        resp = self.session.get(url, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()

    def get_invoice(self, invoice_id):
        """Return single invoice by ID."""
        params = self._auth_params()
        url = f"{self.base_url}/invoice/{invoice_id}"
        resp = self.session.get(url, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
