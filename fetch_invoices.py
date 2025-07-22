#!/usr/bin/env python3
"""Script to fetch invoices from SuperFaktura."""
import json
from superfaktura.client import SuperFakturaClient


def main():
    client = SuperFakturaClient()
    invoices = client.get_invoices()
    print(json.dumps(invoices, indent=2))


if __name__ == "__main__":
    main()
