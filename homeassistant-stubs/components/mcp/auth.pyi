import httpx
from dataclasses import dataclass

WWW_AUTHENTICATE_HEADER: str
RESOURCE_METADATA_REGEXP: str
SCOPES_REGEXP: str

@dataclass
class AuthenticateHeader:
    resource_metadata_url: str
    scopes: list[str] | None = ...
    @classmethod
    def from_header(cls, url: str, error_response: httpx.Response) -> AuthenticateHeader | None: ...
