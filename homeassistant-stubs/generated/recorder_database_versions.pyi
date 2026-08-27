from typing import TypedDict

class DatabaseVersions(TypedDict):
    supported_lts: list[str]
    latest_non_lts: str

SUPPORTED_DATABASE_VERSIONS: dict[str, DatabaseVersions]
