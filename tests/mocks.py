from typing import Any

from azure.core.credentials import AccessToken, TokenCredential


class MockAzureCredential(TokenCredential):
    def get_token(
        self,
        *scopes: str,
        claims: str | None = None,
        tenant_id: str | None = None,
        enable_cae: bool = False,
        **kwargs: Any,
    ) -> AccessToken:
        return AccessToken("", 9999999999)


class MockAzureCredentialExpired(TokenCredential):
    def __init__(self):
        self.access_number = 0

    def get_token(
        self,
        *scopes: str,
        claims: str | None = None,
        tenant_id: str | None = None,
        enable_cae: bool = False,
        **kwargs: Any,
    ) -> AccessToken:
        self.access_number += 1
        if self.access_number == 1:
            return AccessToken("", 0)
        else:
            return AccessToken("", 9999999999)
