import requests
from typing import Dict, Any
from datetime import datetime
import pandas as pd

class BaseAPIClient:
    def __init__(self, base_url: str, api_key: str = None):
        """Initialize API client with base URL and optional API key"""
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})

    def get(self, endpoint: str, params: Dict[str, Any] = None) -> Dict:
        """Execute GET request with error handling and logging"""
        try:
            response = self.session.get(
                f'{self.base_url}/{endpoint.lstrip("/")}',
                params=params
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error making GET request: {str(e)}')
            raise

    def extract_to_dataframe(self, endpoint: str, params: Dict[str, Any] = None) -> pd.DataFrame:
        """Extract API data directly to pandas DataFrame"""
        data = self.get(endpoint, params)
        return pd.json_normalize(data)

    def incremental_extract(self, endpoint: str, date_field: str):
        """Demonstrate incremental extraction pattern"""
        last_run = self._get_last_run_date()
        params = {date_field: last_run.isoformat()}
        return self.get(endpoint, params)

    def _get_last_run_date(self) -> datetime:
        """Mock function to demonstrate incremental load pattern"""
        # In real implementation, this would read from a state store
        return datetime(2024, 1, 1)