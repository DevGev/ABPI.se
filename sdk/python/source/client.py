from .models.company import *
from .models.trademarks import *
from .models.oauth import *
import requests
import time


class Client:

    def __init__(self,
                 credentials: Credentials = None,
                 base_url: str = "https://abpi.se/api"):

        self._base_url: str = base_url if base_url.endswith(
            "/") else base_url + "/"

        self._credentials = credentials

        self._access_token_expiry: int = 0
        self._access_token: OAuthToken = None

        # configurable window dictating how soon before expiry token should be recreated
        self.reauthenticate_before_expiry_window: int = 30

    def company(self, organization_number: str) -> Company:
        json_data = self.__fetch(f"{organization_number}/data")
        return Company.model_validate_json(json_data)

    def company_basic_information(
            self, organization_number: str) -> CompanyBasicInfo:
        json_data = self.__fetch(f"{organization_number}/basic")
        return CompanyBasicInfo.model_validate_json(json_data)

    def company_trademarks(self, organization_number: str) -> Trademarks:
        json_data = self.__fetch(f"{organization_number}/trademarks")
        return Trademarks.model_validate_json(json_data)

    def __authenticate(self):
        if (self._access_token
                and int(time.time() + self.reauthenticate_before_expiry_window)
                < self._access_token_expiry):
            return

        response = requests.post(
            f"{self._base_url}oauth/token",
            json = {
                "email": self._credentials.email,
                "client_name": self._credentials.client_name,
                "api_key": self._credentials.api_key,
            },
        )

        response.raise_for_status()
        json_data = response.text
        token = OAuthToken.model_validate_json(json_data)

        self._access_token_expiry = time.time() + token.expires_in
        self._access_token = token.access_token

    def __fetch(self, endpoint) -> object:
        headers = {}
        if self._credentials:
            self.__authenticate()
            headers["Authorization"] = f"Bearer {self._access_token}"

        response = requests.get(f"{self._base_url}{endpoint}", headers=headers)
        response.raise_for_status()
        return response.text
