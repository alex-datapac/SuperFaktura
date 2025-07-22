from unittest.mock import Mock
import sys
import types
import os


def test_get_invoices_returns_expected_structure(monkeypatch):
    # Ensure project root is on the path
    project_root = os.path.dirname(os.path.dirname(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # Provide a minimal stub for the requests module
    fake_requests = types.ModuleType("requests")
    session_mock = Mock()
    fake_requests.Session = Mock(return_value=session_mock)
    sys.modules['requests'] = fake_requests

    from superfaktura.client import SuperFakturaClient

    mock_response = Mock()
    expected_json = {"invoices": [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]}
    mock_response.json.return_value = expected_json
    mock_response.raise_for_status = Mock()
    session_mock.get.return_value = mock_response

    client = SuperFakturaClient(email="e", api_key="k", company_id="c")
    invoices = client.get_invoices()

    assert invoices == expected_json
