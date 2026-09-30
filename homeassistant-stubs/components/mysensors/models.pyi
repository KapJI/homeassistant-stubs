from .const import DevId as DevId
from _typeshed import Incomplete
from asyncio import Task
from collections import defaultdict
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from mysensors import BaseAsyncGateway as BaseAsyncGateway

type MySensorsConfigEntry = ConfigEntry[MySensorsData]
@dataclass
class MySensorsData:
    gateway: BaseAsyncGateway
    discovered_nodes: set[int] = field(default_factory=set)
    discovered_dev_ids: defaultdict[Platform, set[DevId]] = field(default_factory=Incomplete)
    gateway_start_task: Task[None] | None = ...
