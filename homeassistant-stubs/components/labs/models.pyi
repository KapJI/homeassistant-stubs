from dataclasses import dataclass, field
from homeassistant.helpers.storage import Store as Store
from typing import Self, TypedDict

class EventLabsUpdatedData(TypedDict):
    domain: str
    preview_feature: str
    enabled: bool

@dataclass(frozen=True, kw_only=True, slots=True)
class LabPreviewFeature:
    domain: str
    preview_feature: str
    is_built_in: bool = ...
    feedback_url: str | None = ...
    learn_more_url: str | None = ...
    report_issue_url: str | None = ...
    @property
    def full_key(self) -> str: ...
    def to_dict(self, *, enabled: bool) -> dict[str, str | bool | None]: ...

@dataclass(kw_only=True)
class LabsStoreData:
    preview_feature_status: set[tuple[str, str]]
    @classmethod
    def from_store_format(cls, data: NativeLabsStoreData | None) -> Self: ...
    def to_store_format(self) -> NativeLabsStoreData: ...

class NativeLabsStoreData(TypedDict):
    preview_feature_status: list[NativeLabsStoredFeature]

class NativeLabsStoredFeature(TypedDict):
    domain: str
    preview_feature: str

@dataclass
class LabsData:
    store: Store[NativeLabsStoreData]
    data: LabsStoreData
    preview_features: dict[str, LabPreviewFeature] = field(default_factory=dict)
