from _typeshed import Incomplete
from collections.abc import Container, Iterable, Sequence
from datetime import timedelta
from jwt import PyJWK, PyJWS, PyJWT
from jwt.algorithms import AllowedPublicKeys
from jwt.types import Options
from typing import Any, override

__all__ = ['unverified_hs256_token_decode', 'verify_and_decode']

class _PyJWSWithLoadCache(PyJWS):
    def _load(self, jwt: str | bytes) -> tuple[bytes, bytes, dict, bytes]: ...

class _PyJWTWithVerify(PyJWT):
    _jws: Incomplete
    def __init__(self) -> None: ...
    def verify_and_decode(self, jwt: str, key: str, algorithms: list[str], issuer: str | None = None, leeway: float | timedelta = 0, options: Options | None = None) -> dict[str, Any]: ...
    @override
    def decode(self, jwt: str | bytes, key: AllowedPublicKeys | PyJWK | str | bytes = '', algorithms: Sequence[str] | None = None, options: Options | None = None, verify: bool | None = None, detached_payload: bytes | None = None, audience: str | Iterable[str] | None = None, subject: str | None = None, issuer: str | Container[str] | None = None, leeway: float | timedelta = 0, **kwargs: Any) -> dict[str, Any]: ...
    @override
    def _decode_payload(self, decoded: dict[str, Any]) -> dict[str, Any]: ...

verify_and_decode: Incomplete

def unverified_hs256_token_decode(jwt: str) -> dict[str, Any]: ...
