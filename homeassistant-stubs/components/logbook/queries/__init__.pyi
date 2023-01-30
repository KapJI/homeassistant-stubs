from .all import all_stmt as all_stmt
from .devices import devices_stmt as devices_stmt
from .entities import entities_stmt as entities_stmt
from .entities_and_devices import entities_devices_stmt as entities_devices_stmt
from datetime import datetime as dt
from homeassistant.components.recorder.filters import Filters as Filters
from homeassistant.helpers.json import json_dumps as json_dumps
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement

def statement_for_request(start_day_dt: dt, end_day_dt: dt, event_types: tuple[str, ...], entity_ids: Union[list[str], None] = ..., device_ids: Union[list[str], None] = ..., filters: Union[Filters, None] = ..., context_id: Union[str, None] = ...) -> StatementLambdaElement: ...
